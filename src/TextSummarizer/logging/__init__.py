import os
import logging
import sys

loggingString = "[%(asctime)s] [%(levelname)s] [%(name)s] [%(filename)s:%(lineno)d] [%(threadName)s] [%(message)s]"
log_dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=loggingString,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("TextSummarizer")