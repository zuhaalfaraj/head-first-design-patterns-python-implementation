from . import Subject

class WeatherData(Subject):
    def __init__(self):
        self.humidity = None
        self.pressure = None
        self.temperature = None
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def get_temperature(self):
        if self.temperature is not None:
            return self.temperature
        else:
            return Exception("Temp is None")

    def get_humidity(self):
        if self.humidity is not None:
            return self.humidity
        else:
            return Exception("humidity is None")

    def get_pressure(self):
        if self.pressure is not None:
            return self.pressure
        else:
            return Exception("pressure is None")

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()