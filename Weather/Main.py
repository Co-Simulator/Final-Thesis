import json
import warnings 
import requests
import pandas as pd
import datetime as dt
from Weather_Helper import CaseFileReader, Notifications



class Weather:
    def __init__(self, weather_profile):
        self.Result = None 
        self.imported_file = None
        self.weather_profile = weather_profile


    def GET_from_API(self):
        Base_URL = f"http://api.openweathermap.org/data/2.5/weather?q={City}&appid={API_KEY}&units=metric"
        response = requests.get(Base_URL)
        Result = json.loads(response.text)
        Date_time = dt.datetime.utcfromtimestamp(Result["dt"])
        self.weather_profile["Date"] = Date_time.date()
        self.weather_profile["TempNow"] = Result["main"]["temp"]
        self.weather_profile["MinTemp"] = Result["main"]["temp_min"]
        self.weather_profile["MaxTemp"] = Result["main"]["temp_max"]
        self.weather_profile["RealFeel"] = Result["main"]["feels_like"]        
        self.weather_profile["Humidity"] = Result["main"]["humidity"]
        
       
    def resample_local_CSV(self, ask_sequence):
        self.imported_file = CaseFileReader.local_CSV_reader(CaseFileReader)
        self.resample = self.imported_file.resample(ask_sequence).mean().interpolate(method = "linear")
        self.resample.index = self.resample.index.strftime('%m/%d/%Y')
        self.resample.to_csv('Files/Resampled/resampled_weather_data.csv')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":  
    weather_profile = Notifications.API_data_container(Notifications)
    Main = Weather(weather_profile)
    init_step = Notifications.initial_step(Notifications)
    
    if init_step == "1":
        City, API_KEY = Notifications.API_components(Notifications)
        Main.GET_from_API()
    
    elif init_step == "2":
        ask_sequence = Notifications.resample_time_sequence(Notifications)
        Main.resample_local_CSV(ask_sequence)
    
    else: 
        print("Wrong Input")
