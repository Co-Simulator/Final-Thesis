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
		if (len(uri) > 0 and uri[0] == "coordinates"):
			#Collected coordinates from the Interface
			coordinates = str(params)
            
            # Still have a problem with format of passing a polygon to the API but the test version works
			xmin, ymin, xmax, ymax = 7.67889, 45.06820, 7.68525, 45.07073
			overpass_url = "http://overpass-api.de/api/interpreter"
			overpass_query = f"""
                [out:json];
                (
                  way["building"]({ymin},{xmin},{ymax},{xmax});
                  rel["building"]({ymin},{xmin},{ymax},{xmax});
                );
                out body geom;
            """
			response = requests.get(overpass_url, params={"data": overpass_query})
			data = response.json()
			features = data['elements']             
			output_file = 'Downloaded_Data.geojson'
			geojson = {
                "type": "FeatureCollection",
			    "features": features
            }
			with open(output_file, 'w') as f:
                         json.dump(geojson, f)
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
