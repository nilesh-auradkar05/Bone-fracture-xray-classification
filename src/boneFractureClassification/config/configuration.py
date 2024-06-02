import os
from pathlib import Path
from boneFractureClassification.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from boneFractureClassification.utils.common import read_yaml, create_directories
from boneFractureClassification.entity.config_entity import (
    DataIngestionConfig,
    BaseModelConfig,
    ModelTrainingConfig,
)


class ConfigurationManager:
    def __init__(
        self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # calling config/config.yaml attribute "artifacts_root" which returns artifacts as value which is a folder name to be created.
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        # calling root_dir attribute from config/config.yaml which returns path
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )

        return data_ingestion_config

    def get_base_model_config(self) -> BaseModelConfig:
        config = self.config.base_model

        create_directories([config.root_dir])
        create_directories([config.custom_train_model_dir])

        base_model_config = BaseModelConfig(
            root_dir=Path(config.root_dir),
            custom_train_model_dir=Path(config.custom_train_model_dir),
            base_model_path=Path(config.base_model_path),
            custom_trained_model_path=Path(config.custom_trained_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES,
        )

        return base_model_config

    def get_model_training_config(self) -> ModelTrainingConfig:
        training = self.config.model_training
        base_model = self.config.base_model
        params = self.params

        training_data = os.path.join(
            self.config.data_ingestion.local_data_file,
            "Bone_Fracture_Binary_Classification/train",
        )
        validation_data = os.path.join(
            self.config.data_ingestion.local_data_file,
            "Bone_Fracture_Binary_Classification/val",
        )

        create_directories([Path(training.root_dir)])

        model_training_config = ModelTrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.model_training_path),
            custom_trained_model_path=Path(base_model.custom_trained_model_path),
            training_data=Path(training_data),
            validation_data=Path(validation_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE,
        )

        return model_training_config
