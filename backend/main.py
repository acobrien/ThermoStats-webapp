from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Enable CORS for local development
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve files directly from /data
app.mount("/data", StaticFiles(directory="data"), name="data")