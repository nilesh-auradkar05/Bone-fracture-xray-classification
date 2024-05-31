from boneFractureClassification.config.configuration import ConfigurationManager
from boneFractureClassification.components.model import BaseModel
from boneFractureClassification import logger

STAGE_NAME = "Prepare Base Model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        base_model_config = config.get_base_model_config()
        base_model = BaseModel(config=base_model_config)
        base_model.get_base_model()
        base_model.custom_train_model()
        
if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME}")
        prepareBaseModelPipeline = PrepareBaseModelTrainingPipeline()
        prepareBaseModelPipeline.main()
        logger.info(f"{STAGE_NAME} completed!")
    except Exception as e:
        logger.exception(e)
        raise e