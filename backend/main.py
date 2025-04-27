import os
from email.contentmanager import raw_data_manager

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from app.models.SystemManager import SystemManager

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from scipy.interpolate import CubicSpline
from scipy.interpolate import make_smoothing_spline

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

    return np.linspace(firstTemp, lastTemp, num=1000).tolist()

@app.get("/api/get_interpolated_costs")
def get_interpolated_costs():
    temps = np.array(manager.getAvgOutsideTemperatures())
    firstTemp = np.min(temps)
    lastTemp = np.max(temps)

    delta = lastTemp - firstTemp
    h = delta / 1000 # arbitrary n value, can change

    spline_fn = get_spline_fn(manager.getAvgOutsideTemperatures(), manager.getEnergyCosts())

    interpolatedCosts = []
    while firstTemp < lastTemp:
        cost = spline_fn(firstTemp)
        interpolatedCosts.append(float(cost)) # convert np scalar to Python float
        firstTemp += h

    return interpolatedCosts

@app.get("/api/get_energy_prediction")
def get_energy_prediction(temperature: float):
    temperatures = manager.getAvgOutsideTemperatures()
    energy_costs = manager.getEnergyCosts()
    spline_fn = get_spline_fn(temperatures, energy_costs)
    return spline_fn(temperature)

@app.get("/api/get_statistics")
def get_statistics(thermostat_id: str, date: str):
    analyzer_id = thermostat_id + " Analyzer"
    return manager.callAnalysisGetNumericalStats(analyzer_id, date)

# Internal Methods

def load_save(save_filename):
    manager.loadSave(save_filename)

def write_to_save(raw_filename, save_path):
    raw_file_path = os.path.join(RAW_DIR, raw_filename)
    manager.writeToSave(raw_file_path, save_path)

def write_all_to_save():
    for filename in os.listdir(RAW_DIR):
        write_to_save(filename, SAVE_PATH)


def get_spline_fn(X, y):
    df = pd.DataFrame({'X': X, 'y': y})
    df_avg = df.groupby('X', as_index=False).mean()

    X_avg = df_avg['X'].to_numpy()
    y_avg = df_avg['y'].to_numpy()

    spline_fn = make_smoothing_spline(X_avg, y_avg)
    return spline_fn