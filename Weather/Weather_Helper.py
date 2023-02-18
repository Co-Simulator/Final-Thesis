import os
import pandas as pd

class CaseFileReader():
    
    def __init__(self):
        self.name_search = None
        self.file_name = None
        self.weather_file = None
        self.resample = None   
    
    def local_CSV_reader(self):
        for self.name_search in os.listdir("Files\Local_Data"):
            if self.name_search.endswith(".csv"):
                self.file_name = self.name_search
        input_directory = os.path.dirname(os.path.realpath('__file__'))
        self.weather_file = pd.read_csv(os.path.join(input_directory, 'Files/Local_Data/' + self.file_name))
        self.weather_file['Date'] = pd.to_datetime(self.weather_file['Date'], format='%m/%d/%Y')
        self.weather_file.set_index('Date', inplace=True)

        return self.weather_file

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class Notifications:
    
    def initial_step(self):
        initial_ask = input("1_To get weather data from API.\n2_To import weather data from CSV file.\nType your answer: ")
        return initial_ask

    def resample_time_sequence(self):
        print("Select time period from below items:\nType 'Y' for yearly sampling.\nType 'Q' for seasonal sampling.\nType 'M' for monthly sampling.\nType 'SM' for semi-month sampling.\nType 'W' for weekly sampling.\nType 'D' for daily sampling.\nType 'H' for hourly sampling.\nType 'T' for minutely sampling.\nType 'S' for secondly  sampling.")
        time_sequence = input("Type your answer: ").upper()
        return time_sequence       

    def API_data_container(self):
        weather_profile = { "Date": "",
                          "TempNow": "",
                           "MinTemp": "",
                           "MaxTemp": "",
                           "RealFeel": "",
                           "Humidity": ""}  
        return weather_profile  
        
    def API_components(self):
        City = input("Type the name of the city: ")
        API_KEY = "09e35ebcf6f04c3f6398db89e0b9ae7d"      
        return City, API_KEY