from collections import OrderedDict
from ordered_set import OrderedSet

class Sensor:
    
    def __init__(self, sensorID):
        self.sensorID = sensorID
        self.dateMap = OrderedDict()
    
    def addTemperature(self, timestamp, temperature):
        date = timestamp[:10]
        time = timestamp[11:]
        if date not in self.dateMap:
            self.dateMap[date] = {}
        self.dateMap[date][time] = temperature

    def getDayTimesAndTemps(self, dayMap):
        timesAndTemps = OrderedSet()

        for time in dayMap:
            combo = time + " : " + str(dayMap[time])
            timesAndTemps.add(combo)

        return timesAndTemps

    def getAllTimesAndTemps(self):
        dateString = ""
        for date in self.dateMap.keys():
            dateString += str(self.getDayTimesAndTemps(self.dateMap.get(date))) + "\n"
        return dateString

    def getDates(self):
        return self.dateMap.keys
    
    def getDayMap(self, date):
        return self.dateMap.get(date)
    
    def __str__(self):
        toString = f"Sensor(ID: {self.sensorID})"
        #toString += self.getAllTimesAndTemps()
        return toString

        