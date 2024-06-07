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


class ModelTrainingConfig(BaseModel):
    root_dir: Path
    trained_model_path: Path
    custom_trained_model_path: Path
    training_data: Path
    validation_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list


class InferenceConfig(BaseModel):
    path_to_model: Path
    training_data: Path
    all_params: dict
    mlflow_uri: str
    params_image_size: list
    params_batch_size: int
