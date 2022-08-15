# Creating a conda environment on a Virtual Machine (notebooks or otherwise)

The instructions for creating conda environments on Compute Engine virtual machines are exactly the same as those for Vertex AI notebooks. The reason is that notebooks have conda pre-installed and so don't play well with changing the conda environment within the notebook.

## 1. Create a conda environment
#install mamba

curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh

bash Mambaforge-$(uname)-$(uname -m).sh -b -p $HOME/mambaforge

export PATH="$HOME/mambaforge/bin:$PATH"

mamba create -n rapids -c rapidsai -c nvidia -c conda-forge rapids=22.06 python=3.8 cudatoolkit=11.5 ipykernel

source activate rapids

python -m ipykernel install --user --name=rapids

## Create a custom kernel in cloud-based Juptyer notebook

