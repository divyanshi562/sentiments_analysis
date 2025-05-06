from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Request body structure
class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(input: TextInput):
    result = sentiment_pipeline(input.text)
    return {"label": result[0]["label"], "score": result[0]["score"]}
