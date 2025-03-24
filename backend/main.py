from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from app.models.ThermostatManager import ThermostatManager

async def startup():
    # if saveFile.csv is not empty, call read_save to read into manager

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

def read_save():
