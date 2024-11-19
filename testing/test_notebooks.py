import os
import json
import pytest
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# Read configuration from a JSON file (injected via workflow)
def load_configuration(config_file="env.json"):
    if os.path.exists(config_file):
        with open(config_file) as f:
            return json.load(f)
    return {}

# Parameterize the tests with notebook paths
@pytest.mark.parametrize("notebook_path", [
    "notebooks/GenAI/Gemini_Intro.ipynb",
])
def test_notebook_execution(notebook_path):
    config = load_configuration()
    parameters = {
        "API_KEY": config.get("NOTEBOOK_PROJECT_ID", ""),
        "DB_URL": config.get("NOTEBOOK_GCP_LOCATION", ""),
    }

    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        
        # Inject parameters into the notebook via metadata
        nb.metadata["parameters"] = parameters
        ep.preprocess(nb, {'metadata': {'path': './'}})
