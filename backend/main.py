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

async def shutdown():
    return

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
# QRF + Spline should smooth out noise and provide a smooth function for prediction/graphing

@app.get("/api/get_average_temperatures")
def get_average_temperatures():
    return manager.getAvgOutsideTemperatures()

@app.get("/api/get_energy_costs")
def get_energy_costs():
    return manager.getEnergyCosts()

@app.get("/api/get_interpolated_temperatures")
def get_interpolated_temps():
    temps = np.array(manager.getAvgOutsideTemperatures())

    firstTemp = np.min(temps)
    lastTemp = np.max(temps)

    delta = lastTemp / firstTemp
    h = delta / 100 # arbitrary n value, can change

    interpolatedTemps = []
    while firstTemp < lastTemp:
        interpolatedTemps.append(firstTemp)
        firstTemp += h

    return interpolatedTemps

@app.get("/api/get_interpolated_costs")
def get_interpolated_costs:
    temps = np.array(manager.getAvgOutsideTemperatures())
    firstTemp = np.min(temps)
    lastTemp = np.max(temps)

    delta = lastTemp / firstTemp
    h = delta / 100 # arbitrary n value, can change

    spline_fn = get_spline_fn(manager.getAvgOutsideTemperatures(), manager.getEnergyCosts())

    interpolatedCosts = []
    while firstTemp < lastTemp:
        interpolatedTemps.append(spline_fn(firstTemp))
        firstTemp += h

    return interpolatedCosts

@app.get("/api/get_energy_prediction")
def get_energy_prediction(thermostat_id: str, date: str, temperature: float):
    temperatures = manager.getAvgOutsideTemperatures()
    energy_costs = manager.getEnergyCosts()
    spline_fn = get_spline_fn(temperatures, energy_costs)
    return spline_fn(temperature)

# Methods

def load_save(save_filename):
    manager.loadSave(save_filename)

def write_to_save(raw_filename, save_path):
    raw_file_path = os.path.join(RAW_DIR, raw_filename)
    manager.writeToSave(raw_file_path, save_path)

def write_all_to_save():
    for filename in os.listdir(RAW_DIR):
        write_to_save(filename, SAVE_PATH)

def get_spline_fn(X, y):
    # Train QRF model
    qrf = RandomForestQuantileRegressor(random_state=42, n_estimators=100)
    qrf.fit(X, y)

    # Predict on a fine grid
    temps_grid = np.linspace(X.min(), X.max(), 500).reshape(-1, 1)
    median_preds = qrf.predict(temps_grid, quantile=50)

    # Create spline interpolator
    spline_fn = CubicSpline(temps_grid.flatten(), median_preds)
    return spline_fn