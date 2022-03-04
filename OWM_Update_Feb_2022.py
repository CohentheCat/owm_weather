import pyowm
import time
import datetime
import OWM_keys

clock = time.asctime()
owm = pyowm.OWM(OWM_keys.ApiKey)
mgr = owm.weather_manager()
three_hr_forecast = mgr.forecast_at_place("Frewville, AU", "3h").forecast
list_of_weather_objects = []

#constructs the weather object for usability
class WeatherObject:
    def __init__(self, temp_in_c, sky, update_time, update_date, update_year, update_month, update_day):
        self.temp_in_c = temp_in_c
        self.sky = sky
        self.update_time = update_time
        self.update_date = update_date
        self.update_year = update_year
        self.update_month = update_month
        self.update_day = update_day

    def Desciption_of_Weather_object(self):
        return f"Date: {self.update_day}/{self.update_month}/{self.update_year} at {self.update_time} \nTemp: {self.temp_in_c} \nSky: {self.sky}"

    def get_date(self):
        return f"{self.update_day}/{self.update_month}"
    def get_time(self):
        return self.update_time[0:2]

#Assigns the weather objects attributes
for weather in three_hr_forecast:
    temp_in_c = weather.temperature("celsius")["feels_like"]
    sky = weather.detailed_status
    update_time = weather.reference_time(timeformat='iso')[11:16]
    update_date = weather. reference_time(timeformat='iso')[0:10]
    update_year = update_date[0:4]
    update_month = update_date[5:7]
    update_day = update_date[8:10]
    objectW = WeatherObject(temp_in_c,sky,update_time,update_date,update_year,update_month,update_day)
    list_of_weather_objects.append(objectW)

#checks time now
dt = datetime.datetime.now()
time_str = dt.strftime("%H")
month_str = dt.strftime("%m")
day_str = dt.strftime("%d")
today = f"{day_str}/{month_str}"

count = 0
for i in list_of_weather_objects:
    if today == WeatherObject.get_date(i) and int(time_str) <= int(WeatherObject.get_time(i)):
        print("-" * 20)
        print(WeatherObject.Desciption_of_Weather_object(i))
        count + 1
        print("-"*20)
        time.sleep(3600)
    else:
        pass