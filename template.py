import os
from pathlib import Path
import logging

# We are maintaining the log information along with the format
logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]:%(message)s:')

project_name = "cnnClassifier"

# List of file need to be created
list_of_files = [
    # If we get .yaml file we can remove .gitkeep file
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

]

for filepath in list_of_files:
    # Handle "/" issue of windows while accessing any directory
    filepath = Path(filepath)

    # Get file directory and file name 
    filedir, filename = os.path.split(filepath)

    # Create file directory if not present
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        # Create log
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # If the file doesn't exist or there is nothing written in the file
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        # Open a file
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    # If the file already exists
    else:
        logging.info(f"{filename} is already exists")