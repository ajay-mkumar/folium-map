import folium
import pandas
data=pandas.read_csv("che.txt")
lat=list(data["LATU"])
lon=list(data["LONN"])
nam=list(data["NAME"])
cas=list(data["CASE"])

def color_producer(case):
    if case < 1000:
        return 'green'
    elif 1000 <= case < 4000:
        return 'orange'
    else:
        return 'red'


map=folium.Map(location=[13.067439,80.237617],zoom_start=6,tile="Stamen Terain")
fg=folium.FeatureGroup(name="my map")

for l,o,n,c in zip(lat,lon,nam,cas):
	fg.add_child(folium.Marker(location=[l,o],popup=n+"\n"+str(c),icon=folium.Icon(color=color_producer(c)),fill=True, fill_opacity=0.7))


map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("mymap.html")