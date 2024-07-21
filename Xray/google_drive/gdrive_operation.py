from pydrive.drive import GoogleDrive
import os
import sys

class XRayException(Exception):
    def __init__(self, message, system):
        super().__init__(message)
        self.system = system

class GoogleDriveOperation:
    def __init__(self):
        self.drive = GoogleDrive(self.gauth)

    def sync_folder_from_drive(self, folder_id: str, local_folder: str) -> None:
        try:
            file_list = self.drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
            for file in file_list:
                file_path = os.path.join(local_folder, file['title'])
                file.GetContentFile(file_path)
        except Exception as e:
            raise XRayException(e, sys)

    def sync_folder_to_drive(self, local_folder: str, folder_id: str) -> None:
        try:
            for filename in os.listdir(local_folder):
                file_path = os.path.join(local_folder, filename)
                if os.path.isfile(file_path):
                    file_drive = self.drive.CreateFile({'title': filename, 'parents': [{'id': folder_id}]})
                    file_drive.SetContentFile(file_path)
                    file_drive.Upload()
        except Exception as e:
            raise XRayException(e, sys)

