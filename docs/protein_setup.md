!curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh
!bash Mambaforge-$(uname)-$(uname -m).sh -b -p $HOME/mambaforge

!../../mambaforge/bin/mamba install -y -c conda-forge pandas-gbq pandas

pip install google-colab
