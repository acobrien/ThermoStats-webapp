from thermostat import Thermostat
from sensor import Sensor
from ordered_set import OrderedSet
from collections import OrderedDict
from datetime import date
import os
from datetime import datetime
import re

class ThermostatManager:

    def __init__(self):
        self.thermostats = OrderedSet()
    
    def addThermostat(self, thermostat):
        return self.thermostats.add(thermostat)
    
    def addSensor(self, thermostat, sensor):
        return thermostat.addSensor(sensor)
    
    def getThermostats(self):
        return self.thermostats
    
    def writeToSave(self, inFileName, saveFileName): 
        try:
            inFile = open(inFileName, "r")
            saveFile = open(saveFileName, "w")
            even = True

            fileSize = os.path.getsize(saveFileName)
            
            if fileSize == 0:
                saveFile.write("East Side,Master Bedroom,Master Bathroom,Office," +
                        "Ty's Bedroom,Luke's Bedroom,Sabry's Bedroom,Living Room\n" +
                        "West Side,Brody's Bedroom,Kitchen,Den,Bar,Living Room,Outside")
            
            line = inFile.readline()
            tokens = line.split("[\t ]+")

            if even:
                saveFile.write(self.epochToDateTime(tokens[1]))

            for i in range(4, tokens.__len__):
                if tokens[2] == "0":
                    if i  != 5 and i != 12 and i != 14 and i != 15:
                        saveFile.write("," + tokens[i])
                        break

                elif tokens[2] == "1":
                    if i  != 5 and i != 11 and i != 12 and i != 14 and i != 15:
                        saveFile.write("," + tokens[i])
                        break
            
            if even:
                even = False
            else:
                saveFile.write("\n")
                even = True
            
            while line:
                line = inFile.readline()
                tokens = line.split("[\t ]+")

                if even:
                    saveFile.write(self.epochToDateTime(tokens[1]))

                for i in range(4, tokens.__len__):
                    if tokens[2] == "0":
                        if i  != 5 and i != 12 and i != 14 and i != 15:
                            saveFile.write("," + tokens[i])
                            break

                    elif tokens[2] == "1":
                        if i  != 5 and i != 11 and i != 12 and i != 14 and i != 15:
                            saveFile.write("," + tokens[i])
                            break
            if even:
                even = False
            else:
                saveFile.write("\n")
                even = True

            saveFile.close()
            inFile.close()
        except FileNotFoundError:
            return False


    def epochToDateTime(self, epochTimestamp):
        dt_object = datetime.utcfromtimestamp(epochTimestamp)
        formatted_time = dt_object.strftime('%M/%d/%y-%H:%m:%s')
        return formatted_time
    
    def loadSave(self, saveFileName):
        isMetaData = True

        with open(saveFileName, 'r') as file:
            for line in file:
                tokens = line.split(",")

                dateTimeRegex = "^\\d{2}/\\d{2}/\\d{4}-\\d{2}:\\d{2}:\\d{2}$"

                if isMetaData and not re.match(dateTimeRegex, tokens[0]):
                    thermostat = Thermostat(tokens[0])
                    self.addThermostat(thermostat)

                    for token in tokens[1:]:
                        sensor = Sensor(token)
                        self.addSensor(thermostat, sensor)
                
                else:
                    temperatureIndex = 1
                    isMetaData = False
                    timestamp = tokens[0]
                    for thermostat in self.thermostats:
                        for sensors in thermostat.getSensors():
                            thermostat.addTemperature(sensor, timestamp, float(tokens[temperatureIndex]))
                            temperatureIndex += 1
                            
    def wipeSave(self, saveFileName):
        open(saveFileName, "w").close

    def __str__(self):
        toString = ""
        for thermostat in self.thermostats:
            toString += thermostat
        return toString