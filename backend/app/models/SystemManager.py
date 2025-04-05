from .Thermostat import Thermostat
from .Sensor import Sensor
from .ThermostatAnalyzer import ThermostatAnalyzer
from ordered_set import OrderedSet
import re, os
from time import strftime, localtime

class SystemManager:

    def __init__(self):
        self.thermostats = OrderedSet()
        self.thermostatAnalyzers = OrderedSet()
    
    def addThermostat(self, thermostat):
        self.thermostats.add(thermostat)
        thermostatAnalyzer = ThermostatAnalyzer(thermostat)
        self.thermostatAnalyzers.add(thermostatAnalyzer)
    
    def addSensor(self, thermostat, sensor):
        thermostat.addSensor(sensor)
    
    def getThermostats(self):
        return self.thermostats

    def writeToSave(self, inFileName, saveFileName):
        try:
            os.makedirs(os.path.dirname(saveFileName), exist_ok=True)

            with open(saveFileName, "a+") as saveFile:  # Use a+ mode to read/write
                saveFile.seek(0)  # Move to start to check file size
                even = True

                # Check if file is empty
                if os.fstat(saveFile.fileno()).st_size == 0:
                    saveFile.write("East Side,Master Bedroom,Master Bathroom,Office," +
                                   "Ty's Bedroom,Luke's Bedroom,Sabry's Bedroom,Living Room\n" +
                                   "West Side,Brody's Bedroom,Kitchen,Den,Bar,Living Room,Outside\n")

                # Now process the input file
                with open(inFileName, "r") as inputFile:
                    for line in inputFile:
                        tokens = re.split(r"\t+", line)
                        tokensLength = len(tokens)

                        if even:
                            saveFile.write(str(self.epochToDateTime(tokens[1])))

                        for i in range(2, tokensLength):
                            if tokens[2] == "0":
                                if i not in {3,4,5,12,14,15}:
                                    saveFile.write("," + str(tokens[i]))
                            elif tokens[2] == "1":
                                if i not in {3,4,5,11,12,14,15}:
                                    saveFile.write("," + str(tokens[i]))

                        # Handle line endings
                        # if not even:
                        #     saveFile.write("\n")
                        #     even = True
                        # else:
                        #     even = False

        except Exception as e:
            print(f"Error in writeToSave: {str(e)}")


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

    def callAnalysisExamplePrintAverageTemperaturePerSensorPerDay(self, thermostatAnalyzerID, date):
        for thermostatAnalyzer in self.thermostatAnalyzers:
            if thermostatAnalyzerID == thermostatAnalyzer.getThermostatAnalyzerID():
                return thermostatAnalyzer.analysisExamplePrintAverageTemperaturePerSensorOnDay(date)
        return "Unable to locate Thermostat Analyzer"

    def __str__(self):
        toString = "Thermostat Manager:\n"
        for thermostat in self.thermostats:
            toString += str(thermostat) + "\n"
        return toString