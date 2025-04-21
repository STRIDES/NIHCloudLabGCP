from setuptools import find_packages, setup

# File: setup.py
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "torch",
        "pandas", 
        "scikit-learn",
        "matplotlib",
        "ordereddict"  # Add any dependencies your package needs
    ],
)
