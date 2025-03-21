from collections import OrderedDict
from ordered_set import OrderedSet

class Sensor:
    
    def __init__(self, sensorID):
        self.sensorID = sensorID
        self.dateMap = OrderedDict
    
    def addTemperature(self, timestamp, temperature):
        date = timestamp[0, 10]
        time = timestamp[11:]
        if date in self.dateMap:
            self.dateMap[date] = {time: temperature}
            return
        self.dateMap[date] = {}

    #POTENTIAL BUG: might not be in order, might need to be sorted before returning
    def getTimesAndTemps(self, dayMap):
        timesAndTemps = OrderedSet()

        for time in dayMap:
            combo = time + " : " + dayMap[time]
            timesAndTemps.add(combo)

        return timesAndTemps

    #testing method
    def displayTemperatures(self):
        for date in self.dateMap.keys:
            print(self.getTimesAndTemps(self.dateMap.get(date)))

    def getDates(self):
        return self.dateMap.keys
    
    def getDayMap(self, date):
        return self.dateMap.get(date)
    
    def __str__(self):
        return self.sensorID