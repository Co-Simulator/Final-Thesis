import json
import pandas as pd
from Data_Analyzer import Notification, Initialization, Analyzer

class GeoDataProcess():
    def __init__(self):
        # self.GeoFile = Initialization.SHP_reader(self)
        # Initialization.SHP_convertor(self)
        self.selected_buildings = Initialization.geo_fence_reader(self)
        self.lat = None
        self.lon = None
        
    def Building_selector(self):
        # Select number of building from static GeoJSON ot SHP database
        total_buildings = len(self.selected_buildings)
        print(f"The file contains {total_buildings} buildings") 

    # Assign new IDs
    def ID_assignment(self):
        for i in range(len(self.selected_buildings)):
            self.selected_buildings[i]["id"] = i
        Notification.ID_notif(self)
            
    # Assign a name
    def name_assignment(self):
        for j in range(len(self.selected_buildings)):
            self.selected_buildings[j]["Name"] = ("Building" + " " + "Number" + " " + str(j))
        Notification.name_notif(self)
    
    # Set the types as Polygon
    def type_assignment(self):
        for k in range(len(self.selected_buildings)):
            if "type" in self.selected_buildings[k]:
                pass
            else:
                self.selected_buildings[k]["type"] ="Polygon"
        Notification.type_notif(self)
              
    def building_height_check(self):
        # Check the lenght of the selected buildings from database
        length = Analyzer.__len__(self, self.selected_buildings)
        
        # Check if there is any building without height data
        missed_height = Analyzer.height_analysis(self, self.selected_buildings, length)
        if missed_height !=0:
            print("                                                            ") 
            print(f"{missed_height} buildings do not contain 'height' information")        
            # Offer interface to the user to compensate missing data
            interface = Notification.building_height_interface(self)
            if interface == "1":   #Python
                self.selected_buildings = Analyzer.pythonic_height_interface(self, self.selected_buildings, length)
            elif interface == "2": #Excel
                self.selected_buildings = Analyzer.excel_height_interface(self, self.selected_buildings, length)
            elif interface == "3": #CSV
                self.selected_buildings = Analyzer.csv_height_interface(self, self.selected_buildings, length)
            elif interface == "4": #Geo Spatial
                self.selected_buildings = Analyzer.GeoSpatial_height_interface(self, self.selected_buildings, length)
            elif interface == "5": #Random Assign
                self.selected_buildings = Analyzer.random_assign_height_interface(self, self.selected_buildings, length)
            elif interface == "6": # Skip
                pass
            else:
                self.Building_selector()
        # User do not want to select an interface, pass to next step
        else:
            pass
       
    def building_category_check(self):
        length = Analyzer.__len__(self, self.selected_buildings)
        
        # Check if there is any building without usage category data
        missed_category = Analyzer.category_analysis(self, self.selected_buildings, length)
        if missed_category != 0:
            print("                                                                ")
            print(f"{missed_category} buildings do not contain 'category' information")         
            # Offer interface to the user to compensate missing data
            interface = Notification.building_category_interface(self)
            if interface == "1":   #Python
                self.selected_buildings = Analyzer.pythonic_category_interface(self, self.selected_buildings, length)
            elif interface == "2": #Excel
                self.selected_buildings = Analyzer.excel_category_interface(self, self.selected_buildings, length)
            elif interface == "3": #CSV
                self.selected_buildings = Analyzer.csv_category_interface(self, self.selected_buildings, length)
            elif interface == "4": #Places API
                self.selected_buildings = Analyzer.API_category_interface(self, self.selected_buildings, length)
            elif interface == "5": #Random assign
                self.selected_buildings = Analyzer.random_assign_category_interface(self, self.selected_buildings, length)
            elif interface == "6": #Skip
                pass
            else:
                self.Building_selector()                   
        # User do not want to select an interface, pass to next step
        else:
            pass      

    def building_floor_check(self):
        length = Analyzer.__len__(self, self.selected_buildings)
        
        # Check if there is any building without floor data
        missed_floor = Analyzer.floor_analysis(self, self.selected_buildings, length)
        if missed_floor != 0:
            print("                                                                    ")
            print(f"{missed_floor} buildings do not contain number of 'floor' information")            
            # Offer interface to the user to compensate missing data
            interface = Notification.building_floor_interface(self)
            if interface == "1":   #Python
                self.selected_buildings = Analyzer.pythonic_floor_interface(self, self.selected_buildings, length)
            elif interface == "2": #Excel
                self.selected_buildings = Analyzer.excel_floor_interface(self, self.selected_buildings, length)
            elif interface == "3": #CSV
                self.selected_buildings = Analyzer.csv_floor_interface(self, self.selected_buildings, length)
            elif interface == "4": #Hight division
                self.selected_buildings = Analyzer.floor_assign_height_based_interface(self, self.selected_buildings, length)
                print("Number of floors has been successfully calculated based on the height of each building")
            elif interface == "5": #Random assign
                self.selected_buildings = Analyzer.random_assign_floor_interface(self, self.selected_buildings, length)
            elif interface == "6": #Skip
                pass
            else:
                self.Building_selector()
        # User do not want to select an interface, pass to next step
        else:
            pass
                           
    def building_surface_check(self):
        length = Analyzer.__len__(self, self.selected_buildings)
        # Check if there is any building without surface data
        missed_surface = Analyzer.surface_analysis(self, self.selected_buildings, length)
        if missed_surface != 0:
            print("                                                              ") 
            print(f"{missed_surface} buildings do not contain 'surface' information")
          
            # Offer interface to the user to compensate missing data
            interface = Notification.building_surface_interface(self)
            if interface == "1":   #Python
                self.selected_buildings = Analyzer.pythonic_surface_interface(self, self.selected_buildings, length)
            elif interface == "2": #Polygon
                self.selected_buildings = Analyzer.polygon_area(self, self.selected_buildings, length)
                print("Number of floors has been successfully calculated based on the height of each building")
            elif interface == "3": #Excel
                self.selected_buildings = Analyzer.excel_surface_interface(self, self.selected_buildings, length)
            elif interface == "4": #CSV
                self.selected_buildings = Analyzer.csv_surface_interface(self, self.selected_buildings, length)
            elif interface == "5": #Random assign
                self.selected_buildings = Analyzer.random_assign_surface_interface(self, self.selected_buildings, length)
            elif interface == "6": #Skip
                pass
            else:
                self.Building_selector()
        # User do not want to select an interface, pass to next step
        else:
            pass

    def building_construnction_check(self):
        length = Analyzer.__len__(self, self.selected_buildings)
        
        # Check if there is any building without construction year data
        missed_construnction = Analyzer.construnction_analysis(self, self.selected_buildings, length)
        if missed_construnction != 0:
            print("                                                                               ")
            print(f"{missed_construnction} buildings do not contain 'construnction year' information")
            
            # Offer interface to the user to compensate missing data
            interface = Notification.building_construnction_interface(self)
            if interface == "1":   #Python
                self.selected_buildings = Analyzer.pythonic_construnction_interface(self, self.selected_buildings, length)
            elif interface == "2": #Excel
                self.selected_buildings = Analyzer.excel_construnction_interface(self, self.selected_buildings, length)
            elif interface == "3": #CSV
                self.selected_buildings = Analyzer.csv_construnction_interface(self, self.selected_buildings, length)
            elif interface == "4": #Random assign
                self.selected_buildings = Analyzer.random_assign_construnction_interface(self, self.selected_buildings, length)
            elif interface == "5": #Skip
                pass
            else:
                self.Building_selector()   
        # User do not want to select an interface, pass to next step
        else:
            pass

    def Standard_type_assign(self):
        length = Analyzer.__len__(self, self.selected_buildings)
        self.selected_buildings = Analyzer.construnction_type(self, self.selected_buildings, length)

    def HVAC_type_assign(self):
        length = Analyzer.__len__(self, self.selected_buildings)
        self.selected_buildings = Analyzer.HVAC_type(self, self.selected_buildings, length)

    def Supply_type_assign(self):
        length = Analyzer.__len__(self, self.selected_buildings)
        self.selected_buildings = Analyzer.Supply_type(self, self.selected_buildings, length)
        with open('G:/Final-Project/GeoProcessing/Files/D_Teaser Profile/Teaser.geojson', 'w') as f:
                             json.dump(self.selected_buildings, f)

#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#

if __name__ == "__main__":
    Main_Geo = GeoDataProcess()
    Main_Geo.Building_selector()
    Main_Geo.ID_assignment()
    Main_Geo.name_assignment()
    Main_Geo.type_assignment()
    Main_Geo.building_height_check()
    Main_Geo.building_category_check()
    Main_Geo.building_floor_check()
    Main_Geo.building_surface_check()  
    Main_Geo.building_construnction_check() 
    Main_Geo.Standard_type_assign()
    Main_Geo.HVAC_type_assign()  
    Main_Geo.Supply_type_assign()  