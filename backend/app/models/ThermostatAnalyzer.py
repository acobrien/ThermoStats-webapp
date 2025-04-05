from .Thermostat import Thermostat
from .Sensor import Sensor
import re

class ThermostatAnalyzer:

    def __init__(self, thermostat):
        self.thermostat = thermostat
        self.thermostatAnalyzerID = self.thermostat.getThermostatID() + " Analyzer"

    def getThermostatAnalyzerID(self):
        return self.thermostatAnalyzerID
        
    def analysisExamplePrintAverageTemperaturePerSensorOnDay(self, date):
        print(str(self.thermostat.getThermostatID()) + ":")
        for sensor in self.thermostat.getSensors():
            print(str(sensor) + f" Average Temperature On {date}: ")
            try:
                timesAndTemps = sensor.getDayTimesAndTemps(date)
                tempsTotal = 0
                timesAndTempsLength = len(timesAndTemps)

                for temp in timesAndTemps:
                    timesAndTempsTokens = re.split(r" : ", temp)
                    tempsTotal += float(timesAndTempsTokens[1])

                print(str(tempsTotal / timesAndTempsLength))
            except Exception as e:
                print(e)