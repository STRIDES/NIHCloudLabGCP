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
        "NOTEBOOK_GCP_PROJECT_ID": config.get("NOTEBOOK_GCP_PROJECT_ID", ""),
        "NOTEBOOK_GCP_LOCATION": config.get("NOTEBOOK_GCP_LOCATION", ""),
    }

    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
        
        # Inject parameters into the notebook via metadata
        nb.metadata["parameters"] = parameters

        # Check if metadata is updated correctly
        print("Injected Metadata:", nb.metadata.get('parameters'))

        exec_globals = {}
        for idx, cell in enumerate(nb.cells):
            if cell.cell_type == "code":
                print(f"Executing Cell {idx}:")
                print(cell['source'][:100])  # Print the first 100 characters of the cell source
                try:
                    exec(cell.source, exec_globals)
                except Exception as e:
                    print(f"Error in Cell {idx}: {e}")


        #for idx, cell in enumerate(nb.cells):
        #    print(f"Cell {idx} Type: {cell['cell_type']}")
        #    print(cell['source'][:100])  # Print the first 100 characters of the cell source

        #ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        #ep.preprocess(nb, {'metadata': {'path': './'}})
