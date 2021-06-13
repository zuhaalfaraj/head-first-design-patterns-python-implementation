from . import Observer, DisplayElement

class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.temperature = None
        self.humidity = None

    def update(self, temp, humidity, pressure):
        self.temperature = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature}F degrees and {self.humidity}% humidity")