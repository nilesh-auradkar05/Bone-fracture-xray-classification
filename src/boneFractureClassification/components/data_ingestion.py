import os
import subprocess
import zipfile
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
from boneFractureClassification import logger
from boneFractureClassification.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        self.api = KaggleApi()
        
    def download_file(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        
        try:
            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file
            os.makedirs(Path("artifacts/data_ingestion"), exist_ok=True)
            logger.info(f"Downloading dataset from {dataset_url} into {zip_download_dir}")
            # kaggle datasets download -d bmadushanirodrigo/fracture-multi-region-x-ray-data
            user_name, dataset_id= dataset_url.split("/")[4:]
            
            self.api.dataset_download_files(
                f"{user_name}/{dataset_id}",
                path=Path(zip_download_dir),
                quiet=False,
                unzip=False
            )
            
            logger.info(f"Finished Downloading!. Data stored at {zip_download_dir}")
        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        
        zip_file = [f for f in os.listdir(self.config.local_data_file) if f.endswith(".zip")][0]
        logger.info(f"zipFile's available: {zip_file}")
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(os.path.join(self.config.local_data_file, zip_file), 'r') as zip_ref:
            # zip_ref.printdir()
            for file_info in zip_ref.infolist():
                try:
                    zip_ref.extract(file_info, unzip_path)
                    print(f"Extracted {file_info.filename} into {unzip_path}")
                except Exception as e:
                    print(e)
                    continue
        
        logger.info(f"{zip_file} extracted at {unzip_path}")
        os.remove(os.path.join(self.config.local_data_file, zip_file))