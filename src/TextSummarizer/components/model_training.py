from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
from TextSummarizer.entity import modelTrainingEntity
import torch
import os


class ModelTrainer:
    def __init__(self,config:modelTrainingEntity):
        self.config=config
        
    def train_model(self):
        device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        tokenizer=AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus=AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt)
        seq2seq_collator=DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        
        dataset_samsum_pt=load_from_disk(self.config.data_dir)
        trainer_args=TrainingArguments(
            output_dir=self.config.root,
            num_train_epochs=self.config.num_train_epochs,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_train_batch_size,
            save_steps=self.config.save_steps,
            logging_steps=self.config.logging_steps,
            eval_steps=self.config.eval_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
            warmup_steps=self.config.warmup_steps,
            weight_decay=self.config.weight_decay
        )
        
        trainer=Trainer(
            model=model_pegasus,
            args=trainer_args,
            data_collator=seq2seq_collator,
            train_dataset=dataset_samsum_pt['test'],
            eval_dataset=dataset_samsum_pt['validation']
        )
        
        trainer.train()
        model_pegasus.save_pretrained(os.path.join(self.config.root,'pegasus-samsum-model'))
        tokenizer.save_pretrained(os.path.join(self.config.root,'pegasus-samsum-tokenizer'))

