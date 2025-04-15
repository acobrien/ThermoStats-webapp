from collections import OrderedDict
from ordered_set import OrderedSet

class Sensor:
    
    def __init__(self, sensorID):
        self.sensorID = sensorID
        self.dateMap = OrderedDict()
    
    def addData(self, timestamp, dataArray):
        date = timestamp[:10]
        time = timestamp[11:]
        if date not in self.dateMap:
            self.dateMap[date] = {}
        self.dateMap[date][time] = dataArray #[thermostat mode, temperature]

    def getDayTimesAndData(self, date):
        timesAndData = OrderedSet()
        if date in self.dateMap:
            for time in self.dateMap[date]:
                combo = time + " : " + str(self.dateMap[date][time][0]) + " : " + str(self.dateMap[date][time][1])
                timesAndData.add(combo)
            
            return timesAndData
        else:
            return KeyError("Date not found in dateMap")

    def getSensorID(self):
        return self.sensorID
    
    def getAllTimesAndDataString(self):
        dateString = ""
        for date in self.dateMap.keys():
            dateString += str(self.getDayTimesAndData(self.dateMap.get(date))) + "\n"
        return dateString

    def getDates(self):
        return list(self.dateMap.keys())
    
    def getDayMap(self, date):
        return self.dateMap.get(date)
    
    def __str__(self):
        toString = f"Sensor(ID: {self.sensorID})"
        #-- toString += self.getAllTimesAndTemps() --NOTE: OLD CODE, prints out 1000+ lines just to test if stuff is being added
        return toString