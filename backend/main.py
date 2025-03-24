from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

manager = new ThermostatManager

# Enable CORS for local development
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def writeToSave():
    raw_directory = Path(__file__).parent / "data" / "raw"

    for file_path in raw_directory.iterdir(): # Iterate through all files in data\raw\
        manager.writeToSave(manager, file_path, "data/saveFile.csv")