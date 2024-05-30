from boneFractureClassification import logger
from boneFractureClassification.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"{STAGE_NAME}")
    dataPipeline = DataIngestionPipeline()
    dataPipeline.main()
    logger.info(f"{STAGE_NAME} completed!")
except Exception as e:
    logger.exception(e)
    raise e

