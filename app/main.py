from fastapi import FastAPI, UploadFile, File
from app.processor import process_image
from models.response import build_response
import numpy as np
import cv2

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Glass Fragment API running"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    contents = await file.read()

    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    result = process_image(img)

    return build_response(result)
