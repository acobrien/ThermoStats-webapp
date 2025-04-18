from Thermostat import Thermostat
from Sensor import Sensor
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
        sensors = self.thermostat.getSensors()
        try:
            timesAndTempProbe = sensors[0].getDayTimesAndTemps(date)

            for sensor in sensors:
                #-- print(str(sensor) + f" Average Temperature On {date}: ") --NOTE: OLD CODE
                sensorStatisticsSet = OrderedSet() #Set of statistics for sensor
                
                try:
                    timesAndTemps = sensor.getDayTimesAndTemps(date)
                    tempsTotal = 0
                    timesAndTempsLength = len(timesAndTemps)

                    minTemp = [0, float('inf')] #Sets start index temp as largest
                    maxTemp = [0, float('-inf')] #Sets start index temp as smallest

                    for entry in timesAndTemps:
                        entryTokens = re.split(r" : ", entry) #Strips semicolon, leaving [time, temp]
                        #print(f"entryTokens = {entryTokens}")
                        currTemp = float(entryTokens[1])
                        currTime = entryTokens[0]
                        tempsTotal += currTemp
                        
                        #Finds min between currTemp and minTemp and checks if it is currTemp @ TIME
                        #Over complicated because floating point nums are extremely annoying
                        if math.isclose(min(minTemp[1], currTemp), currTemp): 
                            minTemp = [currTime, currTemp]
                        
                        #Finds max between currTemp and maxTemp and checks if it is currTemp @ TIME
                        if math.isclose(max(maxTemp[1], currTemp), currTemp):
                            maxTemp = [currTime, currTemp]

                    #Calculate average temperature and round each float to four decimal places 
                    averageTemp = round((tempsTotal / timesAndTempsLength), 4)
                    print(f"entryTokens = {averageTemp}")
                    maxTemp[1] = round(maxTemp[1], 4)
                    print(f"entryTokens = {maxTemp}")
                    minTemp[1] = round(minTemp[1], 4)
                    print(f"entryTokens = {minTemp}")

                    sensorStatisticsSet.update([sensor.getSensorID(), maxTemp[0], maxTemp[1], minTemp[0], minTemp[1], averageTemp])

                    thermostatStatisticsSet.add(tuple(sensorStatisticsSet))
                except Exception as e:
                    print(e)
            return thermostatStatisticsSet    
        except KeyError as e:
            return e
        