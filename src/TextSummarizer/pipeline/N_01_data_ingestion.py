from TextSummarizer.config.config import ConfigManager
from TextSummarizer.logging import logger
from TextSummarizer.components.data_ingestion import DataIngestion


class DataIngestionPipeline:
    def __init__(self):
        self.config = ConfigManager()
        self.data_config = self.config.get_dataIngestion_config()
        self.data_ingestion = DataIngestion(self.data_config)

    def run(self):
        logger.info("Data Ingestion Started")
        self.data_ingestion.download_data()
        self.data_ingestion.unzip_data()
        logger.info("Data Ingestion Completed")