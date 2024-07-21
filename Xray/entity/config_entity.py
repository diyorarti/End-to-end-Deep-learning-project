import os
from dataclasses import dataclass
from datetime import datetime
from Xray.constant import *

@dataclass
class DataIngestionConfig:
    FOLDER_NAME: str = FOLDER_NAME
    ZIP_FILE_NAME: str = ZIP_FILE_NAME
    ARTIFACTS_DIR: str = os.path.join(ARTIFACTS_DIR, TIMESTAMP)
    DATA_PATH: str = os.path.join(ARTIFACTS_DIR, "data_ingestion", FOLDER_NAME)
    ZIP_FILE_PATH: str = os.path.join(ARTIFACTS_DIR, ZIP_FILE_NAME)
    TRAIN_DATA_PATH: str = os.path.join(DATA_PATH, "train")
    TEST_DATA_PATH: str = os.path.join(DATA_PATH, "test")
    GD_ZIP_FILE_PATH: str = "https://drive.google.com/uc?id=1lrZNdDcrlHWY6Te2sl-3d5aQ3HaoB1Ke"  # Direct download link for Google Drive
