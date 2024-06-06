import os
import urllib.request as request
from pathlib import Path
import zipfile
from TextSummarizer.logging import logger
from TextSummarizer.utils.common import get_size
from TextSummarizer.entity import dataIngestionEntity

class DataIngestion:
    def __init__(self,data_config:dataIngestionEntity):
        self.data_config=data_config
        
    def download_data(self):
        if not os.path.exists(self.data_config.file):
            filename, headers = request.urlretrieve(self.data_config.URL, self.data_config.file)
            logger.info(f"Downloaded {filename} Download with following headers : {headers}")
        else:
            logger.info(f"File already exists with size {get_size(Path(self.data_config.file))}")
            
    def unzip_data(self):
        unzip_dir=self.data_config.unzip_dir
        os.makedirs(unzip_dir,exist_ok=True)
        with zipfile.ZipFile(self.data_config.file, 'r') as zip_ref:
            zip_ref.extractall(unzip_dir)
            logger.info(f"Unzipped {self.data_config.file} to {unzip_dir}")
        