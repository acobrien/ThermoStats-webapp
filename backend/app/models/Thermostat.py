from ordered_set import OrderedSet
from collections import OrderedDict

class Thermostat:
    def __init__(self, thermostatID):
        self.thermostatID = thermostatID
        self.sensors = OrderedSet()
        self.dateActivityMap = OrderedDict()

        if self.thermostatID == "0":
            self.sensorKeys = OrderedSet(["Master Bedroom","Master Bathroom","Office",
                        "Ty's Bedroom","Luke's Bedroom","Sabry's Bedroom","Living Room"])

        elif self.thermostatID == "1":
            self.sensorKeys = OrderedSet(["Brody's Bedroom","Kitchen","Den","Bar","Living Room","Outside"])

        else:
            self.sensorKeys = OrderedSet()

    def addActivity(self, timestamp, activity):
        date = timestamp[:10]
        time = timestamp[11:]
        if date not in self.dateActivityMap:
            self.dateActivityMap[date] = {}
        self.dateActivityMap[date][time] = activity

    def getTimeList(self, date):
        timeList = []
        if date in self.dateActivityMap:
            for time in self.dateActivityMap[date]:
                timeList.append(time)
            return timeList
        else:
            return KeyError("Date not found in dateActivityMap")

    def getActivityList(self, date):
        activityList = []
        if date in self.dateActivityMap:
            for time in self.dateActivityMap[date]:
                activityList.append(self.dateActivityMap[date][time])
            return activityList
        else:
            return KeyError("Date not found in dateActivityMap")

    def addSensor(self, sensor):
        if sensor not in self.sensors:
            self.sensors.add(sensor)

    def addTemperature(self, sensor, timestamp, temperature):
        if sensor in self.sensors:
            sensor.addTemperature(timestamp, temperature)
            return True
        return False

    def getSensors(self):
        return self.sensors

    def getDates(self):
        dates = []
        for date in self.dateActivityMap:
            dates.append(date)
        return dates

    def getEnergyCost(self, date):
        cost = 0
        if date in self.dateActivityMap:
            for time in self.dateActivityMap[date]:
                match self.dateActivityMap[date][time]:
                    case "1" | "2": # heating | cooling
                        cost += 0.02955 # half of value from save_format because it is a 30 second reading
                    case "5": # airwave
                        cost += 0.00355
            return cost * 0.152 # price per kwh
        else:
            return KeyError("Date not found in dateActivityMap")

    def getSensorByID(self, searchID):
        for sensor in self.sensors:
            if sensor.getSensorID() == searchID:
                return sensor
        return None

    def getThermostatID(self):
        return self.thermostatID
    
    def getThermostatIDNum(self):
        if self.thermostatID == "East Side":
            return "0"
        elif self.thermostatID == "West Side":
            return "1"

    def __str__(self):
        toString = f"Thermostat(ID: {self.thermostatID})\n"
        #for sensor in self.sensors:
        #--  toString += str(sensor) --NOTE: OLD CODE, prints out 1000+ lines just to see if things are being added
        return toString