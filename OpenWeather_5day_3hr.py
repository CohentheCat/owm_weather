from pyowm import OWM
from pprint import pprint
import datetime
import OWM_key

owm = OWM(OWM_key.key)

class OpenWeather:
    #initializes the api key
    def __init__(self, owm):
        self.owm = owm
        
    #function to create a list of forecast objects
    def makeObjectList(self):
        __mgr = owm.weather_manager()
        three_h_forecast = __mgr.forecast_at_place("Eudunda, AU", "3h").forecast
        weather_object_list = [weather for weather in three_h_forecast]
        #set a time object for logic
        ts = str(datetime.datetime.now())
        curr_date = str(ts[0:10])
        #compares the objects date property against today using list comprehesion 
        sorted_object_list = [dates for dates in weather_object_list if dates.reference_time(timeformat = 'iso')[0:10] == curr_date]
        return sorted_object_list

        

forecast = OpenWeather(owm).makeObjectList()



for object in forecast:
        print(object.reference_time(timeformat = "iso")[0:10])
        print(object.temperature("celsius")['temp'])





