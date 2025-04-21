import os
from email.contentmanager import raw_data_manager

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from app.models.SystemManager import SystemManager

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from skgarden import RandomForestQuantileRegressor
from scipy.interpolate import CubicSpline

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
def get_sensor_options(thermostat_id: str):
    thermostat = manager.getThermostatByID(thermostat_id)
    if thermostat is None:
        return []

    sensors = []
    for sensor in thermostat.getSensors():
        sensors.append(sensor.getSensorID())
    return sensors

@app.get("/api/date_options")
def get_date_options(thermostat_id: str):
    thermostat = manager.getThermostatByID(thermostat_id)
    if thermostat is None:
        return []

    return thermostat.getDates()

@app.get("/api/sensor_time_list")
def get_time_list(thermostat_id: str, sensor_id: str, date: str):
    thermostat = manager.getThermostatByID(thermostat_id)
    if thermostat is None:
        return []

    sensor = thermostat.getSensorByID(sensor_id)
    if sensor is None:
        return []

    return sensor.getTimeList(date)

@app.get("/api/sensor_temp_list")
def get_temp_list(thermostat_id: str, sensor_id: str, date: str):
    thermostat = manager.getThermostatByID(thermostat_id)
    if thermostat is None:
        return []

    sensor = thermostat.getSensorByID(sensor_id)
    if sensor is None:
        return []

    return sensor.getTempList(date)

@app.get("/api/thermostat_time_list")
def get_thermostat_time_list(thermostat_id: str, date: str):
    thermostat = manager.getThermostatByID(thermostat_id)
    if thermostat is None:
        return []

    return thermostat.getTimeList(date)

@app.get("/api/thermostat_activity_list")
def get_thermostat_activity_list(thermostat_id: str, date: str):
    thermostat = manager.getThermostatByID(thermostat_id)
    if thermostat is None:
        return []

    return thermostat.getActivityList(date)

# Want a graph with plotted points of (avg temp, energy cost)
# X-axis: daily avg temp, Y-axis: daily energy cost

@app.get("/api/get_energy_function")
# def get_energy_function(thermostat_id: str, date: str):
#     # === 1. Load your data ===
#     # Replace this with your actual DataFrame
#     # Assume df has columns: ['avg_temp', 'energy_cost']
#     df = pd.read_csv("your_data.csv")  # or however you load your data
#     X = df[['avg_temp']].values
#     y = df['energy_cost'].values
#
#     # === 2. Train QRF model ===
#     qrf = RandomForestQuantileRegressor(random_state=42, n_estimators=100)
#     qrf.fit(X, y)
#
#     # === 3. Predict on a fine grid ===
#     temps_grid = np.linspace(X.min(), X.max(), 500).reshape(-1, 1)
#     median_preds = qrf.predict(temps_grid, quantile=50)
#
#     # === 4. Create spline interpolator ===
#     spline_fn = CubicSpline(temps_grid.flatten(), median_preds)
#
#     # === 5. Use the interpolator ===
#     # Example: Predict energy cost at 72.5°F
#     predicted_cost = spline_fn(72.5)
#     print(f"Predicted cost at 72.5°F: {predicted_cost:.2f}")
#
#     # === 6. Optionally define a function to reuse ===
#     def predict_energy_cost(temp):
#         """
#         Predict energy cost using QRF + spline interpolation.
#         """
#         return spline_fn(temp)

# Methods

def load_save(save_filename):
    manager.loadSave(save_filename)

def write_to_save(raw_filename, save_path):
    raw_file_path = os.path.join(RAW_DIR, raw_filename)
    manager.writeToSave(raw_file_path, save_path)

def write_all_to_save():
    for filename in os.listdir(RAW_DIR):
        write_to_save(filename, SAVE_PATH)