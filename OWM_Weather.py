import pyowm
import time

clock = time.asctime()
owm = pyowm.OWM('0c3990a2a587901c24d0f0b229f05758')
mgr = owm.weather_manager()
three_hr_forecast = mgr.forecast_at_place("Adelaide, AU", "3h").forecast

for weather in three_hr_forecast:
    temp_in_celsius = weather.temperature("celsius")["feels_like"]
    sky = weather.detailed_status
    update_time = weather.reference_time(timeformat='iso')[11:13]
    update_date = weather.reference_time(timeformat='iso')[0:10]
    update_year = update_date[0:4]
    update_month = update_date[5:7]
    update_day = update_date[8:10]
    

    
    print()
    print("-"*21)
    print("Today is: " + update_day + " of " + update_month)
    print("At: ", update_time)
    print("The Sky should be " + sky)
    print("&")
    print("and the air feels like " + str(temp_in_celsius)+" degrees Celsius")
    print("-"*21)
    print()
    
