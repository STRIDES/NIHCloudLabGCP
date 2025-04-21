import os
import torch

import pickle
import numpy as np
import pandas as pd
import torch.nn as nn
import matplotlib.pyplot as plt

from kfp.v2 import compiler
from torch.nn import Sequential
from collections import OrderedDict
from google.cloud import aiplatform
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from kfp.v2.dsl import component, Output, Dataset, Model, Input, Artifact, Metrics
from sklearn.preprocessing import StandardScaler

class SimpleNN(nn.Module):
    def __init__(self, n_input):
        super(SimpleNN, self).__init__()
        self.NN = Sequential(
            nn.Linear(n_input, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 1),
            nn.Sigmoid()
        )
    def forward(self, x):
        return self.NN(x)
    
class BreastCancerDataset(Dataset):
    def __init__(self, df):
        scaler = StandardScaler()
        self.X = torch.tensor(scaler.fit_transform(df.iloc[:,1:-1].values))   # first (ID) and last (diagnisis) columns are excluded
        self.y =  torch.tensor(df.iloc[:,-1].values)                          # load the diagnosis (malignant=1, benign=0)
    
    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]
    
class Client:
    def __init__(self, name, model, train_loader, val_loader, optimizer, criterion):
        self.name = name
        self.model = model
        self.optimizer = optimizer
        self.criterion = criterion
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.metrics = dict({"train_acc": list(), "train_loss": list(), "val_acc": list(), "val_loss": list()})

        print(f"[INFO] Initialized client '{self.name}' with {len(train_loader.dataset)} train and {len(val_loader.dataset)} validation samples")
        
        
    def train(self):
        """
            Trains the model of the client for 1 epoch.
        """
        self.model.train()
        correct_predictions = 0
        running_loss = 0.0

        # iterate over training dataset
        for inputs, labels in self.train_loader:
            # make predictions
            self.optimizer.zero_grad()
            outputs = self.model(inputs)
            labels = torch.unsqueeze(labels, 1)

            # apply gradient
            loss = self.criterion(outputs, labels)
            loss.backward()
            self.optimizer.step()
            running_loss += loss.item()

            # calculate number of correct predictions
            predicted = torch.round(outputs)
            correct_predictions += (predicted == labels).sum().item()

        # calculate overall loss and acc.
        epoch_loss = running_loss / len(self.train_loader)
        accuracy = correct_predictions / len(self.train_loader.dataset)

        # save metrics
        self.metrics["train_acc"].append(accuracy)
        self.metrics["train_loss"].append(epoch_loss)
    
    def validate(self):
        """
            Validates the model of the client based on the given validation data loader.
        """
        self.model.eval()
        total_loss = 0
        correct_predictions = 0

        # iterate over validation data loader and make predictions
        with torch.no_grad():
            for inputs, labels in self.val_loader:
                outputs = self.model(inputs)
                labels = torch.unsqueeze(labels, 1)
                loss = self.criterion(outputs, labels)

                total_loss += loss.item()
                predicted = torch.round(outputs)
                correct_predictions += (predicted == labels).sum().item()

        # calculate overall loss and acc.
        average_loss = total_loss / len(self.val_loader)
        accuracy = correct_predictions / len(self.val_loader.dataset)

        # save metrics
        self.metrics["val_acc"].append(accuracy)
        self.metrics["val_loss"].append(average_loss)

class FLServer:
    def __init__(self, model, clients):
        self.model = model
        self.clients = clients
        self.n_data_points = [len(client.train_loader.dataset) for client in self.clients]

    def run(self, epochs):
        for i in range(epochs):
            print(f"Epoch {i}")

            # Step 2 of figure at the beginning of the tutorial
            for client in self.clients:
                client.train()

            # aggregate the models using FedAvg (Step 3 & 4 of figure at the beginning of the tutorial)
            client_states = [client.model.state_dict() for client in self.clients]                 # Step 3
            aggregated_state = fed_avg(self.model.state_dict(), client_states, self.n_data_points) # Step 4
            self.model.load_state_dict(aggregated_state)
            
            # redistribute central model (Step 1 of figure at the beginning of the tutorial)
            for client in fl_server.clients:
                client.model.load_state_dict(aggregated_state)

            # run validation of aggregated model
            for client in self.clients:
                client.validate()

            # repeat for n epochs (Step 5 of figure at the beginning of the tutorial