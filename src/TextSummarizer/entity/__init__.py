from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class dataIngestionEntity:
    root: Path
    URL: str
    file: Path
    unzip_dir: Path
    
    
@dataclass(frozen=True)
class dataCheckingEntity:
    root: Path
    status_file: str
    required_files: list
    
@dataclass(frozen=True)
class dataTransformationEntity:
    root: Path
    data_dir: Path
    tokenizer_name: Path
    
    
@dataclass(frozen=True)
class modelTrainingEntity:
    root: Path
    data_dir: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: int
    gradient_accumulation_steps: int
    

@dataclass(frozen=True)
class modelEvaluationEntity:
    root: Path
    data_dir: Path
    model_path: Path
    tokenizer_path: Path
    metric_file: Path
    