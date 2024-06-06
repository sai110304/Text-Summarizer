from TextSummarizer.logging import logger
from TextSummarizer.pipeline.N_01_data_ingestion import DataIngestionPipeline
from TextSummarizer.pipeline.N_02_data_checking import DataCheckingPipeline
from TextSummarizer.pipeline.N_03_data_transformation import DataTransformationPipeline
# logger.info("TextSummarizer is running...") 


CURRENT_STAGE = "Data Ingestion"
logger.info(f"{CURRENT_STAGE} Started")
data_ingestion_pipeline = DataIngestionPipeline()
data_ingestion_pipeline.run()
logger.info(f"{CURRENT_STAGE} Completed")


CURRENT_STAGE = "Data Checking"
logger.info(f"{CURRENT_STAGE} Started")
data_checking_pipeline = DataCheckingPipeline()
data_checking_pipeline.run()
logger.info(f"{CURRENT_STAGE} Completed")


CURRENT_STAGE = "Data Transformation"
logger.info(f"{CURRENT_STAGE} Started")
data_transformation_pipeline = DataTransformationPipeline()
data_transformation_pipeline.run()
logger.info(f"{CURRENT_STAGE} Completed")

