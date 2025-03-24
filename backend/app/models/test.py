from ThermostatManager import ThermostatManager

manager = ThermostatManager()

manager.wipeSave("../../data/saveFile.csv")
manager.writeToSave("../../data/raw/dump-2025-03-05.txt", "../../data/saveFile.csv")
manager.writeToSave("../../data/raw/dump-2025-03-06.txt", "../../data/saveFile.csv")
manager.writeToSave("../../data/raw/dump-2025-03-07.txt", "../../data/saveFile.csv")
manager.loadSave("../../data/saveFile.csv")
print(manager)