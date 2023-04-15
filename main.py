from transformers import ViTFeatureExtractor, ViTForImageClassification
from fastapi import FastAPI
from PIL import Image
from pydantic import BaseModel
import requests


class Item(BaseModel):
    url: str


# model predicts one of the 1000 ImageNet classes
def predict_of_cat(url: str) -> str:
    image = Image.open(requests.get(url, stream=True).raw)

    inputs = feature_extractor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()

    return model.config.id2label[predicted_class_idx]


app = FastAPI()
feature_extractor = ViTFeatureExtractor.from_pretrained(
    'google/vit-base-patch16-224')
model = ViTForImageClassification.from_pretrained(
    'google/vit-base-patch16-224')


@app.get("/")
def root():
    return {"message": "This is neural network's main page"}


@app.get("/demo/")
def demo():
    url = "https://www.purina.ru/sites/default/files/2021-10/britanskaya-3.jpg"
    return predict_of_cat(url)


@app.post("/predict/")
def predict(item: Item):
    return predict_of_cat(item.url)
