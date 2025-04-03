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
    # Create required directories
    os.makedirs(RAW_DIR, exist_ok = True)

    # Create save file if missing
    if not os.path.exists(SAVE_PATH):
        open(SAVE_PATH, 'a').close()

    # Load save if it has data
    if os.path.getsize(SAVE_PATH) > 0:
        load_save(SAVE_PATH)

async def shutdown():
    pass

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

def load_save(save_filename):
    manager.loadSave(save_filename)

def write_to_save(raw_filename, save_path):
    raw_file_path = os.path.join(RAW_DIR, raw_filename)
    manager.writeToSave(raw_file_path, save_path)

def write_all_to_save():
    for filename in os.listdir(RAW_DIR):
        write_to_save(filename, SAVE_PATH)

# API endpoints
@app.post("/api/load-all-raw")
async def load_all_raw():
    write_all_to_save()
    load_save(SAVE_PATH)
    return {"message": "All raw data processed and loaded."}

@app.post("/api/process-file")
async def process_file(data: dict):
    raw_filename = data.get("raw_filename")
    try:
        write_to_save(raw_filename, SAVE_PATH)  # Explicit save path
        load_save(SAVE_PATH)
        return {"message": f"File {raw_filename} processed successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))