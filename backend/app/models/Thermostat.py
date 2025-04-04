from ordered_set import OrderedSet

class Thermostat:
    def __init__(self, thermostatID):
        self.thermostatID = thermostatID
        self.sensors = OrderedSet()

        if self.thermostatID == "0":
            self.sensorKeys = OrderedSet(["Master Bedroom","Master Bathroom","Office",
                        "Ty's Bedroom","Luke's Bedroom","Sabry's Bedroom","Living Room"])
        elif self.thermostatID == "1":
            self.sensorKeys = OrderedSet(["Brody's Bedroom","Kitchen","Den","Bar","Living Room","Outside"])
        else:
            self.sensorKeys = OrderedSet()

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
        #    toString += str(sensor)
        return toString