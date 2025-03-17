from thermostat import Thermostat
from sensor import Sensor
from ordered_set import OrderedSet
from collections import OrderedDict
from datetime import date

class ThermostatManager:

    def __init__(self):
        self.thermostats = OrderedSet()
    
    def addThermostat(self, thermostat):
        return self.thermostats.add(thermostat)
    
    def addSensor(self, thermostat, sensor):
        return thermostat.addSensor(sensor)
    
    def getThermostats(self):
        return self.thermostats
    
    def writeToSave(inFileName, saveFileName): 
        progress = "currently working on this"
        print(progress)

    def epochToDateTime(epochTimestamp):
        progress = "currently working on this"
        print(progress)

    def loadSave(saveFileName):
        progress = "currently working on this"
        print(progress)

    def wipeSave(saveFileName):
        progress = "currently working on this"
        print(progress)

    def __str__(self):
        toString = ""
        for thermostat in self.thermostats:
            toString += thermostat
        return toString