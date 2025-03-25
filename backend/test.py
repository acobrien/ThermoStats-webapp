import os
from app.models.ThermostatManager import ThermostatManager

# Absolute path configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # backend/
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw")
SAVE_PATH = os.path.join(DATA_DIR, "saveFile.csv")  # backend/data/saveFile.csv

manager = ThermostatManager()

print("Base:", BASE_DIR)
print("Data:", DATA_DIR)
print("Raw:", RAW_DIR)

def write_to_save(raw_filename, save_path):
    raw_file_path = os.path.join(RAW_DIR, raw_filename)
    print("Raw File:", raw_file_path)
    manager.writeToSave(raw_file_path, save_path)

input_filename = "dump-2025-03-05.txt"

write_to_save(input_filename, SAVE_PATH)

print(manager)