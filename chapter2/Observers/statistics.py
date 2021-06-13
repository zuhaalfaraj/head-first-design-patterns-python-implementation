from . import Observer, DisplayElement

class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.max_temp = 0
        self.min_temp = 200
        self.temp_sum = 0
        self.num_readings = 0

    def update(self, temp, humidity, pressure):
        self.num_readings += 1
        self.temp_sum += temp

        if temp > self.max_temp:
            self.max_temp = temp
        if temp < self.min_temp:
            self.min_temp = temp
        self.display()


    def display(self):
        print(f"Avg/Max/Min temperature = {(self.temp_sum / self.num_readings)}/{self.max_temp}/{self.min_temp}")