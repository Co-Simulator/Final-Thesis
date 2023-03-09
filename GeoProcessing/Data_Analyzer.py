import os
import pyproj
import random
import geojson
# import rasterio
import geopandas
import shapefile
import googlemaps
import pandas as pd
from lxml import etree
from dbfread import DBF
import lxml.etree as ET
from geojson import dumps


class Notification():
    
    # ask the user how many building wants to select and return it to GeoProcessing file
    def select_building(self):
        ask_number = int(input("How many buildings you want to select: "))
        return ask_number
    
    # Let the user know that IDs are assigned
    def ID_notif(self):
        print("   ")
        print("New IDs has been assigned to the selected buildings")

    # Let the user know that names are assigned
    def name_notif(self):
        print("   ")
        print("New names has been assigned to the selected buildings")

    # Let the user know that polygon type is assigned
    def type_notif(self):
        print("   ")
        print("Polygon type has been assigned to the selected buildings")
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    
    # Show interfaces to the user and return the selected one
    def building_height_interface(self):
        print("   ")
        print("Choose one of below interfaces to continue the process:")
        print("   ")
        user_input = input ("1_Pythonic interface.\n2_EXCEL file.\n3_CSV file.\n4_GeoSpatial\n5_Random assignment\n6_Skip and continue.\n7_Restart the process.\nType your answer:  ")  
        return user_input
        
    # Use this message for all Excel interfaces
    def building_excel_interface(self):
        print("An excel file has been created")
        user_input = input("When the file is filled, press '1' to continue: ")
        return user_input
    
    # Use this message for all CSV interfaces
    def building_csv_interface(self):
        print("A csv file has been created")
        user_input = input("When the file is filled, press '1' to continue: ")
        return user_input

    # Show interfaces to the user and return the selected one
    def building_category_interface(self):
        print("   ")
        print("Choose one of below interfaces to continue the process:")
        print("   ")
        user_input = input ("1_Pythonic interface.\n2_EXCEL file.\n3_CSV file.\n4_Google Places API\n5_Random assignment\n6_Skip and continue.\n7_Restart the process.\nType your answer:  ")  
        return user_input
 
    # All probable categories to be assumed as Residential 
    def building_category_API(self):
        residential_types = ["residenziale", "abitativa", "residenziale e commerciale", "residenziale e produttivo", "residential", "multi residential, multi-residential", "locality", "neighborhood"]
        return residential_types

    # Show interfaces to the user and return the selected one
    def building_floor_interface(self):
        print("   ")
        print("Choose one of below interfaces to continue the process:")
        print("   ")
        user_input = input ("1_Pythonic interface.\n2_EXCEL file.\n3_CSV file.\n4_Calculation based on height\n5_Random assignment\n6_Skip and continue.\n7_Restart the process.\nType your answer:  ")  
        return user_input

    # Show interfaces to the user and return the selected one
    def building_surface_interface(self):
        print("   ")
        print("Choose one of below interfaces to continue the process:")
        print("   ")
        user_input = input ("1_Pythonic interface.\n2_EXCEL file.\n3_CSV file.\n4_Random assignment\n5_Skip and continue.\n6_Restart the process.\nType your answer:  ")  
        return user_input

    # Show interfaces to the user and return the selected one
    def building_construnction_interface(self):
        print("   ")
        print("Choose one of below interfaces to continue the process:")
        print("   ")
        user_input = input ("1_Pythonic interface.\n2_EXCEL file.\n3_CSV file.\n4_Random assignment\n5_Skip and continue.\n6_Restart the process.\nType your answer:  ")  
        return user_input




#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#




class Initialization():
    
    def Places_API_key(self):
        API_key = "AIzaSyAn-V_D0aPmOlPPbjxE8708udXES2cV4-8"
        return API_key
    
    def SHP_reader(self):
        SHP = geopandas.GeoDataFrame.from_file(r"Files\A_SHP file\EDIFICIO.shp")
        return SHP

    def SHP_convertor(self):
        SHP = shapefile.Reader("Files\A_SHP file\EDIFICIO.shp")
        fields = SHP.fields[1:]
        field_names = [field[0] for field in fields]
        buffer = []
        for sr in SHP.shapeRecords():
            atr = dict(zip(field_names, sr.record))
            geom = sr.shape.__geo_interface__
            buffer.append(dict(type="Feature", geometry=geom, properties=atr))
        geojson = open("Files\B_Converted SHP to Geojson\GeoData.geojson", "w")
        geojson.write(dumps({"features": buffer}, indent=2) + "\n")
        geojson.close()

    # Read the converted SHP which is saved in GeoJSON format
    def Converted_SHP_reader(self):
        for file_name in os.listdir("Files\B_Converted SHP to Geojson"):
            if file_name.endswith(".geojson"):
                Geo_file = file_name
        input_directory = os.path.dirname(os.path.realpath('__file__'))
        with open(os.path.join(input_directory, 'Files/B_Converted SHP to Geojson/' + Geo_file)) as File:
            converted_file = geojson.load(File)
        return converted_file
    
    # Read the static GeoJSON file given by the user
    def Zone_profile_reader(self):
        for file_name in os.listdir("Files\C_Zone Profile"):
            if file_name.endswith(".geojson"):
                Zone_file = file_name
        input_directory = os.path.dirname(os.path.realpath('__file__'))
        with open(os.path.join(input_directory, 'Files/C_Zone Profile/' + Zone_file)) as File:
            zone_profile = geojson.load(File)
        return zone_profile

    def DTM_reader(self):
        for file_name in os.listdir("Files\E_GeoSpatial\DTM"):
            if file_name.endswith(".tif"):
                DTM_file = file_name
        input_directory = os.path.dirname(os.path.realpath('__file__'))
        DTM = rasterio.open(os.path.join(input_directory, 'Files/E_GeoSpatial/DTM/' + DTM_file))
        return DTM

    # Read DTM file and convert it if the standard is not in "EPSG:4326"
    def DTM_Convertor(self, DTM):
        input_directory = os.path.dirname(os.path.realpath('__file__'))
        DTM_rds = rasterio.open(os.path.join(input_directory, 'Files/E_GeoSpatial/DTM/' + DTM))
        DTM_rds_4326 = DTM_rds.rio.reproject("EPSG:4326")
        DTM_rds_4326.rio.to_raster("Files/E_GeoSpatial/DTM/DTM.tif")
        converted_DTM = rasterio.open(r"Files/E_GeoSpatial/DTM/DTM.tif")
        return converted_DTM

    def DSM_reader(self):
        for file_name in os.listdir("Files\E_GeoSpatial\DSM"):
            if file_name.endswith(".tif"):
                DSM_file = file_name
        input_directory = os.path.dirname(os.path.realpath('__file__'))
        DSM = rasterio.open(os.path.join(input_directory, 'Files/E_GeoSpatial/DSM/' + DSM_file))
        return DSM

    # Read DSM file and convert it if the standard is not in "EPSG:4326"
    def DSM_Convertoron(self, DSM):
        input_directory = os.path.dirname(os.path.realpath('__file__'))
        DSM_rds = rasterio.open(os.path.join(input_directory, 'Files/E_GeoSpatial/DSM' + DSM))
        DSM_rds_4326 = DSM_rds.rio.reproject("EPSG:4326")
        DSM_rds_4326.rio.to_raster("Files/E_GeoSpatial/DSM/DSM.tif")
        converted_DSM = rasterio.open(r"Files/E_GeoSpatial/DSM/DSM.tif")
        return converted_DSM




#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#




class Analyzer():
    
    def __len__(self, building):
        return len(building)
    
    # Check if there is any missing data on buildings height
    def height_analysis(self, selected_buildings, length):
        counter = 0
        for alt in range(length):
            if "ALTEZZA_VO" in selected_buildings[alt]["properties"]:
                pass
            else:
                counter += 1
        return counter
    
    
    def pythonic_height_interface(self, buildings, length):
        for j in range(length):
            if "ALTEZZA_VO" in buildings[j]["properties"]:
                pass
            else:
                height_ask = input(f'What is the height of building number {j}? ')
                buildings[j]["properties"]["ALTEZZA_VO"] = height_ask
        return buildings
    
    
    def excel_height_interface(self, buildings, length):
        height_dict = {"name": [],
                        "height": []}
        for i in range(length):
            if "ALTEZZA_VO" in buildings[i]["properties"]:
                pass
            else:
                height_dict["name"].append(buildings[i]["properties"]["NOME"])
                height_dict["height"].append("NONE")
        dataframe = pd.DataFrame.from_dict(height_dict)
        dataframe.to_excel("Files/F_Excel/building_height.xlsx") 
        user_input = Notification.building_excel_interface(self)
        if user_input == "1":
            height = pd.read_excel("Files/F_Excel/building_height.xlsx", index_col = 0)
            for j in range(length):
                buildings[j]["properties"]["ALTEZZA_VO"] = height["height"].loc[j]
        return buildings
          
    
    def csv_height_interface(self, buildings, length):
        height_dict = {"name": [],
                        "height": []}
        for i in range(length):
            if "ALTEZZA_VO" in buildings[i]["properties"]:
                pass
            else:
                height_dict["name"].append(buildings[i]["properties"]["NOME"])
                height_dict["height"].append("NONE")
        dataframe = pd.DataFrame.from_dict(height_dict)
        dataframe.to_csv("Files/G_CSV/building_height.csv") 
        user_input = Notification.building_csv_interface(self)
        if user_input == "1":
            height = pd.read_csv("Files/G_CSV/building_height.csv", index_col = 0)
            for j in range(length):
                buildings[j]["properties"]["ALTEZZA_VO"] = height["height"].loc[j]
        return buildings      


    def GeoSpatial_height_interface(self, buildings, length):
        for i in range(length):
            if "ALTEZZA_VO" in buildings[i]["properties"]:
                pass
            else:
                DTM = Initialization.DTM_reader(self)
                DTM_standard = DTM.crs
                if DTM_standard == 'EPSG:4326':
                    pass
                else:
                    DTM = Initialization.DTM_Convertor(self, DTM)
                    
                DSM = Initialization.DSM_reader(self)
                DSM_standard = DTM.crs
                if DSM_standard == 'EPSG:4326':
                    pass
                else:
                    DSM = Initialization.DSM_Convertor(self, DTM)
                    
                for i in range(length):
                    x = []
                    y = []
                    for j in range(len(buildings[i]["geometry"]["coordinates"][0])):
                        x.append(buildings[i]["geometry"]["coordinates"][0][j][0])
                        y.append(buildings[i]["geometry"]["coordinates"][0][j][1])
                        x.sort()
                        y.sort()
                        lat = sum(x)/len(x)
                        lon = sum(y)/len(y)
                    DTM_row, DTM_col = DTM.index(lat, lon)
                    DSM_row, DSM_col = DSM.index(lat, lon)
                    DTM_data = DTM.read(1)
                    DSM_data = DSM.read(1)
                    elevation = DSM_data[DSM_row, DSM_col] - DTM_data[DTM_row, DTM_col]
                    print(elevation)
                    if elevation > 2:
                        buildings[i]["properties"]["ALTEZZA_VO"] = elevation
                    else:
                        del buildings[i]
        return buildings
    
    def random_assign_height_interface(self, buildings, length):
        for i in range(length):
            if "ALTEZZA_VO" in buildings[i]["properties"]:
                pass
            else:
                height = random.randint(3, 20)
                buildings[i]["properties"]["ALTEZZA_VO"] = height
        return buildings
 
               
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#

    # Check if there is any missing data on buildings category
    def category_analysis(self, selected_buildings, length):
        counter = 0
        for categ in range(length):
            if "EDIFIC_USO" in selected_buildings[categ]["properties"]:
                pass
            else:
                counter += 1
        return counter


    def pythonic_category_interface(self, buildings, length):
        for j in range(length):
            if 'EDIFIC_USO' in buildings[j]["properties"]:
                pass
            else:
                categ_ask = input(f'What is the usage category of building number {j}? ')
                buildings[j]["properties"]["EDIFIC_USO"] = categ_ask
        return buildings


    def excel_category_interface(self, buildings, length):
        category_dict = {"name": [],
                        "category": []}
        for i in range(length):
            if "EDIFIC_USO" in buildings[i]["properties"]:
                pass
            else:
                category_dict["name"].append(buildings[i]["properties"]["NOME"])
                category_dict["category"].append("NONE")
        dataframe = pd.DataFrame.from_dict(category_dict)
        dataframe.to_excel("Files/F_Excel/building_category.xlsx") 
        user_input = Notification.building_excel_interface(self)
        if user_input == "1":
            category = pd.read_excel("Files/F_Excel/building_category.xlsx", index_col = 0)
            for j in range(length):
                buildings[j]["properties"]["EDIFIC_USO"] = category["category"].loc[j]
        return buildings
          
    
    def csv_category_interface(self, buildings, length):
        category_dict = {"name": [],
                        "category": []}
        for i in range(length):
            if "EDIFIC_USO" in buildings[i]["properties"]:
                pass
            else:
                category_dict["name"].append(buildings[i]["properties"]["NOME"])
                category_dict["category"].append("NONE")
        dataframe = pd.DataFrame.from_dict(category_dict)
        dataframe.to_csv("Files/G_CSV/building_category.csv") 
        user_input = Notification.building_csv_interface(self)
        if user_input == "1":
            category = pd.read_csv("Files/G_CSV/building_category.csv", index_col = 0)
            for j in range(length):
                buildings[j]["properties"]["EDIFIC_USO"] = category["category"].loc[j]
        return buildings     


    def API_category_interface(self, buildings, length):
        residential_types = Notification.building_category_API(self)
        for i in range(length):
            if "EDIFIC_USO" in buildings[i]["properties"]:
                pass
            else:
                for j in range(len(buildings[i]["geometry"]["coordinates"][0])):
                    x = []
                    y = []
                    x.append(buildings[i]["geometry"]["coordinates"][0][j][0])
                    y.append(buildings[i]["geometry"]["coordinates"][0][j][1])
                lon = str(sum(x)/len(x))
                lat = str(sum(y)/len(y))
                api_key = Initialization.Places_API_key(self)
                gmaps = googlemaps.Client(key = api_key)
                place_result = gmaps.places_nearby(location = (lat ,lon) , radius = 5)
                building_type = []
                for k in range(len(place_result["results"])):
                    for s in range(len(place_result["results"][k]["types"])):
                        building_type.append(place_result["results"][k]["types"][s])
                for m in building_type:
                    if m in residential_types:
                        redisential = True
                    else:
                        pass
                if redisential == True:
                    buildings[i]["properties"]["EDIFIC_USO"] = "residential"
                else:
                    buildings[i]["properties"]["EDIFIC_USO"] = "non-residential"
        return buildings

    def random_assign_category_interface(self, buildings, length):
        category = ["residential", "non-residential"]
        for i in range(length):
            if "EDIFIC_USO" in buildings[i]["properties"]:
                pass
            else:
                categ = random.choice(category)
                buildings[i]["properties"]["EDIFIC_USO"] = categ
        return buildings


    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#

    # Check if there is any missing data on buildings floor
    def floor_analysis(self, selected_buildings, length):
        counter = 0
        for floor in range(length):
            if "NUM_PIANI" in selected_buildings[floor]["properties"]:
                pass
            else:
                counter += 1
        return counter

    def pythonic_floor_interface(self, buildings, length):
        for j in range(length):
            if 'NUM_PIANI' in buildings[j]["properties"]:
                pass
            else:
                floor_ask = input(f'How many floors does the building number {j} has? ')
                buildings[j]["properties"]["NUM_PIANI"] = floor_ask
        return buildings

    def excel_floor_interface(self, buildings, length):
        floor_dict = {"name": [],
                        "floors": []}
        for i in range(length):
            if "NUM_PIANI" in buildings[i]["properties"]:
                pass
            else:
                floor_dict["name"].append(buildings[i]["properties"]["NOME"])
                floor_dict["floors"].append("NONE")
        dataframe = pd.DataFrame.from_dict(floor_dict)
        dataframe.to_excel("Files/F_Excel/building_floors.xlsx") 
        user_input = Notification.building_excel_interface(self)
        if user_input == "1":
            floors = pd.read_excel("Files/F_Excel/building_floors.xlsx", index_col = 0)
            for j in range(length):
                buildings[j]["properties"]["NUM_PIANI"] = floors["floors"].loc[j]
        return buildings

    def csv_floor_interface(self, buildings, length):
        floor_dict = {"name": [],
                        "floors": []}
        for i in range(length):
            if "NUM_PIANI" in buildings[i]["properties"]:
                pass
            else:
                floor_dict["name"].append(buildings[i]["properties"]["NOME"])
                floor_dict["floors"].append("NONE")
        dataframe = pd.DataFrame.from_dict(floor_dict)
        dataframe.to_csv("Files/G_CSV/building_floors.csv") 
        user_input = Notification.building_csv_interface(self)
        if user_input == "1":
            floors = pd.read_csv("Files/G_CSV/building_floors.csv", index_col = 0)
            for j in range(length):
                buildings[j]["properties"]["NUM_PIANI"] = floors["floors"].loc[j]
        return buildings     

    def floor_assign_height_based_interface(self, buildings, length):
        for i in range(length):
            if "NUM_PIANI" in buildings[i]["properties"]:
                pass
            else:
                height = buildings[i]["properties"]["ALTEZZA_VO"]
                floors = round(height/3)
                buildings[i]["properties"]["NUM_PIANI"] = floors
        return buildings
                
   
    def random_assign_floor_interface(self, buildings, length):
        for i in range(length):
            if "NUM_PIANI" in buildings[i]["properties"]:
                pass
            else:
                floor = random.randint(1, 10)
                buildings[i]["properties"]["NUM_PIANI"] = floor
        return buildings
            

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#

    # Check if there is any missing data on buildings surface
    def surface_analysis(self, selected_buildings, length):
        counter = 0
        for floor in range(length):
            if "SUPERFICIE" in selected_buildings[floor]["properties"]:
                pass
            else:
                counter += 1
        return counter         
            
    def pythonic_surface_interface(self, buildings, length):
        for j in range(length):
            if 'SUPERFICIE' in buildings[j]["properties"]:
                pass
            else:
                surface_ask = input(f'What is the surface of building number {j} ? ')
                buildings[j]["properties"]["SUPERFICIE"] = surface_ask
        return buildings

    def excel_surface_interface(self, buildings, length):
        surface_dict = {"name": [],
                        "surface": []}
        for i in range(length):
            if "SUPERFICIE" in buildings[i]["properties"]:
                pass
            else:
                surface_dict["name"].append(buildings[i]["properties"]["NOME"])
                surface_dict["surface"].append("NONE")
        dataframe = pd.DataFrame.from_dict(surface_dict)
        dataframe.to_excel("Files/F_Excel/building_surface.xlsx") 
        user_input = Notification.building_excel_interface(self)
        if user_input == "1":
            surface = pd.read_excel("Files/F_Excel/building_surface.xlsx", index_col = 0)
            for j in range(length):
                buildings[j]["properties"]["SUPERFICIE"] = surface["surface"].loc[j]
        return buildings

    def csv_surface_interface(self, buildings, length):
        surface_dict = {"name": [],
                        "surface": []}
        for i in range(length):
            if "SUPERFICIE" in buildings[i]["properties"]:
                pass
            else:
                surface_dict["name"].append(buildings[i]["properties"]["NOME"])
                surface_dict["surface"].append("NONE")
        dataframe = pd.DataFrame.from_dict(surface_dict)
        dataframe.to_csv("Files/G_CSV/building_surface.csv") 
        user_input = Notification.building_csv_interface(self)
        if user_input == "1":
            surface = pd.read_csv("Files/G_CSV/building_surface.csv", index_col = 0)
            for j in range(length):
                buildings[j]["properties"]["SUPERFICIE"] = surface["surface"].loc[j]
        return buildings                
            
    def random_assign_surface_interface(self, buildings, length):
       for i in range(length):
           if "SUPERFICIE" in buildings[i]["properties"]:
               pass
           else:
               surface = random.randint(50, 250)
               buildings[i]["properties"]["SUPERFICIE"] = surface
       return buildings           
            
            
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#

    # Check if there is any missing data on buildings construction year
    def construnction_analysis(self, selected_buildings, length):
        counter = 0
        for floor in range(length):
            if "EPOCA" in selected_buildings[floor]["properties"]:
                pass
            else:
                counter += 1
        return counter                   
            
    def pythonic_construnction_interface(self, buildings, length):
        for j in range(length):
            if 'EPOCA' in buildings[j]["properties"]:
                pass
            else:
                construction_ask = input(f'What is the construnction year of building number {j} ? ')
                buildings[j]["properties"]["EPOCA"] = construction_ask
        return buildings

    def excel_construnction_interface(self, buildings, length):
        construnction_dict = {"name": [],
                        "construnction": []}
        for i in range(length):
            if "EPOCA" in buildings[i]["properties"]:
                pass
            else:
                construnction_dict["name"].append(buildings[i]["properties"]["NOME"])
                construnction_dict["construnction"].append("NONE")
        dataframe = pd.DataFrame.from_dict(construnction_dict)
        dataframe.to_excel("Files/F_Excel/building_construnction.xlsx") 
        user_input = Notification.building_excel_interface(self)
        if user_input == "1":
            construnction = pd.read_excel("Files/F_Excel/building_construnction.xlsx", index_col = 0)
            for j in range(length):
                buildings[j]["properties"]["EPOCA"] = construnction["construnction"].loc[j]
        return buildings

    def csv_construnction_interface(self, buildings, length):
        construnction_dict = {"name": [],
                        "construnction": []}
        for i in range(length):
            if "EPOCA" in buildings[i]["properties"]:
                pass
            else:
                construnction_dict["name"].append(buildings[i]["properties"]["NOME"])
                construnction_dict["construnction"].append("NONE")
        dataframe = pd.DataFrame.from_dict(construnction_dict)
        dataframe.to_csv("Files/G_CSV/building_construnction.csv") 
        user_input = Notification.building_csv_interface(self)
        if user_input == "1":
            construnction = pd.read_csv("Files/G_CSV/building_construnction.csv", index_col = 0)
            for j in range(length):
                buildings[j]["properties"]["EPOCA"] = construnction["construnction"].loc[j]
        return buildings               
    
    def random_assign_construnction_interface(self, buildings, length):
       for i in range(length):
           if "EPOCA" in buildings[i]["properties"]:
               pass
           else:
               construnction = random.randint(1965, 1995)
               buildings[i]["properties"]["EPOCA"] = construnction
       return buildings     


    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
   
    # Checkthe construction year and assign a construction standard
    def construnction_type(self, selected_buildings, length):

        for j in range(length):
            if selected_buildings[j]["properties"]["EPOCA"] in range(1000, 1921):
                selected_buildings[j]["properties"]["Construction_Type"] = "STANDARD1"
                
            elif selected_buildings[j]["properties"]["EPOCA"] in range(1920, 1971):
                selected_buildings[j]["properties"]["Construction_Type"] = "STANDARD2"
        
            elif selected_buildings[j]["properties"]["EPOCA"] in range(1971, 1980):
                selected_buildings[j]["properties"]["Construction_Type"] = "STANDARD3"
        
            elif selected_buildings[j]["properties"]["EPOCA"] in range(1981, 2000):
                selected_buildings[j]["properties"]["Construction_Type"] = "STANDARD4"
        
            elif selected_buildings[j]["properties"]["EPOCA"] in range(2000, 2040):
                selected_buildings[j]["properties"]["Construction_Type"] = "STANDARD5"
            else:
                pass
        return selected_buildings


    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#

    # Assign HVAC specifications based on building category
    def HVAC_type(self, selected_buildings, length):

        for i in range(length):
            if selected_buildings[i]["properties"]["EDIFIC_USO"] == "residential":
                dbf = DBF('Files/I_DBF_Files/air_conditioning.dbf')
                dbf = pd.DataFrame(dbf)
                col = dbf.columns
                air_conditioning = []
                selected_buildings[i]["properties"]["air_conditioning"] = air_conditioning
                for j in range(len(col)):
                    selected_buildings[j]["properties"]["air_conditioning"].append({col[j] : " "})
            else:
                dbf = DBF('Files/I_DBF_Files/air_conditioning.dbf')
                dbf = pd.DataFrame(dbf)
                col = dbf.columns
                air_conditioning = []
                selected_buildings[i]["properties"]["air_conditioning"] = air_conditioning
                for j in range(len(col)):
                    selected_buildings[j]["properties"]["air_conditioning"].append({col[j] :dbf.loc[:,col[j]].to_dict()})
                
        return selected_buildings

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#

    # Assign supply system specifications based on building category
    def Supply_type(self, selected_buildings, length):

        for i in range(length):
            if selected_buildings[i]["properties"]["EDIFIC_USO"] == "residential":
                dbf = DBF('Files/I_DBF_Files/supply_systems.dbf')
                dbf = pd.DataFrame(dbf)
                col = dbf.columns
                supply_system = []
                selected_buildings[i]["properties"]["supply_system"] = supply_system
                for j in range(len(col)):
                    selected_buildings[j]["properties"]["supply_system"].append({col[j] : " "})
            else:
                dbf = DBF('Files/I_DBF_Files/supply_systems.dbf')
                dbf = pd.DataFrame(dbf)
                col = dbf.columns
                supply_system = []
                selected_buildings[i]["properties"]["supply_system"] = supply_system
                for j in range(len(col)):
                    selected_buildings[j]["properties"]["supply_system"].append({col[j] :dbf.loc[:,col[j]].to_dict()})
                
        return selected_buildings

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#

    # def CityGML_creator(self, buildings, length):


        # input_crs = pyproj.CRS('EPSG:4326')
        # output_crs = pyproj.CRS('EPSG:4978')
        # ns_citygml = 'http://www.opengis.net/citygml/2.0'
        # ns_bldg = 'http://www.opengis.net/citygml/building/2.0'
        # ns_gml = 'http://www.opengis.net/gml/3.2'
        
        # root = etree.Element('{%s}CityModel' % ns_citygml, nsmap={None: ns_citygml, 'bldg': ns_bldg, 'gml': ns_gml})
        # building = etree.SubElement(root, '{%s}building' % ns_bldg, {'{%s}id' % ns_gml: 'building1', 'usage': 'residential'})
        # solid = etree.SubElement(building, '{%s}boundedBy' % ns_bldg)
        
        # geometry = pd.DataFrame({
        #     'lon': [43.860304, 43.860301, 43.860296, 43.860298],
        #     'lat': [18.411144, 18.411143, 18.411149, 18.411150],
        #     'elev': [20.00, 20.00, 20.00, 20.00]
        # })
        # x, y, z = pyproj.transform(input_crs, output_crs, geometry['lon'].values, geometry['lat'].values, geometry['elev'].values)
        
        # pos_list = etree.SubElement(solid, '{%s}MultiSurface' % ns_gml)
        # surface = etree.SubElement(pos_list, '{%s}surfaceMember' % ns_gml)
        # polygon = etree.SubElement(surface, '{%s}Polygon' % ns_gml)
        
        # pos = ' '.join('{:.2f} {:.2f} {:.2f}'.format(x[i], y[i], z[i]) for i in range(len(x)))
        # ring = etree.SubElement(polygon, '{%s}exterior' % ns_gml)
        # pos_list = etree.SubElement(ring, '{%s}posList' % ns_gml, {'srsDimension': '3'})
        # pos_list.text = pos
        
        # doc = etree.ElementTree(root)
        # doc.write('output_citygml.gml', pretty_print=True, xml_declaration=True, encoding='UTF-8') 
    

    
    
    
    


#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#


          
           
# if __name__ == "__main__":
#     Main_Analysis = Analyzer()
#     Main_Analysis.height_analysis()