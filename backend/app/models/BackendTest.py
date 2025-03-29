from SystemManager import SystemManager


manager = SystemManager()

manager.wipeSave("../../data/saveFile.csv")
manager.writeToSave("backend/data/raw/dump-2025-03-05.txt", "../../data/saveFile.csv")
#manager.writeToSave("../../data/raw/dump-2025-03-06.txt", "../../data/saveFile.csv")
#manager.writeToSave("../../data/raw/dump-2025-03-07.txt", "../../data/saveFile.csv")
manager.loadSave("../../data/saveFile.csv")
manager.callAnalysisExamplePrintAverageTemperaturePerSensorPerDay("East Side Analizer", "03/05/2025")