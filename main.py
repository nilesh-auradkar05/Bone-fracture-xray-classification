from boneFractureClassification import logger
from boneFractureClassification.pipeline.stage_01_data_ingestion import (
    DataIngestionPipeline,
)
from boneFractureClassification.pipeline.stage_02_base_model import (
    PrepareBaseModelTrainingPipeline,
)
from boneFractureClassification.pipeline.stage_03_train_model import (
    ModelTrainingPipeline,
)

from boneFractureClassification.pipeline.stage_04_model_evaluation_and_logging import (
    ModelInferencePipeline,
)

# STAGE_NAME = "Data Ingestion Stage"

"""try:
    logger.info(f"{STAGE_NAME}")
    dataPipeline = DataIngestionPipeline()
    dataPipeline.main()
    logger.info(f"{STAGE_NAME} completed!")

except Exception as e:
    logger.exception(e)
    raise e
"""
# STAGE_NAME = "Prepare Base Model"
"""
try:
    logger.info(f"{STAGE_NAME}")
    prepare_base_model_pipeline = PrepareBaseModelTrainingPipeline()
    prepare_base_model_pipeline.main()
    logger.info(f"{STAGE_NAME} completed!")
except Exception as e:
    logger.exception(e)
    raise e
"""

STAGE_NAME = "Model Training"

try:
    logger.info(f"{STAGE_NAME}")
    model_training_pipeline = ModelTrainingPipeline()
    model_training_pipeline.main()
    logger.info(f"{STAGE_NAME} completed!")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "MODEL INFERENCE"

try:
    logger.info(f"{STAGE_NAME}")
    model_inference_pipeline = ModelInferencePipeline()
    model_inference_pipeline.main()
    logger.info(f"{STAGE_NAME} finished!")
except Exception as e:
    logger.exception(e)
    raise e
