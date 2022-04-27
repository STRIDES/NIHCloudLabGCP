# Spleen Segmentation with Liver Example using NVIDIA Models and MONAI
_We have put together a training example that segments the Spleen in 3D CT Images. At the end is an example of combining both the Spleen model and the Liver model._

## Introduction
Two pre-trained models from NVIDIA are used in this training, a Spleen model and Liver. 
The Spleen model is additionally retrained on the medical decathlon spleen dataset: [http://medicaldecathlon.com/](http://medicaldecathlon.com/)
Data is not necessary to be downloaded to run the notebook. The notebook downloads the data during it's run.
The notebook uses the Python package [MONAI](https://monai.io/), the Medical Open Network for Artificial Intelligence. 

- Spleen Model - [clara_pt_spleen_ct_segmentation_V2](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/med/models/clara_pt_spleen_ct_segmentation)
- Liver Model - [clara_pt_liver_and_tumor_ct_segmentation_V1](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/med/models/clara_pt_liver_and_tumor_ct_segmentation)

## Outcomes
After following along with this notebook the user will be familiar with:
- Downloading public datasets using MONAI
- Using MONAI transformations for training
- Downloading a pretrained NVIDIA Clara model using MONAI
- Retrain model using MONAI
- Visualizing medical images in python/matplotlib

## Installing MONAI
Please follow the [instructions](https://monai.io/started.html#installation) on MONAI's website for up to date install.
Installing MONAI in a notebook environment can be completed with the commands:
- !python -c "import monai" || pip install -q 'monai[all]'
- !python -c "import matplotlib" || pip install -q matplotlib

## Dependencies
_It is recommended to use an NVIDIA GPU for training. If the user does not have access to a NVIDIA GPU then it is recommended to skip the training cells._

The following packages and versions were installed during the testing of this notebook:
- MONAI version: 0.8.1
- Numpy version: 1.21.1
- Pytorch version: 1.9.0
- Pytorch Ignite version: 0.4.8
- Nibabel version: 3.2.1
- scikit-image version: 0.18.2
- Pillow version: 8.3.1
- Tensorboard version: 2.5.0
- gdown version: 3.13.0
- TorchVision version: 0.10.0+cu111
- tqdm version: 4.61.2
- lmdb version: 1.2.1
- psutil version: 5.8.0
- pandas version: 1.3.0
- einops version: 0.3.0
- transformers version: 4.18.0
- mlflow version: 1.25.1
