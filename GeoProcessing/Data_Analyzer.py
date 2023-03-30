import os
import re
import random
import geojson
import requests
# import rasterio
import geopandas
import shapefile
# import googlemaps
import pandas as pd
from dbfread import DBF
from geojson import dumps
from pyproj import Transformer
from shapely.geometry import Polygon

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
        user_input = input("After filling the file, you need to press '1' to proceed: ")
        return user_input
    
    # Use this message for all CSV interfaces
    def building_csv_interface(self):
        print("A csv file has been created")
        user_input = input("After filling the file, you need to press '1' to proceed: ")
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
        user_input = input ("1_Pythonic interface.\n2_Polygon area calculation\n3_EXCEL file.\n4_CSV file.\n5_Random assignment\n6_Skip and continue.\n7_Restart the process.\nType your answer:  ")  
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
    def geo_fence_reader(self):
        for file_name in os.listdir("G:\Final-Project\GeoProcessing\Files\J_Downloaded_Fence"):
            if file_name.endswith(".geojson"):
                Geo_file = file_name
        input_directory = os.path.dirname(os.path.realpath('__file__'))
        with open(os.path.join(input_directory, 'Files/J_Downloaded_Fence/' + Geo_file)) as File:
            Fence = geojson.load(File)
        return Fence

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
            if "height" in selected_buildings[alt]["tags"]:
                pass
            else:
                counter += 1
        return counter
    
    def pythonic_height_interface(self, buildings, length):
        for j in range(length):
            if "height" in buildings[j]["tags"]:
                pass
            else:
                height_ask = input(f'What is the height of building number {j}? ')
                buildings[j]["tags"]["height"] = height_ask
        return buildings
    
    def excel_height_interface(self, buildings, length):
        height_dict = {"name": [],
                        "height": []}
        for i in range(length):
            if "height" in buildings[i]["tags"]:
                pass
            else:
                height_dict["name"].append(buildings[i]["Name"])
                height_dict["height"].append("NONE")
        dataframe = pd.DataFrame.from_dict(height_dict)
        dataframe.to_excel("Files/F_Excel/building_height.xlsx") 
        user_input = Notification.building_excel_interface(self)
        if user_input == "1":
            height = pd.read_excel("Files/F_Excel/building_height.xlsx", index_col = 0)
            for j in range(len(height)):
                buildings[j]["tags"]["height"] = height["height"].loc[j]
        print("Height values are assigned successfully")
        return buildings
              
    def csv_height_interface(self, buildings, length):
        height_dict = {"name": [],
                        "height": []}
        for i in range(length):
            if "height" in buildings[i]["tags"]:
                pass
            else:
                height_dict["name"].append(buildings[i]["Name"])
                height_dict["height"].append("NONE")
        dataframe = pd.DataFrame.from_dict(height_dict)
        dataframe.to_csv("Files/G_CSV/building_height.csv") 
        user_input = Notification.building_csv_interface(self)
        if user_input == "1":
            height = pd.read_csv("Files/G_CSV/building_height.csv", index_col = 0)
            for j in range(len(height)):
                buildings[j]["tags"]["height"] = height["height"].loc[j]
        print("Height values are assigned successfully")
        return buildings      

    def GeoSpatial_height_interface(self, buildings, length):
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
            if "height" in buildings[i]["tags"]:
                pass
            else:
                lat = buildings[i]["center"]["lat"]
                lon = buildings[i]["center"]["lon"]
                DTM_row, DTM_col = DTM.index(lon, lat)
                DSM_row, DSM_col = DSM.index(lon, lat)
                DTM_data = DTM.read(1)
                DSM_data = DSM.read(1)
                elevation = DSM_data[DSM_row, DSM_col] - DTM_data[DTM_row, DTM_col]
                buildings[i]["tags"]["height"] = int(elevation)
        if elevation > 1.9:
            pass
        else:
            del buildings[i]
        return buildings
    
    def random_assign_height_interface(self, buildings, length):
        for i in range(length):
            if "height" in buildings[i]["tags"]:
                pass
            else:
                height = random.randint(3, 20)
                buildings[i]["tags"]["height"] = height
        print("Missing heights are randomly assigned")
        return buildings
           
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#

    # Check if there is any missing data on buildings category
    def category_analysis(self, selected_buildings, length):
        counter = 0
        for categ in range(length):
            if "building:use" in selected_buildings[categ]["tags"] or "building" in selected_buildings[categ]["tags"]:
                pass
            else:
                counter += 1
        return counter

    def pythonic_category_interface(self, buildings, length):
        for j in range(length):
            if 'building:use' in buildings[j]["tags"] or "building" in buildings[j]["tags"]:
                pass
            else:
                categ_ask = input(f'What is the usage category of building number {j}? ')
                buildings[j]["tags"]["building:use"] = categ_ask
        return buildings

    def excel_category_interface(self, buildings, length):
        category_dict = {"name": [],
                        "category": []}
        for i in range(length):
            if "building:use" in buildings[i]["tags"]:
                pass
            else:
                category_dict["name"].append(buildings[i]["Name"])
                category_dict["category"].append("NONE")
        dataframe = pd.DataFrame.from_dict(category_dict)
        dataframe.to_excel("Files/F_Excel/building_category.xlsx") 
        user_input = Notification.building_excel_interface(self)
        if user_input == "1":
            category = pd.read_excel("Files/F_Excel/building_category.xlsx", index_col = 0)
            for j in range(len(category)):
                buildings[j]["tags"]["building:use"] = category["category"].loc[j]
        return buildings
   
    def csv_category_interface(self, buildings, length):
        category_dict = {"name": [],
                        "category": []}
        for i in range(length):
            if "building:use" in buildings[i]["tags"]:
                pass
            else:
                category_dict["name"].append(buildings[i]["Name"])
                category_dict["category"].append("NONE")
        dataframe = pd.DataFrame.from_dict(category_dict)
        dataframe.to_csv("Files/G_CSV/building_category.csv") 
        user_input = Notification.building_csv_interface(self)
        if user_input == "1":
            category = pd.read_csv("Files/G_CSV/building_category.csv", index_col = 0)
            for j in range(len(category)):
                buildings[j]["tags"]["building:use"] = category["category"].loc[j]
        return buildings     

    def API_category_interface(self, buildings, length):
        residential_types = Notification.building_category_API(self)
        for i in range(length):
            if "building:use" in buildings[i]["tags"]:
                pass
            else:
                lat = buildings[i]["center"]["lat"]
                lon = buildings[i]["center"]["lon"]
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
                    buildings[i]["tags"]["building:use"] = "residential"
                else:
                    buildings[i]["tags"]["building:use"] = "non-residential"
        return buildings

    def random_assign_category_interface(self, buildings, length):
        category = ["residential", "non-residential"]
        for i in range(length):
            categ = random.choice(category)
            buildings[i]["tags"]["building"] = categ
        return buildings

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#

    # Check if there is any missing data on buildings floor
    def floor_analysis(self, selected_buildings, length):
        counter = 0
        for floor in range(length):
            if "building:levels" in selected_buildings[floor]["tags"]:
                pass
            else:
                counter += 1
        return counter

    def pythonic_floor_interface(self, buildings, length):
        for j in range(length):
            if 'building:levels' in buildings[j]["tags"]:
                pass
            else:
                floor_ask = input(f'How many floors does the building number {j} has? ')
                buildings[j]["tags"]["building:levels"] = floor_ask
        return buildings

    def excel_floor_interface(self, buildings, length):
        floor_dict = {"name": [],
                        "floors": []}
        for i in range(length):
            if "building:levels" in buildings[i]["tags"]:
                pass
            else:
                floor_dict["name"].append(buildings[i]["Name"])
                floor_dict["floors"].append("NONE")
        dataframe = pd.DataFrame.from_dict(floor_dict)
        dataframe.to_excel("Files/F_Excel/building_floors.xlsx") 
        user_input = Notification.building_excel_interface(self)
        if user_input == "1":
            floors = pd.read_excel("Files/F_Excel/building_floors.xlsx", index_col = 0)
            for j in range(len(floors)):
                buildings[j]["tags"]["building:levels"] = floors["floors"].loc[j]
        return buildings

    def csv_floor_interface(self, buildings, length):
        floor_dict = {"name": [],
                        "floors": []}
        for i in range(length):
            if "building:levels" in buildings[i]["tags"]:
                pass
            else:
                floor_dict["name"].append(buildings[i]["Name"])
                floor_dict["floors"].append("NONE")
        dataframe = pd.DataFrame.from_dict(floor_dict)
        dataframe.to_csv("Files/G_CSV/building_floors.csv") 
        user_input = Notification.building_csv_interface(self)
        if user_input == "1":
            floors = pd.read_csv("Files/G_CSV/building_floors.csv", index_col = 0)
            for j in range(len(floors)):
                buildings[j]["tags"]["building:levels"] = floors["floors"].loc[j]
        return buildings     

    def floor_assign_height_based_interface(self, buildings, length):
        for i in range(length):
            if "building:levels" in buildings[i]["tags"]:
                pass
            else:
                height = buildings[i]["tags"]["height"]
                if type(height) == int or type(height) == float:
                    pass
                
                elif re.match(r"^\d+m$", height):
                    height = float(height[:-1])
                    buildings[i]["tags"]["height"] = height
                
                elif re.match(r"^\d+\s*m$", height):
                    height = float(height[:-2])
        
                elif re.match(r"^\d+(\.\d+)?$", height):
                    height = float(height)
        
                elif re.match(r"^\d+(\.\d+)?\s*m$", height):
                    height = float(height[:-2])
        
                else:
                    height = float(height)
            
                buildings[i]["tags"]["height"] = height
                floors = round(height/3)
                buildings[i]["tags"]["building:levels"] = floors
        return buildings           
   
    def random_assign_floor_interface(self, buildings, length):
        for i in range(length):
            if "building:levels" in buildings[i]["tags"]:
                pass
            else:
                floor = random.randint(1, 10)
                buildings[i]["tags"]["building:levels"] = floor
        return buildings

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#

    # Check if there is any missing data on buildings surface
    def surface_analysis(self, selected_buildings, length):
        counter = 0
        for floor in range(length):
            if "surface" in selected_buildings[floor]["tags"]:
                pass
            else:
                counter += 1
        return counter         
            
    def pythonic_surface_interface(self, buildings, length):
        for j in range(length):
            if 'surface' in buildings[j]["tags"]:
                pass
            else:
                surface_ask = input(f'What is the surface of building number {j} ? ')
                buildings[j]["tags"]["surface"] = surface_ask
        return buildings

    def polygon_area(self, buildings, length):
        for i in range(length):
            pol = []
            for j in range(len(buildings[i]["nodes"])):
                node_id = buildings[i]["nodes"][j]
                query = f"""
                    [out:json];
                    node({node_id});
                    out center;
                """
                response = requests.get(f"http://overpass-api.de/api/interpreter?data={query}")
                data = response.json()
                lat = data["elements"][0]["lat"]
                lon = data["elements"][0]["lon"]
                proj4326 = Transformer.from_crs("epsg:4326", "epsg:3857")
                proj3857 = Transformer.from_crs("epsg:3857", "epsg:4326")
                x, y = proj4326.transform(lon, lat)
                lon, lat = proj3857.transform(x, y)
                lon = "{:.7f}".format(lon)
                lat = "{:.7f}".format(lat)
                pol.append((float(lon), float(lat)))
            proj4326 = Transformer.from_crs("epsg:4326", "epsg:3857")
            proj3857 = Transformer.from_crs("epsg:3857", "epsg:4326")
            x, y = proj4326.transform(*zip(*pol))
            poly = Polygon(zip(x, y))
            area = round(poly.area)
            buildings[i]["tags"]["surface"] = area     
        return buildings   

    def excel_surface_interface(self, buildings, length):
        surface_dict = {"name": [],
                        "surface": []}
        for i in range(length):
            if "surface" in buildings[i]["tags"]:
                pass
            else:
                surface_dict["name"].append(buildings[i]["Name"])
                surface_dict["surface"].append("NONE")
        dataframe = pd.DataFrame.from_dict(surface_dict)
        dataframe.to_excel("Files/F_Excel/building_surface.xlsx") 
        user_input = Notification.building_excel_interface(self)
        if user_input == "1":
            surface = pd.read_excel("Files/F_Excel/building_surface.xlsx", index_col = 0)
            for j in range(len(surface)):
                buildings[j]["tags"]["surface"] = surface["surface"].loc[j]
        return buildings

    def csv_surface_interface(self, buildings, length):
        surface_dict = {"name": [],
                        "surface": []}
        for i in range(length):
            if "surface" in buildings[i]["tags"]:
                pass
            else:
                surface_dict["name"].append(buildings[i]["Name"])
                surface_dict["surface"].append("NONE")
        dataframe = pd.DataFrame.from_dict(surface_dict)
        dataframe.to_csv("Files/G_CSV/building_surface.csv") 
        user_input = Notification.building_csv_interface(self)
        if user_input == "1":
            surface = pd.read_csv("Files/G_CSV/building_surface.csv", index_col = 0)
            for j in range(len(surface)):
                buildings[j]["tags"]["surface"] = surface["surface"].loc[j]
        return buildings                
            
    def random_assign_surface_interface(self, buildings, length):
       for i in range(length):
           if "surface" in buildings[i]["tags"]:
               pass
           else:
               surface = random.randint(50, 250)
               buildings[i]["tags"]["surface"] = surface
       return buildings                     
            
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#

    # Check if there is any missing data on buildings construction year
    def construnction_analysis(self, selected_buildings, length):
        counter = 0
        for floor in range(length):
            if "start_date" in selected_buildings[floor]["tags"]:
                pass
            else:
                counter += 1
        return counter                   
            
    def pythonic_construnction_interface(self, buildings, length):
        for j in range(length):
            if 'start_date' in buildings[j]["tags"]:
                pass
            else:
                construction_ask = input(f'What is the construnction year of building number {j} ? ')
                buildings[j]["tags"]["start_date"] = construction_ask
        return buildings

    def excel_construnction_interface(self, buildings, length):
        construnction_dict = {"name": [],
                        "construnction": []}
        for i in range(length):
            if "start_date" in buildings[i]["tags"]:
                pass
            else:
                construnction_dict["name"].append(buildings[i]["Name"])
                construnction_dict["construnction"].append("NONE")
        dataframe = pd.DataFrame.from_dict(construnction_dict)
        dataframe.to_excel("Files/F_Excel/building_construnction.xlsx") 
        user_input = Notification.building_excel_interface(self)
        if user_input == "1":
            construnction = pd.read_excel("Files/F_Excel/building_construnction.xlsx", index_col = 0)
            for j in range(len(construnction)):
                buildings[j]["tags"]["start_date"] = construnction["construnction"].loc[j]
        return buildings

    def csv_construnction_interface(self, buildings, length):
        construnction_dict = {"name": [],
                        "construnction": []}
        for i in range(length):
            if "start_date" in buildings[i]["tags"]:
                pass
            else:
                construnction_dict["name"].append(buildings[i]["Name"])
                construnction_dict["construnction"].append("NONE")
        dataframe = pd.DataFrame.from_dict(construnction_dict)
        dataframe.to_csv("Files/G_CSV/building_construnction.csv") 
        user_input = Notification.building_csv_interface(self)
        if user_input == "1":
            construnction = pd.read_csv("Files/G_CSV/building_construnction.csv", index_col = 0)
            for j in range(len(construnction)):
                buildings[j]["tags"]["start_date"] = construnction["construnction"].loc[j]
        return buildings               

    def random_assign_construnction_interface(self, buildings, length):
       for i in range(length):
           if "start_date" in buildings[i]["tags"]:
               pass
           else:
               construnction = random.randint(1920, 2010)
               buildings[i]["tags"]["start_date"] = construnction
       return buildings     

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
   
    # Checkthe construction year and assign a construction standard
    def construnction_type(self, selected_buildings, length):
        for j in range(length):
            if selected_buildings[j]["tags"]["start_date"] in range(1000, 1921):
                selected_buildings[j]["tags"]["Construction_standard"] = "STANDARD1"
                
            elif selected_buildings[j]["tags"]["start_date"] in range(1920, 1971):
                selected_buildings[j]["tags"]["Construction_standard"] = "STANDARD2"
        
            elif selected_buildings[j]["tags"]["start_date"] in range(1971, 1980):
                selected_buildings[j]["tags"]["Construction_standard"] = "STANDARD3"
        
            elif selected_buildings[j]["tags"]["start_date"] in range(1981, 2000):
                selected_buildings[j]["tags"]["Construction_standard"] = "STANDARD4"
        
            elif selected_buildings[j]["tags"]["start_date"] in range(2000, 2040):
                selected_buildings[j]["tags"]["Construction_standard"] = "STANDARD5"
            else:
                standard = ["STANDARD1", "STANDARD2", "STANDARD3", "STANDARD4", "STANDARD5"]
                random_standard = random.choice(standard)
                selected_buildings[j]["tags"]["Construction_standard"] = random_standard
        return selected_buildings

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#

    # Assign HVAC specifications based on building category
    def HVAC_type(self, selected_buildings, length):
        dbf = DBF('Files/I_DBF_Files/air_conditioning.dbf')
        dbf = pd.DataFrame(dbf)
        col = dbf.columns
        residential_AirCondition = []
        non_residential_AirCondition = []
        
        for j in range(len(col)):
            non_residential_AirCondition.append({col[j] :dbf.loc[:,col[j]].to_dict()})

        for k in range(len(col)):
            residential_AirCondition.append({col[k] : " "})
 
        for i in range(length):
            if selected_buildings[i]["tags"]["building"] == "residential":
                selected_buildings[i]["tags"]["air_condition"] = residential_AirCondition
            else:
                selected_buildings[i]["tags"]["air_condition"] = non_residential_AirCondition
                
        return selected_buildings

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#

    # Assign supply system specifications based on building category
    def Supply_type(self, selected_buildings, length):
        dbf = DBF('Files/I_DBF_Files/supply_systems.dbf')
        dbf = pd.DataFrame(dbf)
        col = dbf.columns 
        residential_supply_system = []
        non_residential_supply_system = []
        for j in range(len(col)):
            non_residential_supply_system.append({col[j] :dbf.loc[:,col[j]].to_dict()})
            
        for k in range(len(col)):
            residential_supply_system.append({col[k] : " "})
        
        for i in range(length):
            if selected_buildings[i]["tags"]["building"] == "residential":
                selected_buildings[i]["tags"]["supply_system"] = residential_supply_system
            else:
                selected_buildings[i]["tags"]["supply_system"] = non_residential_supply_system
        return selected_buildings
