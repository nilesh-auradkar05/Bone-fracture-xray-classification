from boneFractureClassification import logger
from boneFractureClassification.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from boneFractureClassification.pipeline.stage_02_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"{STAGE_NAME}")
    dataPipeline = DataIngestionPipeline()
    dataPipeline.main()
    logger.info(f"{STAGE_NAME} completed!")
    
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f"{STAGE_NAME}")
    prepare_base_model_pipeline = PrepareBaseModelTrainingPipeline()
    prepare_base_model_pipeline.main()
    logger.info(f"{STAGE_NAME} completed!")
except Exception as e:
    logger.exception(e)
    raise e 
