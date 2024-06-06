from TextSummarizer.config.config import ConfigManager
from TextSummarizer.logging import logger
from transformers import AutoTokenizer
from transformers import pipeline


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigManager().get_modelEvaluation_config()
        
    def predict(self,text):
        tokenizer=AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "max_length": 35, "num_beams": 8}
        
        pipeline_summarization = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer)
        
        output=pipeline_summarization(text, **gen_kwargs)[0]['summary_text']
        # print("Summary",output)
        return output
        
        