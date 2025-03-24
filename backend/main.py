import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from app.models.ThermostatManager import ThermostatManager

async def startup():
    # Silently load save file if it exists and is non-empty
    save_file = "saveFile.csv"
    if os.path.exists(save_file) and os.path.getsize(save_file) > 0:
        load_save(save_file)

async def shutdown():
    pass  # Add any shutdown logic if needed

@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup()
    yield
    await shutdown()

app = FastAPI(lifespan=lifespan)
manager = ThermostatManager()

# Serve raw files for frontend access
app.mount("/data", StaticFiles(directory="data/raw"), name="raw_data")

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

def write_to_save(raw_filename, save_filename):
    manager.writeToSave(raw_filename, save_filename)

def write_all_to_save(save_file_name):
    raw_dir = os.path.join('data', 'raw')
    for filename in os.listdir(raw_dir):
        write_to_save(filename, save_file_name)

@app.post("/api/load-all-raw")
async def handle_load_all_raw():
    """Endpoint to process all raw files into save file"""
    save_file = "saveFile.csv"
    write_all_to_save(save_file)
    load_save(save_file)  # Refresh manager with new data
    return {"message": "All raw data processed successfully"}

@app.post("/api/process-file")
async def handle_process_file(data: dict):
    """Endpoint to process a single file"""
    if not (filename := data.get("filename")):
        raise HTTPException(400, "Filename required")

    save_file = "saveFile.csv"
    try:
        write_to_save(filename, save_file)
        load_save(save_file)  # Refresh manager
        return {"message": f"Processed {filename} successfully"}
    except Exception as e:
        raise HTTPException(500, str(e))