from Thermostat import Thermostat
from Sensor import Sensor
from ordered_set import OrderedSet
import re, os
from time import strftime, localtime

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
            saveFile = open(saveFileName, "a")
            even = True
            
            fileSize = os.path.getsize(saveFileName)
             
            if fileSize == 0:
                saveFile.write("East Side,Master Bedroom,Master Bathroom,Office," +
                        "Ty's Bedroom,Luke's Bedroom,Sabry's Bedroom,Living Room\n" +
                        "West Side,Brody's Bedroom,Kitchen,Den,Bar,Living Room,Outside\n")
                
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
            print("There was a reading/writing error")


    def epochToDateTime(self, epochTimestamp):
        formatted_time = strftime('%m/%d/%Y-%H:%M:%S', localtime(float(epochTimestamp)))
        return formatted_time
    
    def loadSave(self, saveFileName):
        isMetaData = True
        try:
            with open(saveFileName, 'r') as file:
                for line in file:
                    cleanedLine = line.rstrip().strip(",")
                    tokens = re.split(r",", cleanedLine)

                    dateTimeRegex = "^\\d{2}/\\d{2}/\\d{4}-\\d{2}:\\d{2}:\\d{2}$"

                    if isMetaData and not re.match(dateTimeRegex, tokens[0]):
                        thermostat = Thermostat(tokens[0])
                        self.addThermostat(thermostat)

                        for token in tokens[1:]:
                            sensor = Sensor(token)
                            self.addSensor(thermostat, sensor)
                    
                    else:
                        isMetaData = False
                        timestamp = tokens[0]
                        for thermostat in self.thermostats:
                            if thermostat.getThermostatIDNum() == tokens[1]:
                                temperatureIndex = 2
                                for sensor in thermostat.getSensors():
                                    thermostat.addTemperature(sensor, timestamp, float(tokens[temperatureIndex]))
                                    temperatureIndex += 1

        except Exception as e:
            print("There was a loading error" + str(e))
                            
    def wipeSave(self, saveFileName):
        try:
            open(saveFileName, "w").close
        except:
            print("There was a wiping error")

    def __str__(self):
        toString = "Thermostat Manager:\n"
        for thermostat in self.thermostats:
            toString += str(thermostat) + "\n"
        return toString