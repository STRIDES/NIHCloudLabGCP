# Setting Up the Environment to Run AlphaFold on Vertex AI

## 1. Install Mamba (via Mambaforge)
Use the following commands to install Mambaforge:

```bash
# Download the Mambaforge installer
curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh

# Install Mambaforge to your home directory
bash Mambaforge-$(uname)-$(uname -m).sh -b -p $HOME/mambaforge

# Use mamba to install required Python packages
$HOME/mambaforge/bin/mamba install -y -c conda-forge pandas-gbq pandas
```
## 2. Install Google Colab Package
Use the following command to install google-colab: 

```bash
pip install google-colab
```
