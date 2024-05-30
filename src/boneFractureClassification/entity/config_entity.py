from pydantic import BaseModel
from pathlib import Path

# model attribute values are defined in config.yaml
class DataIngestionConfig(BaseModel):
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path