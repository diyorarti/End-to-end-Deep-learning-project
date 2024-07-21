from datetime import datetime 
from typing import List
import torch

TIMESTAMP: datetime = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

# Data ingestion constants
ARTIFACTS_DIR: str = "artifacts"
FOLDER_NAME = "Data"
GD_ZIP_FILE_PATH = "https://drive.google.com/file/d/1lrZNdDcrlHWY6Te2sl-3d5aQ3HaoB1Ke/view?usp=sharing"
ZIP_FILE_NAME = 'Xray_dataset.zip'
DATA_INGESTION_DATA_DIR = "data"