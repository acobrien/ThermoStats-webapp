from sensor import Sensor
from ordered_set import OrderedSet

class Thermostat:
    def __init__(self, thermostatID):
        self.thermostatID = thermostatID
        self.sensors = OrderedSet()

    def addSensor(self, sensor):
        self.sensors.add(sensor)

    def addTemperature(self, sensor, timestamp, temperature):
        sensor.addTemperature(timestamp, temperature)
        return True

    def getSensors(self):
        return self.sensors

    def getThermostatID(self):
        return self.thermostatID

    def __str__(self):
        return self.thermostatID