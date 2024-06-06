from fastapi import FastAPI
import uvicorn
import os
import sys
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.responses import Response

from TextSummarizer.pipeline.prediction import PredictionPipeline

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/",tags=["Authentication"])
async def read_root():
    return RedirectResponse(url="/docs")


@app.post("/predict",tags=["Prediction"])
async def predict(text:str):
    pipeline=PredictionPipeline()
    summary=pipeline.predict(text)
    return summary


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)