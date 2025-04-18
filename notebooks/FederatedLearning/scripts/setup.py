from setuptools import find_packages
from setuptools import setup

setup(
    name='breast_cancer_federated_learning',
    version='0.1',
    install_requires=[
        'torch',
        'numpy',
        'pandas',
        'matplotlib',
        'scikit-learn',
        'google-cloud-storage',
        'google-cloud-aiplatform',
    ],
    packages=find_packages(),
    include_package_data=True,
    description='Breast Cancer Federated Learning Training Script',
)
