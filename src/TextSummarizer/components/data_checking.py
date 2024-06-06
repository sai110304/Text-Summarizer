import os
from TextSummarizer.logging import logger
from TextSummarizer.entity import dataCheckingEntity


class DataChecking:
    def __init__(self, data_config: dataCheckingEntity):
        self.data_config = data_config

    def check_allFiles_exist(self) -> bool:
        try:
            check_status = True
            files=os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))
            for file in files:
                if file not in self.data_config.required_files:
                    check_status = False
                    with open(self.data_config.status_file, "a") as f:
                        #each line in the file will have the file name and the status of the file check
                        f.write(f"Data checking status :{file} {check_status}\n")
                else:
                    check_status = True
                    with open(self.data_config.status_file, "a") as f:
                        f.write(f"Data checking status :{file} {check_status}\n")
                        
            return check_status
        except Exception as e:
            raise e