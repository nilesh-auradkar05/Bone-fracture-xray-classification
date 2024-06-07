from boneFractureClassification.config.configuration import ConfigurationManager
from boneFractureClassification.components.inference import Inference
from boneFractureClassification import logger

STAGE_NAME = "MODEL INFERENCE"


class ModelInferencePipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        inference_config = config.get_inference_config()
        inference = Inference(inference_config)
        inference.inference()
        inference.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME}")
        model_inference_pipeline = ModelInferencePipeline()
        model_inference_pipeline.main()
        logger.info(f"{STAGE_NAME} finished!")
    except Exception as e:
        logger.exception(e)
        raise e
