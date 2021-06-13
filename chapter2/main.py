from subjects.weather_data import WeatherData
from Observers import current_conditions, statistics, forcast


weather_data = WeatherData()
current_cond =  current_conditions.CurrentConditionsDisplay(weather_data)
stat = statistics.StatisticsDisplay(weather_data)
forc = forcast.ForecastDisplay(weather_data)

weather_data.set_measurements(30, 80, 33)
weather_data.set_measurements(21, 50, 22.5)
weather_data.set_measurements(14, 39, 40)