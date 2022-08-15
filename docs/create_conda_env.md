# Creating a conda environment on a Virtual Machine (notebooks or otherwise)

The instructions for creating conda environments on Compute Engine virtual machines are exactly the same as those for Vertex AI notebooks. The reason is that notebooks have conda pre-installed and so don't play well with changing the conda environment within the notebook. Thus, if you are using a notebook, follow all steps from within a terminal, which you can access from the launcher. 

<img src="/images/launch_terminal.png" width="350" height="200">

## 1. Create a conda environment

### Install mamba
curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh
bash Mambaforge-$(uname)-$(uname -m).sh -b -p $HOME/mambaforge

### Export to Path
export PATH="$HOME/mambaforge/bin:$PATH"

From within the notebook you can add Mamba to path with 
```
import os
os.environ["PATH"] += os.pathsep + os.environ["HOME"]+"/Mambaforge/bin"
```

### Create and activate the environment
mamba create -n vcftools -c bioconda vcftools ipykernel -y

source activate vcftools

## 2. Create a custom kernel for your notebook instance

### Create the kernel using ipykernel

python -m ipykernel install --user --name=vcftools

### Open the kernel 

Now you can switch to the kernel either from the launcher

<img src="/images/launcher_env.png" width="350" height="200">


Or, from the top right from within the notebook.

<img src="/images/kernel.png" width="350" height="200">
