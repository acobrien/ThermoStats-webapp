class Sensor:

    def __init__(self, sensorID):
        self.sensorID = sensorID
        self.datemap = {}
    
    def addTemperature(self, timestamp, temperature):
        date = timestamp[0, 10]
        time = timestamp[11:]
        if date in self.datemap:
            self.datemap[date] = {time: temperature}
            return
        self.datemap[{}] = date

    def display_temperatures(self):
        for date, times in self.datemap.items():
            print(f"Date: {date}")
            for time, temp in times.items():
                print(f"  {time}: {temp}°F")