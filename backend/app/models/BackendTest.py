from .SystemManager import SystemManager


manager = SystemManager()

manager.wipeSave("../../data/saveFile.csv")
manager.writeToSave("data/raw/dump-2025-03-05.txt", "../../data/saveFile.csv")
#manager.writeToSave("../../data/raw/dump-2025-03-06.txt", "../../data/saveFile.csv") --NOTE: NOT IN USE
#manager.writeToSave("../../data/raw/dump-2025-03-07.txt", "../../data/saveFile.csv") --NOTE: NOT IN USE
manager.loadSave("../../data/saveFile.csv")
print(str(manager.callAnalysisGetNumericalStats("East Side Analyzer", "03/05/2025")))