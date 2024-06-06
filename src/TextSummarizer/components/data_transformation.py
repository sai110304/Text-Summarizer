import os
from TextSummarizer.logging import logger
from transformers import AutoTokenizer
from TextSummarizer.entity import dataTransformationEntity
from datasets import load_from_disk

class DataTransformation:
    def __init__(self, data_config: dataTransformationEntity):
        self.data_config = data_config
        self.tokenizer=AutoTokenizer.from_pretrained(self.data_config.tokenizer_name)

    def tokenize_data(self, batch):
        input_encodings = self.tokenizer(batch["dialogue"], max_length=1024,truncation=True)
        
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(batch["summary"], max_length=128,truncation=True)
        
        return {
            "input_ids": input_encodings.input_ids,
            "attention_mask": input_encodings.attention_mask,
            "labels": target_encodings.input_ids
        }
        
    def convert(self):
        dataset_samsum=load_from_disk(self.data_config.data_dir)
        dataset_samsum_pt=dataset_samsum.map(self.tokenize_data,batched=True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.data_config.root,"samsum_dataset"))
        
        