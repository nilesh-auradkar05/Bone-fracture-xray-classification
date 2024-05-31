from pydantic import BaseModel
from pathlib import Path

# model attribute values are defined in config.yaml
class DataIngestionConfig(BaseModel):
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
    
class BaseModelConfig(BaseModel):
    root_dir: Path
    base_model_path: Path
    custom_trained_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int