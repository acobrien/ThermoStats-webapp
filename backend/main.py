from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

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

def add_data (filename):
    