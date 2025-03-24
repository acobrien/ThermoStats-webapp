from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.models.ThermostatManager import ThermostatManager

app = FastAPI()

manager = ThermostatManager()

# Enable CORS for local development
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def writeToSave(inFileName, saveFileName):
    manager.writeToSave(inFileName, saveFileName)