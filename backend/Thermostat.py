from Sensor import Sensor

class Thermostat:
    def __init__(self):
        self.sensors = {}

    def addSensor(self, sensor):
        self.sensors.append(sensor)