import os
from box.exceptions import BoxValueError
import yaml
from boneFractureClassification import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads yaml file from the given path.

    Args:
        path_to_yaml (str): input received from calling function.

    Raises:
        BoxValueError: If yaml file is empty
        e: Empty file

    Returns:
        ConfigBox: Returns ConfigBox Type. Which helps to access attributes using "." operator in python
    """
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully!")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is Empty.")
    except Exception as e:
        raise e
    

@ensure_annotations
def save_json(path: Path, data: dict):
    """_summary_

    Args:
        path (Path): _description_
        data (dict): _description_
    """
    
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file saved at: {path}")
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """_summary_

    Args:
        path_to_directories (list): _description_
        verbose (bool, optional): _description_. Defaults to True.
    """
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """_summary_

    Args:
        path (Path): _description_

    Returns:
        ConfigBox: _description_
    """
    
    with open(path) as f:
        content = json.load(f)
        
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """_summary_

    Args:
        data (Any): _description_
        path (Path): _description_
    """
    
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """_summary_

    Args:
        path (Path): _description_

    Returns:
        Any: _description_
    """
    
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    
@ensure_annotations
def get_size(path: Path) -> str:
    """_summary_

    Args:
        path (Path): _description_

    Returns:
        str: _description_
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"

def decodeImage(imgString, fileName):
    imageData = base64.b64decode(imgString)
    with open(fileName, "wb") as f:
        f.write(imageData)
        f.close()
        
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())