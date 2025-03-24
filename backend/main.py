import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from app.models.ThermostatManager import ThermostatManager

async def startup():
    # if saveFile.csv is not empty, call read_save to read into manager
    # if it is empty, prompt user to read all raw data

async def shutdown():
    # do shutdown process

@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup()  # Runs on startup
    yield
    await shutdown()  # Runs on shutdown

app = FastAPI(lifespan=lifespan)

manager = ThermostatManager()

# Enable CORS for local development
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_save(save_filename):
    manager.loadSave(save_filename)

def write_to_save(raw_filename, save_filename):
    manager.writeToSave(raw_filename, save_filename)

def write_all_to_save(save_file_name):
    raw_directory = os.path.join('data', 'raw')
    for raw_filename in os.listdir(raw_directory):
        write_to_save(raw_filename, save_file_name)