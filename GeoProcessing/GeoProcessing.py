import pandas as pd
from Data_Analyzer import Notification, Initialization, Analyzer




class GeoDataProcess():
    def __init__(self):
        # self.GeoFile = Initialization.SHP_reader(self)
        # Initialization.SHP_convertor(self)
        self.Profile = Initialization.Converted_SHP_reader(self)
        self.selected_buildings = []
        self.lat = None
        self.lon = None
        print("ME")
        
    def Building_selector(self):
        total_buildings = len(self.Profile["features"])
        print(f"The file contains {total_buildings} buildings")
        user_input_number = Notification.select_building(self)
        for Building in range(user_input_number):
            self.selected_buildings.append(self.Profile["features"][Building])

    
    def ID_assignment(self):
        for i in range(len(self.selected_buildings)):
            self.selected_buildings[i]["properties"]["ID"] = i
        Notification.ID_notif(self)
            
            
    def name_assignment(self):
        for j in range(len(self.selected_buildings)):
            self.selected_buildings[j]["properties"]["NOME"] = ("Building" + " " + "Number" + " " + str(j))
        Notification.name_notif(self)
    
    
    def type_assignment(self):
        for k in range(len(self.selected_buildings)):
            if "type" in self.selected_buildings[k]["geometry"]:
                pass
            else:
                self.selected_buildings[k]["geometry"]["type"].append("Polygon") 
        Notification.type_notif(self)
        
        
    def building_height_check(self):
        length = Analyzer.__len__(self, self.selected_buildings)
        missed_height = Analyzer.height_analysis(self, self.selected_buildings, length)
        if missed_height !=0:
            print(f"{missed_height} buildings do not contain height information")
            interface = Notification.building_height_interface(self)
            if interface == "1":
                self.selected_buildings = Analyzer.pythonic_height_interface(self, self.selected_buildings, length)
            elif interface == "2":
                self.selected_buildings = Analyzer.excel_height_interface(self, self.selected_buildings, length)
            elif interface == "3":
                self.selected_buildings = Analyzer.csv_height_interface(self, self.selected_buildings, length)
            elif interface == "4":
                self.selected_buildings = Analyzer.GeoSpatial_height_interface(self, self.selected_buildings, length)
            elif interface == "5":
                self.selected_buildings = Analyzer.random_assign_height_interface(self, self.selected_buildings, length)
            elif interface == "6":
                pass
            else:
                self.Building_selector()
        else:
            pass
    
    
    def building_category_check(self):
        length = Analyzer.__len__(self, self.selected_buildings)
        missed_category = Analyzer.category_analysis(self, self.selected_buildings, length)
        if missed_category != 0:
            print(f"{missed_category} buildings do not contain height information")
            interface = Notification.building_category_interface(self)
            if interface == "1":
                self.selected_buildings = Analyzer.pythonic_category_interface(self, self.selected_buildings, length)
            elif interface == "2":
                self.selected_buildings = Analyzer.excel_category_interface(self, self.selected_buildings, length)
            elif interface == "3":
                self.selected_buildings = Analyzer.csv_category_interface(self, self.selected_buildings, length)
            elif interface == "4":
                self.selected_buildings = Analyzer.API_category_interface(self, self.selected_buildings, length)
            elif interface == "5":
                self.selected_buildings = Analyzer.random_assign_category_interface(self, self.selected_buildings, length)
            elif interface == "6":
                pass
            else:
                self.Building_selector()                   
        else:
            pass
        

    def building_floor_check(self):
        length = Analyzer.__len__(self, self.selected_buildings)
        missed_floor = Analyzer.floor_analysis(self, self.selected_buildings, length)
        if missed_floor != 0:
            print(f"{missed_floor} buildings do not contain height information")        
            interface = Notification.building_floor_interface(self)
            if interface == "1":
                self.selected_buildings = Analyzer.pythonic_floor_interface(self, self.selected_buildings, length)
            elif interface == "2":
                self.selected_buildings = Analyzer.excel_floor_interface(self, self.selected_buildings, length)
            elif interface == "3":
                self.selected_buildings = Analyzer.csv_floor_interface(self, self.selected_buildings, length)
            elif interface == "4":
                self.selected_buildings = Analyzer.floor_assign_height_based_interface(self, self.selected_buildings, length)
            elif interface == "5":
                self.selected_buildings = Analyzer.random_assign_floor_interface(self, self.selected_buildings, length)
            elif interface == "6":
                pass
            else:
                self.Building_selector()
        else:
            pass
                           

    def building_surface_check(self):
        length = Analyzer.__len__(self, self.selected_buildings)
        missed_surface = Analyzer.surface_analysis(self, self.selected_buildings, length)
        if missed_surface != 0:
            print(f"{missed_surface} buildings do not contain height information")
            interface = Notification.building_surface_interface(self)
            if interface == "1":
                self.selected_buildings = Analyzer.pythonic_surface_interface(self, self.selected_buildings, length)
            elif interface == "2":
                self.selected_buildings = Analyzer.excel_surface_interface(self, self.selected_buildings, length)
            elif interface == "3":
                self.selected_buildings = Analyzer.csv_surface_interface(self, self.selected_buildings, length)
            elif interface == "4":
                self.selected_buildings = Analyzer.random_assign_surface_interface(self, self.selected_buildings, length)
            elif interface == "5":
                pass
            else:
                self.Building_selector()
        else:
            pass
        

    def building_construnction_check(self):
        length = Analyzer.__len__(self, self.selected_buildings)
        missed_construnction = Analyzer.construnction_analysis(self, self.selected_buildings, length)
        if missed_construnction != 0:
            print(f"{missed_construnction} buildings do not contain height information")
            interface = Notification.building_construnction_interface(self)
            if interface == "1":
                self.selected_buildings = Analyzer.pythonic_construnction_interface(self, self.selected_buildings, length)
            elif interface == "2":
                self.selected_buildings = Analyzer.excel_construnction_interface(self, self.selected_buildings, length)
            elif interface == "3":
                self.selected_buildings = Analyzer.csv_construnction_interface(self, self.selected_buildings, length)
            elif interface == "4":
                self.selected_buildings = Analyzer.random_assign_construnction_interface(self, self.selected_buildings, length)
            elif interface == "5":
                pass
            else:
                self.Building_selector()              
        else:
            pass
            
            
    def data_frame_export(self):
        return self.selected_buildings
        # length = Analyzer.__len__(self, self.selected_buildings)
        # Analyzer.CityGML_creator(self, self.selected_buildings, length)


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
    # Main_Geo.data_frame_export()