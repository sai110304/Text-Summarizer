from TextSummarizer.config.config import ConfigManager
from TextSummarizer.logging import logger
from TextSummarizer.components.data_checking import DataChecking

class DataCheckingPipeline:
    def __init__(self):
        self.config = ConfigManager()
        self.data_config = self.config.get_dataChecking_config()
        self.data_checking = DataChecking(self.data_config)

    def run(self):
        logger.info("Data Checking Started")
        self.data_checking.check_allFiles_exist()
        logger.info("Data Checking Completed")