from geopy.geocoders import GoogleV3
import gmplot

#need way to secretly keep API keys in script
geocode_API_key = "[omitted]"
javascript_API_key = "[omitted]"

geo = GoogleV3(api_key = geocode_API_key)


days_of_week = ['MON','TUE','WED','THU','FRI','SAT','SUN']

color = {"MON": "#FF0000", #Red
        "TUE": "#008000",  #Green
        "WED": "#0000FF",  #Blue
        "THU": "#FF00FF",  #Fuschia
        "FRI": "#FFFF00",  #Yellow
        "SAT": "#00FFFF",  #aqua
        "SUN": "#808080",  #grey            
        }  

def geocode(address):
    try:
        code = geo.geocode(address)
        print("geocoded: %s, %s" % (code.latitude, code.longitude))
        return code.latitude, code.longitude
    except Exception, e:
        print(e)
        print("geocode failed")
        return None, None

def scatterPlot_and_writeHTML(day,lat_list,lon_list):
    try:
        gmap = gmplot.GoogleMapPlotter(lat_list[0],lon_list[0],15,apikey=javascript_API_key)
        gmap.scatter(lat_list,lon_list,color[day], size=6, marker=False)
        file_name = day + "_map.html"
        gmap.draw(file_name)
    except Exception, e:
        print(e)
        print(".html file failed to write")
        print("-"*30)