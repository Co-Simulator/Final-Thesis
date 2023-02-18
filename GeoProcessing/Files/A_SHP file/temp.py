import googlemaps
import geojson
from geojson import dumps
import pandas
import geopandas
import shapefile
from shapely import wkt
import shapely
from shapely.geometry import Polygon
from matplotlib import pyplot as plt
from shapely.geometry import Point, Polygon


pol = geopandas.GeoDataFrame.from_file(r"EDIFICIO.shp")
converted_pol = geopandas.GeoDataFrame(pol, crs="EPSG:4326")
bounding_box = converted_pol.envelope
data_frame = geopandas.GeoDataFrame(geopandas.GeoSeries(bounding_box), columns=['geometry'])
coordinate_series = geopandas.GeoSeries(data_frame.iloc[0])
centroid_coordinate = coordinate_series.centroid
coord = []
coord.append(centroid_coordinate.geometry.y[0])
coord.append(centroid_coordinate.geometry.x[0])

lat = str(coord.pop(0))
lon = str(coord.pop(0))

api_key = "AIzaSyAn-V_D0aPmOlPPbjxE8708udXES2cV4-8"
gmaps = googlemaps.Client(key = api_key)
place_result = gmaps.places_nearby(location = (lat ,lon) , radius = 5)

italian_categ = ["commerciale", "residenziale", "servizio pubblico", "industriale"]
english_categ = ["comercial", "residential", "public service", "industrial"]

Categories = []
for categ in range(len(place_result["results"])):
    for types in range(len(place_result["results"][categ]["types"])):
        Categories.append(place_result["results"][categ]["types"][types])



for compare in range(len(Categories)):
    if Categories[compare] in italian_categ or Categories[compare] in english_categ:
        print("Found")
    else:
        print("Not Found")
















Database = {"Name": ["cyrus"]}

username = "maria"

if username in Database["Name"]:
    print("Found")
else:
    print("Not Found")
















# "45.04742097835543, 7.643936524987207"

















# intersections = geopandas.overlay(df, pol, how='intersection')
# plt.ion()
# intersections.plot() 
# print(b.overlay)
# m = b.total_bounds











# df = geopandas.GeoDataFrame(geopandas.GeoSeries(bb_polygon), columns=['geometry'])

# intersections2 = geopandas.overlay(df, pol, how='intersection')











# with open('zone.geojson') as File:
#     Zone_profile = geojson.load(File)

# coord = []

# coordinate = Zone_profile["features"][0]["geometry"]["coordinates"][0]
# for i in range(len(Zone_profile["features"][0]["geometry"]["coordinates"][0])):
#     coord.append(coordinate[i])
#     # coord.append(coordinate[i][1])



# print(b.overlay)
# m = b.total_bounds





# types = []
# for i in range(len(place_result["results"])):
#     place_type = place_result["results"][i]["types"]
#     types.append(place_type)

# for j in range(len(types)):
#     for m in range(len(types[j])):  
#         if "place" in types[j][m] or "residenziale" in types[j][m] or "comercial" in types[j][m] :
#             print("hast")