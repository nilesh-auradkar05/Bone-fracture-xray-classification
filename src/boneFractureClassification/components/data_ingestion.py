import os
import opendatasets as od
from boneFractureClassification import logger
from boneFractureClassification.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        
        try:
            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading dataset from {dataset_url} into {zip_download_dir}")
            
            user_name, dataset_id = dataset_url.split("/")[4:]
            prefix_url = "https://www.kaggle.com/datasets/"
            od.download(prefix_url+user_name+"/"+dataset_id,data_dir=zip_download_dir)
            
            logger.info(f"Finished Downloading!. Data stored at {zip_download_dir}")
        except Exception as e:
            raise e