from TextSummarizer.constants import *
from TextSummarizer.utils.common import read_yaml,create_directories
from TextSummarizer.entity import dataIngestionEntity

class ConfigManager:
    def __init__(self,config_path=CONFIG_PATH, param_path=PARAM_PATH):
        # print("------------------------------------",config_path)
        # print("------------------------------------",param_path)
        self.config=read_yaml(config_path)
        self.params=read_yaml(param_path)
        create_directories([self.config.artifacts_root])
        
    def get_dataIngestion_config(self) -> dataIngestionEntity:
        data_config=self.config.data_ingestion
        
        create_directories([data_config.root])
        
        data_ingestion_config=dataIngestionEntity(
            root=data_config.root,
            URL=data_config.URL,
            file=data_config.file,
            unzip_dir=data_config.unzip_dir
        )
        
        return data_ingestion_config
        