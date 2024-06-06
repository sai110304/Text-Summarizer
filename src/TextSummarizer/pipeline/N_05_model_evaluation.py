from TextSummarizer.config.config import ConfigManager
from TextSummarizer.logging import logger
from TextSummarizer.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def __init__(self):
        self.config = ConfigManager()
        self.model_evaluation_config = self.config.get_modelEvaluation_config()
        self.model_evaluator = ModelEvaluation(self.model_evaluation_config)

    def run(self):
        logger.info("Model Evaluation Started")
        self.model_evaluator.evaluate()
        logger.info("Model Evaluation Completed")