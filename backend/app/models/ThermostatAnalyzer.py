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
                timesAndTemps = sensor.getDayTimesAndTemps(date)
                tempsTotal = 0
                timesAndTempsLength = len(timesAndTemps)

                minTemp = float('inf') #Sets start index temp as largest
                maxTemp = float('-inf') #Sets start index temp as smallest

                for temp in timesAndTemps:
                    tempTokens = re.split(r" : ", temp) #Strips semicolon, leaving [time, temp]
                    currTemp = float(tempTokens[1])
                    tempsTotal += currTemp
                    
                    #Finds min between currTemp and minTemp and checks if it is currTemp 
                    #Over complicated because floating point nums are extremely annoying
                    if math.isclose(min(minTemp, currTemp), currTemp): 
                        minTemp = currTemp
                    
                    #Finds max between currTemp and maxTemp and checks if it is currTemp
                    if math.isclose(max(maxTemp, currTemp), currTemp):
                        maxTemp = currTemp

                #Calculate average temperature and round each float to four decimal places
                averageTemp = round((tempsTotal / timesAndTempsLength), 4)
                maxTemp = round(maxTemp, 4)
                minTemp = round(minTemp, 4)

                sensorStatisticsSet.update([sensor.getSensorID(), maxTemp, minTemp, averageTemp])

                thermostatStatisticsSet.add(tuple(sensorStatisticsSet))
            except Exception as e:
                print(e)
        return thermostatStatisticsSet