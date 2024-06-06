from TextSummarizer.config.config import ConfigManager
from TextSummarizer.logging import logger
from TextSummarizer.components.model_training import ModelTrainer

class ModelTrainingPipeline:
    def __init__(self):
        self.config = ConfigManager()
        self.model_training_config = self.config.get_modelTraining_config()
        self.model_trainer = ModelTrainer(self.model_training_config)

    def run(self):
        logger.info("Model Training Started")
        self.model_trainer.train_model()
        logger.info("Model Training Completed")