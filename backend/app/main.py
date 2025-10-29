# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Support APP", version="0.1.0")

# cors configurations
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def home():
  return {"message":"Backend funcionando con FastAPI"}

@app.get("/health")
def health():
  return {"status":"Ok"}

