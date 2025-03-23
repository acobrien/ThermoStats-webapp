from thermostat_manager import ThermostatManager

manager = ThermostatManager()

manager.wipeSave("thermometer-network\\backend\\data\\saveFile.csv")
manager.writeToSave("thermometer-network\\backend\\data\\dump-2025-03-05.txt", "thermometer-network\\backend\\data\\saveFile.csv")
manager.writeToSave("thermometer-network\\backend\\data\\dump-2025-03-06.txt", "thermometer-network\\backend\\data\\saveFile.csv")
manager.writeToSave("thermometer-network\\backend\\data\\dump-2025-03-07.txt", "thermometer-network\\backend\\data\\saveFile.csv")
manager.loadSave("thermometer-network\\backend\\data\\saveFile.csv")
print(manager)