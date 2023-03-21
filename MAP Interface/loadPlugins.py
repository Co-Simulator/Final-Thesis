import cherrypy
import os
import requests
import json

class Interface(object):
	"""docstring for Reverser"""
	exposed=True
	def __init__(self):
		self.id=1
	def GET(self, *uri, **params):
		if (len(uri) > 0 and uri[0] == 'coordinates'):
 			coordinates = str(params["coordinates"])
 			pairs = coordinates.split(',')
 			poly = ' '.join(pairs)
 			overpass_url = "http://overpass-api.de/api/interpreter"
 			overpass_query = f"""
            [out:json];
            (
              way["building"](poly:"{poly}");
              node(w);
            );
            out center;
            """
 			response = requests.post(overpass_url, data=overpass_query)
 			data = json.loads(response.content)
 			buildings = [element for element in data["elements"] if element["type"] == "way" and "tags" in element and element["tags"].get("building")]
 			with open('G:/Final-Project/GeoProcessing/Files/J_Downloaded_Fence/Geo-Fence.geojson', 'w') as f:
                            json.dump(buildings, f)

 			return open('index.html')
		else:
			return open('index.html')


if __name__ == '__main__':
	conf={
		'/':{
				'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
				'tools.staticdir.root': os.path.abspath(os.getcwd()),
			},
		 '/css':{
		 'tools.staticdir.on': True,
		 'tools.staticdir.dir':'./css'
		 },
		 '/js':{
		 'tools.staticdir.on': True,
		 'tools.staticdir.dir':'./js'
		 },
	}		
	cherrypy.tree.mount(Interface(),'/',conf)
	cherrypy.engine.start()
	cherrypy.engine.block()