from TextSummarizer.config.config import ConfigManager
from TextSummarizer.logging import logger
from TextSummarizer.components.data_transformation import DataTransformation

class DataTransformationPipeline:
    def __init__(self):
        self.config = ConfigManager()
        self.data_transform_config = self.config.get_dataTransformation_config()
        self.data_transformation = DataTransformation(self.data_transform_config)

    def run(self):
        logger.info("Data Transformation Started")
        self.data_transformation.convert()
        logger.info("Data Transformation Completed")