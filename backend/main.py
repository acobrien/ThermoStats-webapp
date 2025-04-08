import os
from email.contentmanager import raw_data_manager

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from app.models.SystemManager import SystemManager

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # backend/
DATA_DIR = os.path.join(BASE_DIR, "data")             # backend/data/
RAW_DIR = os.path.join(DATA_DIR, "raw")               # backend/data/raw
SAVE_PATH = os.path.join(DATA_DIR, "saveFile.csv")    # backend/data/saveFile.csv

async def startup():
    os.makedirs(RAW_DIR, exist_ok = True)
    if not os.path.exists(SAVE_PATH):
        open(SAVE_PATH, 'a').close()

    if os.path.getsize(SAVE_PATH) > 0:
        load_save(SAVE_PATH)
    else:
        write_all_to_save()
        load_save(SAVE_PATH)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup()
    yield
    await shutdown()

app = FastAPI(lifespan = lifespan)
manager = SystemManager()

# Enable CORS
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API endpoints

@app.get("/")
def home():
    return {"message": "Server is running"}

@app.get("/api/thermostat_options")
def get_thermostat_options():
    thermostats = []
    for thermostat in manager.getThermostats():
        thermostats.append(thermostat.getThermostatID())
    return thermostats

@app.get("/api/sensor_options")
def get_sensor_options():
    return ["sensor1", "sensor2", "sensor3"]

@app.get("/api/date_options")
def get_date_options():
    return ["date1", "date2", "date3"]

# Methods

def load_save(save_filename):
    manager.loadSave(save_filename)

def write_to_save(raw_filename, save_path):
    raw_file_path = os.path.join(RAW_DIR, raw_filename)
    manager.writeToSave(raw_file_path, save_path)

def write_all_to_save():
    for filename in os.listdir(RAW_DIR):
        write_to_save(filename, SAVE_PATH)