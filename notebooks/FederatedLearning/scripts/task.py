# Importing Libraries
import os
import torch
import numpy as np
import pandas as pd
import torch.nn as nn
# import matplotlib.pyplot as plt

# from torch.nn import Sequential
# from collections import OrderedDict
# from torch.utils.data import Dataset, DataLoader
# from sklearn.preprocessing import StandardScaler
# from google.cloud import storage
# from io import BytesIO

# # BreastCancerDataset Class
# class BreastCancerDataset(Dataset):
#     def __init__(self, df):
#         scaler = StandardScaler()
#         self.X = torch.tensor(scaler.fit_transform(df.iloc[:,1:-1].values))   # first (ID) and last (diagnosis) columns are excluded
#         self.y =  torch.tensor(df.iloc[:,-1].values)                          # load the diagnosis (malignant=1, benign=0)

#     def __len__(self):
#         return len(self.X)

#     def __getitem__(self, idx):
#         return self.X[idx], self.y[idx]

# # # Function to Load Data from GCS 
# # # Description: This function stores downloads files from cloud storage and reads them into a pandas dataframe. 
# # def load_dataset_from_gcs(bucket_name, file_path):
# #     client = storage.Client()
# #     bucket = client.get_bucket(bucket_name)
# #     blob = bucket.blob(file_path)
# #     data = blob.download_as_string()
# #     df = pd.read_csv(BytesIO(data))
# #     return df

# # Client Class (same as above)
# class Client:
#     def __init__(self, name, model, train_loader, val_loader, optimizer, criterion):
#         self.name = name
#         self.model = model
#         self.optimizer = optimizer
#         self.criterion = criterion
#         self.train_loader = train_loader
#         self.val_loader = val_loader
#         self.metrics = dict({"train_acc": list(), "train_loss": list(), "val_acc": list(), "val_loss": list()})

#         print(f"[INFO] Initialized client '{self.name}' with {len(train_loader.dataset)} train and {len(val_loader.dataset)} validation samples")

#     def train(self):
#         """
#             Trains the model of the client for 1 epoch.
#         """
#         self.model.train()
#         correct_predictions = 0
#         running_loss = 0.0

#         # iterate over training dataset
#         for inputs, labels in self.train_loader:
#             # make predictions
#             self.optimizer.zero_grad()
#             outputs = self.model(inputs)
#             labels = torch.unsqueeze(labels, 1)

#             # apply gradient
#             loss = self.criterion(outputs, labels)
#             loss.backward()
#             self.optimizer.step()
#             running_loss += loss.item()

#             # calculate number of correct predictions
#             predicted = torch.round(outputs)
#             correct_predictions += (predicted == labels).sum().item()

#         # calculate overall loss and acc.
#         epoch_loss = running_loss / len(self.train_loader)
#         accuracy = correct_predictions / len(self.train_loader.dataset)

#         # save metrics
#         self.metrics["train_acc"].append(accuracy)
#         self.metrics["train_loss"].append(epoch_loss)

#     def validate(self):
#         """
#             Validates the model of the client based on the given validation data loader.
#         """
#         self.model.eval()
#         total_loss = 0
#         correct_predictions = 0

#         # iterate over validation data loader and make predictions
#         with torch.no_grad():
#             for inputs, labels in self.val_loader:
#                 outputs = self.model(inputs)
#                 labels = torch.unsqueeze(labels, 1)
#                 loss = self.criterion(outputs, labels)

#                 total_loss += loss.item()
#                 predicted = torch.round(outputs)
#                 correct_predictions += (predicted == labels).sum().item()

#         # calculate overall loss and acc.
#         average_loss = total_loss / len(self.val_loader)
#         accuracy = correct_predictions / len(self.val_loader.dataset)

#         # save metrics
#         self.metrics["val_acc"].append(accuracy)
#         self.metrics["val_loss"].append(average_loss)

# SimpleNN Model Definition (same as above)
class SimpleNN(nn.Module):
    def __init__(self, n_input):
        super(SimpleNN, self).__init__()
        self.NN = Sequential(
            nn.Linear(n_input, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16,1),
            nn.Sigmoid()
        )

    def forward(self, x):
        logits = self.NN(x)
        return logits

# FedAvg Function (same as above)

# def fed_avg(global_state_dict, client_states, n_data_points):
#     """
#     Averages the weights of client models to update the global model by FedAvg.

#     Args:
#         global_state_dict: The state dict of the global PyTorch model.
#         client_states: A list of PyTorch models state dicts representing client models.
#         n_data_points: A list with the number of data points per client.

#     Returns:
#         The state dict of the updated global PyTorch model.
#     """
#     averaged_state_dict = OrderedDict()

#     for key in global_state_dict.keys():
#         for state, n in zip(client_states, n_data_points):
#             averaged_state_dict[key] =+ state[key] * (n/ sum(n_data_points))

#     return averaged_state_dict

# # FLServer Class
# class FLServer:
#     def __init__(self, model, clients):
#         self.model = model
#         self.clients = clients
#         self.n_data_points = [len(client.train_loader.dataset) for client in self.clients]

#     def run(self, epochs):
#         for i in range(epochs):
#             print(f"Epoch {i}")

#             # Step 2 of figure at the beginning of the tutorial
#             for client in self.clients:
#                 client.train()

#             # aggregate the models using FedAvg (Step 3 & 4 of figure at the beginning of the tutorial)
#             client_states = [client.model.state_dict() for client in self.clients]                 # Step 3
#             aggregated_state = fed_avg(self.model.state_dict(), client_states, self.n_data_points) # Step 4
#             self.model.load_state_dict(aggregated_state)

#             # redistribute central model (Step 1 of figure at the beginning of the tutorial)
#             for client in fl_server.clients:
#                 client.model.load_state_dict(aggregated_state)

#             # run validation of aggregated model
#             for client in self.clients:
#                 client.validate()

#             # repeat for n epochs (Step 5 of figure at the beginning of the tutorial)

# # Plotting Metrics
# def plot_metrics(client):
#     plt.figure(figsize=(8, 4))
#     for k, v in client.metrics.items():
#         x_vals = range(len(v))
#         plt.plot(x_vals, v, label=k)

#     plt.ylim(bottom=0.0, top=1.0)
#     plt.xlim(left=0)
#     plt.xlabel("Epoch")
#     plt.ylabel("Metric")
#     plt.title(client.name)
#     plt.legend()
#     plt.show()

# # Main Function
# def main():
#     import argparse
#     #arguments are parsed from the command line
#     parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
#     parser.add_argument('--bucket_name', type=str, required=True, help='GCS bucket name')
#     parser.add_argument('--train_file', type=str, required=True, help='Path to the training file in GCS')
#     parser.add_argument('--validation_file', type=str, required=True, help='Path to the validation file in GCS')
#     parser.add_argument('--output_dir', type=str, required=True, help='Output directory for the model in GCS')
#     parser.add_argument('--epochs', type=int, default=10, help='Number of epochs to train')
#     parser.add_argument('--batch_size', type=int, default=50, help='Batch size for training')
#     args = parser.parse_args()

#     # Load datasets from GCS
#     train_df = load_dataset_from_gcs(args.bucket_name, args.train_file)
#     val_df = load_dataset_from_gcs(args.bucket_name, args.validation_file)

#     train_data = BreastCancerDataset(train_df)
#     val_data = BreastCancerDataset(val_df)

#     train_dataloader = DataLoader(train_data, batch_size=args.batch_size, shuffle=True)
#     val_dataloader = DataLoader(val_data, batch_size=args.batch_size, shuffle=False)

#     # Initialize model and client for centralized training
#     model = SimpleNN(n_input=30)
#     optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
#     criterion = nn.BCELoss()
#     central_client = Client("central", model, train_dataloader, val_dataloader, optimizer, criterion)

#     # Centralized training
#     for i in range(args.epochs):
#         print(f"Epoch {i}")
#         central_client.train()
#         central_client.validate()

#     plot_metrics(central_client)

#     print("Accuracy of the centrally trained model:")
#     run_prediction(central_client.model, args.bucket_name, args.test_file)

#     # Federated Learning
#     fed_model = SimpleNN(n_input=30)
#     clients = list()
#     for i in range(2):
#         train_df = load_dataset_from_gcs(args.bucket_name, f"client_{i}/train_data.csv")
#         val_df = load_dataset_from_gcs(args.bucket_name, f"client_{i}/val_data.csv")

#         train_data = BreastCancerDataset(train_df)
#         val_data = BreastCancerDataset(val_df)

#         train_dataloader = DataLoader(train_data, batch_size=7, shuffle=True)
#         val_dataloader = DataLoader(val_data, batch_size=7, shuffle=False)

#         optimizer = torch.optim.SGD(fed_model.parameters(), lr=0.01, momentum=0.9)
#         criterion = nn.BCELoss()

#         clients.append(Client(f"client_{i}", fed_model, train_dataloader, val_dataloader, optimizer, criterion))

#     fl_server = FLServer(fed_model, clients)

#     for client in fl_server.clients:
#         client.model.load_state_dict(fl_server.model.state_dict())

#     fl_server.run(epochs=args.epochs)

#     for client in fl_server.clients:
#         plot_metrics(client)

#     print("Model trained with federated learning accuracy:")
#     run_prediction(fl_server.model, args.bucket_name, args.test_file)

#     # Save the model to GCS
#     client = storage.Client()
#     bucket = client.get_bucket(args.bucket_name)
#     model_path = os.path.join(args.output_dir, "fed_model.pth")
#     torch.save(fed_model.state_dict(), model_path)
#     bucket.blob(model_path).upload_from_filename(model_path)

# if __name__ == "__main__":
#     main()
