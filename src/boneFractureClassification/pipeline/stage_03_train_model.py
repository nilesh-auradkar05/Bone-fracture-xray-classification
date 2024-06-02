from boneFractureClassification.config.configuration import ConfigurationManager
from boneFractureClassification.components.model_train import ModelTraining
from boneFractureClassification import logger

STAGE_NAME = "Model Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_model_training_config()
        train = ModelTraining(config=training_config)
        train.load_base_model()
        train.train_val_data_generator()
        train.train_model()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME}")
        model_training_pipeline = ModelTrainingPipeline()
        model_training_pipeline.main()
        logger.info(f"{STAGE_NAME} completed!")
    except Exception as e:
        logger.exception(e)
        raise e
