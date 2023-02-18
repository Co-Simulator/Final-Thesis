import os
import random
import geojson
# import rasterio
import geopandas
import shapefile
import googlemaps
import pandas as pd
import lxml.etree as ET
from geojson import dumps


class Notification():
    
    def select_building(self):
        ask_number = int(input("How many buildings you want to select: "))
        return ask_number
    
    def ID_notif(self):
        print("   ")
        print("New IDs has been assigned to the selected buildings")

    def name_notif(self):
        print("   ")
        print("New names has been assigned to the selected buildings")

    def type_notif(self):
        print("   ")
        print("Polygon type has been assigned to the selected buildings")
    
    def building_height_interface(self):
        print("   ")
        print("Choose one of below interfaces to continue the process:")
        print("   ")
        user_input = input ("1_Pythonic interface.\n2_EXCEL file.\n3_CSV file.\n4_GeoSpatial\n5_Random assignment\n6_Skip and continue.\n7_Restart the process.\nType your answer:  ")  
        return user_input
        
    def building_excel_interface(self):
        print("An excel file has been created")
        user_input = input("When the file is filled, press '1' to continue: ")
        return user_input

    def building_csv_interface(self):
        print("A csv file has been created")
        user_input = input("When the file is filled, press '1' to continue: ")
        return user_input

    def building_category_interface(self):
        print("   ")
        print("Choose one of below interfaces to continue the process:")
        print("   ")
        user_input = input ("1_Pythonic interface.\n2_EXCEL file.\n3_CSV file.\n4_Google Places API\n5_Random assignment\n6_Skip and continue.\n7_Restart the process.\nType your answer:  ")  
        return user_input
    
    def building_category_API(self):
        residential_types = ["residenziale", "abitativa", "residenziale e commerciale", "residenziale e produttivo", "residential", "multi residential, multi-residential", "locality", "neighborhood"]
        return residential_types

    def building_floor_interface(self):
        print("   ")
        print("Choose one of below interfaces to continue the process:")
        print("   ")
        user_input = input ("1_Pythonic interface.\n2_EXCEL file.\n3_CSV file.\n4_Calculation based on height\n5_Random assignment\n6_Skip and continue.\n7_Restart the process.\nType your answer:  ")  
        return user_input

    def building_surface_interface(self):
        print("   ")
        print("Choose one of below interfaces to continue the process:")
        print("   ")
        user_input = input ("1_Pythonic interface.\n2_EXCEL file.\n3_CSV file.\n4_Random assignment\n5_Skip and continue.\n6_Restart the process.\nType your answer:  ")  
        return user_input

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

    def Converted_SHP_reader(self):
        for file_name in os.listdir("Files\B_Converted SHP to Geojson"):
            if file_name.endswith(".geojson"):
                Geo_file = file_name
        input_directory = os.path.dirname(os.path.realpath('__file__'))
        with open(os.path.join(input_directory, 'Files/B_Converted SHP to Geojson/' + Geo_file)) as File:
            converted_file = geojson.load(File)
        return converted_file

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
   

    def CityGML_creator(self, buildings, length):
        residential = ["residenziale", "residenziale e commerciale", "residential", "abitativa"]
        category = []
        lat = []
        lon = []
        height = []
        name = []
        floors = []
        area = []
        construction = []
        for i in range(length):
            lat_building = []
            lon_building = []
            name.append(buildings[i]["properties"]["NOME"])
            height.append(buildings[i]["properties"]["ALTEZZA_VO"]) 
            floors.append(buildings[i]["properties"]["NUM_PIANI"]) 
            construction.append(buildings[i]["properties"]["EPOCA"])
            if buildings[i]["properties"]["EDIFC_USO"] in residential:
                category.append("residential")
            else:
                category.append("non-residential")
            area.append(buildings[i]["properties"]["SUPERFICIE"]) 
            for b in range(len(buildings[i]["geometry"]["coordinates"][0])):
                for c in range(1):
                    lat_building.append(buildings[i]["geometry"]["coordinates"][0][b][0]) 
                    lon_building.append(buildings[i]["geometry"]["coordinates"][0][b][1])
            lat.append(lat_building) 
            lon.append(lon_building)

        geo_data = pd.DataFrame()            
        geo_data.insert(0,"name", name)
        geo_data.insert(1,"lat", lat)
        geo_data.insert(2,"lon", lon)
        geo_data.insert(3,"height", height)
        geo_data.insert(4,"floors", floors)
        geo_data.insert(5,"category", category)
        geo_data.insert(6,"area", area)
        geo_data.insert(7,"construction_year", construction)




        citygml = ET.Element("{http://www.opengis.net/citygml/3.0}CityModel", nsmap={None: "http://www.opengis.net/citygml/3.0"})
        
        for _, row in geo_data.iterrows():
            building = ET.SubElement(citygml, "{http://www.opengis.net/citygml/3.0}building")
            name = ET.SubElement(building, "{http://www.opengis.net/citygml/3.0}name")
            name.text = row["name"]
            
            lon = ET.SubElement(building, "{http://www.opengis.net/citygml/3.0}longitude")
            lon.text = str(row["lon"])
            
            lat = ET.SubElement(building, "{http://www.opengis.net/citygml/3.0}latitude")
            lat.text = str(row["lat"])
            
            height = ET.SubElement(building, "{http://www.opengis.net/citygml/3.0}height")
            height.text = str(row["height"])
        
            floors = ET.SubElement(building, "{http://www.opengis.net/citygml/3.0}floors")
            floors.text = str(row["floors"])
            
            category = ET.SubElement(building, "{http://www.opengis.net/citygml/3.0}category")
            category.text = str(row["category"])
            
            area = ET.SubElement(building, "{http://www.opengis.net/citygml/3.0}area")
            area.text = str(row["area"])
            
            construction = ET.SubElement(building, "{http://www.opengis.net/citygml/3.0}construction_year")
            construction.text = str(row["construction_year"])
        
        tree = ET.ElementTree(citygml)
        tree.write("Files/H_CityGML/buildings.xml", xml_declaration=True, encoding='UTF-8', pretty_print=True)
    

    
    
    
    


#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#


          
           
# if __name__ == "__main__":
#     Main_Analysis = Analyzer()
#     Main_Analysis.height_analysis()