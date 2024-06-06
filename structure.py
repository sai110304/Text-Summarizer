import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

projectName='TextSummarizer'

listOfPaths = {
    ".github/workflows/.gitkeep",
    f"src/{projectName}/__init__.py",
    f"src/{projectName}/components/__init__.py",
    f"src/{projectName}/utils/__init__.py",
    f"src/{projectName}/utils/common.py",
    f"src/{projectName}/logging/__init__.py",
    f"src/{projectName}/config/__init__.py",
    f"src/{projectName}/config/config.py",
    f"src/{projectName}/pipeline/__init__.py",
    f"src/{projectName}/entity/__init__.py",
    f"src/{projectName}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "requirements.txt",
    "Dockerfile",
    'setup.py',
    "research/trials.ipynb"
}


for path in listOfPaths:
    file_path=Path(path)
    file_dir, file_name = os.path.split(file_path)
    
    if file_dir:
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f"Creating file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")