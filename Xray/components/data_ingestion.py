import os
import sys
import zipfile
import gdown
from Xray.entity.artifact_entity import DataIngestionArtifact
from Xray.entity.config_entity import DataIngestionConfig
from Xray.exception import XrayException
from Xray.logger import logging


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

    def create_directories(self, paths: list):
        for path in paths:
            if not os.path.exists(path):
                os.makedirs(path)

    def download_file_from_drive(self) -> None:
        try:
            logging.info("Entered the download_file_from_drive method of Data ingestion class")

            # Ensure the directory exists
            self.create_directories([self.data_ingestion_config.ARTIFACTS_DIR, self.data_ingestion_config.DATA_PATH])

            # Download the zip file using gdown
            gdown.download(self.data_ingestion_config.GD_ZIP_FILE_PATH, self.data_ingestion_config.ZIP_FILE_PATH, quiet=False)

            logging.info("Exited the download_file_from_drive method of Data ingestion class")

        except Exception as e:
            raise XrayException(e, sys)

    def unzip_data(self, zip_file_path: str, extract_to: str) -> None:
        try:
            logging.info("Entered the unzip_data method of Data ingestion class")

            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)

            logging.info("Exited the unzip_data method of Data ingestion class")

        except Exception as e:
            raise XrayException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered the initiate_data_ingestion method of Data ingestion class")

        try:
            self.download_file_from_drive()

            # Unzip the downloaded file
            self.unzip_data(self.data_ingestion_config.ZIP_FILE_PATH, self.data_ingestion_config.DATA_PATH)

            data_ingestion_artifact: DataIngestionArtifact = DataIngestionArtifact(
                train_file_path=self.data_ingestion_config.TRAIN_DATA_PATH,
                test_file_path=self.data_ingestion_config.TEST_DATA_PATH,
            )

            logging.info("Exited the initiate_data_ingestion method of Data ingestion class")

            return data_ingestion_artifact

        except Exception as e:
            raise XrayException(e, sys)
