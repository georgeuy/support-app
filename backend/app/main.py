# backend/app/main.py

from fastapi import FastAPI

app = FastAPI(title="Support APP", version="0.1.0")

@app.get("/")
def home():
  return {"message":"Backend funcionando con FastAPI"}

@app.get("/health")
def health():
  return {"status":"Ok"}

