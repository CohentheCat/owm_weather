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
        curr_hour = int(ts[11:13])

        round_time = 3 * round(curr_hour/3)


        #compares the objects date property against today using list comprehesion 
        sorted_object_list = [dates for dates in weather_object_list if dates.reference_time(timeformat = 'iso')[0:10] == curr_date]
        for object in sorted_object_list:
            if int(object.reference_time(timeformat = 'iso')[11:13]) == round_time:
                weather_now = object
                
        return weather_now

        
#initialize the forcast object
forecast = OpenWeather(owm).makeObjectList()

#for single object
try:
    print(forecast.reference_time(timeformat = 'iso')[0:10])
    print(forecast.reference_time(timeformat = 'iso')[11:13])
    print(forecast.temperature("celsius")['temp'])
    
    #for list of objects
except TypeError:
    for object in forecast:
            print(object.reference_time(timeformat = "iso")[0:10])
            print(object.temperature("celsius")['temp']) 







