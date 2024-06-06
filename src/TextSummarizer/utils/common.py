import os
from box.exceptions import BoxValueError # type: ignore
import yaml
from TextSummarizer.logging import logger
from ensure import ensure_annotations # type: ignore
from box import ConfigBox # type: ignore
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(file_path: Path) -> ConfigBox:
    """
    Read a yaml file and return a ConfigBox object
    """
    try:
        with open(file_path) as file:
            data = yaml.safe_load(file)
            logger.info(f"yaml file: {file_path} Loaded successfully.")
        return ConfigBox
    except BoxValueError as e:
        logger.error(f"Error reading yaml file: {file_path}")
        raise e
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True) -> None:
    """
    Create directories if they don't exist
    """
    for directory in path_to_directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            if verbose:
                logger.info(f"Directory created: {directory}")
        else:
            if verbose:
                logger.info(f"Directory already exists: {directory}")



@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in KB
    """
    size = round(os.path.getsize(path)/1024)
    return f"~{size} KB"