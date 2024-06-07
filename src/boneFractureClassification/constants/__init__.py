from pathlib import Path
from dotenv import dotenv_values

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
DVC_FILE_PATH = Path("dvc.yaml")

dagshub = dotenv_values(".env")
MLFLOW_TRACKING_URI = dagshub.get("MLFLOW_TRACKING_URI")
MLFLOW_TRACKING_USERNAME = dagshub.get("MLFLOW_TRACKING_USERNAME")
MLFLOW_TRACKING_PASSWORD = dagshub.get("MLFLOW_TRACKING_PASSWORD")
