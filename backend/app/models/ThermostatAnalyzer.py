from .Thermostat import Thermostat
from .Sensor import Sensor
from ordered_set import OrderedSet
import math
import re

class ThermostatAnalyzer:

    def __init__(self, thermostat):
        self.thermostat = thermostat
        self.thermostatAnalyzerID = self.thermostat.getThermostatID() + " Analyzer"

    def getThermostatAnalyzerID(self):
        return self.thermostatAnalyzerID
        
    def analysisGetNumericalStats(self, date):
        #Returns a set of [SensorID, MaxTemp, MinTemp, AverageTemp] for each sensor in thermostat
        #-- print(str(self.thermostat.getThermostatID()) + ":") --NOTE: OLD CODE
        thermostatStatisticsSet = OrderedSet() #Set of sets of statistics for each sensor in thermostat
        for sensor in self.thermostat.getSensors():
            #-- print(str(sensor) + f" Average Temperature On {date}: ") --NOTE: OLD CODE
            sensorStatisticsSet = OrderedSet() #Set of statistics for sensor
            try:
                timesAndData = sensor.getDayTimesAndData(date)
                tempsTotal = 0
                timesAndDataLength = len(timesAndData)

                minTemp = float('inf') #Sets start index temp as largest
                maxTemp = float('-inf') #Sets start index temp as smallest

                for entry in timesAndData:
                    entryTokens = re.split(r"\s*:\s*", entry) #Strips semicolon, leaving [time, temp]
                    currTime = entryTokens[0]
                    currActivity = entryTokens[1]
                    currTemp = float(entryTokens[2])
                    tempsTotal += currTemp
                    energyTotal = 0
                    
                    #Finds min between currTemp and minTemp and checks if it is currTemp @ TIME
                    #Over complicated because floating point nums are extremely annoying
                    if math.isclose(min(minTemp, currTemp), currTemp): 
                        minTemp = [currTime, currTemp]
                    
                    #Finds max between currTemp and maxTemp and checks if it is currTemp @ TIME
                    if math.isclose(max(maxTemp, currTemp), currTemp):
                        maxTemp = [currTime, currTemp]

                #Calculate average temperature and round each float to four decimal places 
                averageTemp = round((tempsTotal / timesAndDataLength), 4)
                maxTemp[1] = round(maxTemp[1], 4)
                minTemp[1] = round(minTemp[1], 4)

                sensorStatisticsSet.update([sensor.getSensorID(), maxTemp, minTemp, averageTemp])

                thermostatStatisticsSet.add(tuple(sensorStatisticsSet))
            except Exception as e:
                print(e)
        return thermostatStatisticsSet