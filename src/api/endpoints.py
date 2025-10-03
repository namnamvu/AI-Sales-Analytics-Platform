from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO
from ..core.analyzer_engine import AnalyzerEngine

app = FastAPI(title="BI Auto Analyzer (MVP)")
engine = AnalyzerEngine()

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(BytesIO(contents))
        result = engine.analyze(df)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
