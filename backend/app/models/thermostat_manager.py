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
        self.thermostats.add(thermostat)
    
    def addSensor(self, thermostat, sensor):
        thermostat.addSensor(sensor)
    
    def getThermostats(self):
        return self.thermostats
    
    def writeToSave(self, inFileName, saveFileName): 
        try:
            saveFile = open(saveFileName, "w")
            even = True
            
            with open(inFileName, "r") as file:
                for line in file:
                    tokens = re.split(r"\t+", line)
                    tokensLength = len(tokens)

                    if even:
                        saveFile.write(str(self.epochToDateTime(tokens[1])))

                    for i in range(2, tokensLength):
                        if tokens[2] == "0":
                            if i != 3 and i != 4 and i  != 5 and i != 12 and i != 14 and i != 15:
                                saveFile.write("," + str(tokens[i]))
                                

                        elif tokens[2] == "1":
                            if i != 3 and i != 4 and i != 5 and i != 11 and i != 12 and i != 14 and i != 15:
                                saveFile.write("," + str(tokens[i]))
                                
                    
                if not even:
                    saveFile.write("\n")
                    even = True
                else:
                    even = False
                    
            saveFile.close()       
        except:
            print("There was an reading/writing error")


    def epochToDateTime(self, epochTimestamp):
        dt_object = datetime.utcfromtimestamp(float(epochTimestamp))
        formatted_time = dt_object.strftime('%m/%d/%y-%H:%M:%S')
        return formatted_time
    
    def loadSave(self, saveFileName):
        isMetaData = True
        try:
            with open(saveFileName, 'r') as file:
                for line in file:
                    tokens = re.split(r",", line)
                    tokens.pop() #removes item at last index which is "\n"

                    dateTimeRegex = "^\\d{2}/\\d{2}/\\d{4}-\\d{2}:\\d{2}:\\d{2}$"

                    if isMetaData and not re.match(dateTimeRegex, tokens[0]):
                        thermostat = Thermostat(tokens[1])
                        self.addThermostat(thermostat)

                        for token in thermostat.sensorKeys:
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
        except:
            print("There was a loading error")
                            
    def wipeSave(self, saveFileName):
        try:
            open(saveFileName, "w").close
        except:
            print("There was a wiping error")

    def __str__(self):
        toString = "Thermostat Manager:"
        for thermostat in self.thermostats:
            toString += str(thermostat) + "\n"
        return toString