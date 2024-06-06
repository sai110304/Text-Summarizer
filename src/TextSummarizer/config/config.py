from TextSummarizer.constants import *
from TextSummarizer.utils.common import read_yaml,create_directories
from TextSummarizer.entity import dataIngestionEntity, dataCheckingEntity, dataTransformationEntity , modelTrainingEntity , modelEvaluationEntity

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
    
    
    def get_dataChecking_config(self) -> dataCheckingEntity:
        data_config=self.config.data_checking
        
        create_directories([data_config.root])
        
        data_checking_config=dataCheckingEntity(
            root=data_config.root,
            status_file=data_config.status_file,
            required_files=data_config.required_files
        )
        
        return data_checking_config
        
        
    def get_dataTransformation_config(self) -> dataTransformationEntity:
        config=self.config.data_transformation
        
        create_directories([config.root])
        
        data_transformation_config=dataTransformationEntity(
            root=config.root,
            data_dir=config.data_dir,
            tokenizer_name=config.tokenizer_name
        )
        
        return data_transformation_config
    
    
    def get_modelTraining_config(self) -> modelTrainingEntity:
        config=self.config.model_training
        params=self.params.TrainingArguments
        
        create_directories([config.root])
        
        model_training_config=modelTrainingEntity(
            root=config.root,
            data_dir=config.data_dir,
            model_ckpt=config.model_ckpt,
            num_train_epochs=params.num_train_epochs,
            warmup_steps=params.warmup_steps,
            per_device_train_batch_size=params.per_device_train_batch_size,
            weight_decay=params.weight_decay,
            logging_steps=params.logging_steps,
            evaluation_strategy=params.evaluation_strategy,
            eval_steps=params.eval_steps,
            save_steps=params.save_steps,
            gradient_accumulation_steps=params.gradient_accumulation_steps
        )
        
        return model_training_config
    

    def get_modelEvaluation_config(self) -> modelEvaluationEntity:
        config=self.config.model_evaluation
        
        create_directories([config.root])
        
        model_evaluation_config=modelEvaluationEntity(
            root=config.root,
            data_dir=config.data_dir,
            model_path=config.model_path,
            tokenizer_path=config.tokenizer_path,
            metric_file=config.metric_file
        )
        
        return model_evaluation_config