from funciones import latitud
from funciones import longitudee
import folium
import pandas as pd 
from funciones import mapa2

df2 = pd.read_csv("./world.csv")

paises_lista= []
for p in df2["Country (region)"]:
    paises_lista.append(p)

paises_up = paises_lista[:10]
paises_up  

mi_mapa = mapa2("Spain")
# aádimos los 10 paises mas felices

Finland = folium.Marker(location=(latitud("Finland"), longitudee("Finland")))
Denmark = folium.Marker(location=(latitud("Denmark"), longitudee("Denmark")))
Norway = folium.Marker(location=(latitud("Norway"), longitudee("Norway")))
Iceland = folium.Marker(location=(latitud("Iceland"), longitudee("Iceland")))
Netherlands = folium.Marker(location=(latitud("Netherlands"), longitudee("Netherlands")))
Switzerland = folium.Marker(location=(latitud("Switzerland"), longitudee("Switzerland")))
Sweden = folium.Marker(location=(latitud("Sweden"), longitudee("Sweden")))
New_Zealand = folium.Marker(location=(latitud("New Zealand"), longitudee("New Zealand")))
Canada = folium.Marker(location=(latitud("Canada"), longitudee("Canada")))
Austria = folium.Marker(location=(latitud("Austria"), longitudee("Austria")))

Finland.add_to(mi_mapa)
Denmark.add_to(mi_mapa)
Norway.add_to(mi_mapa)
Iceland.add_to(mi_mapa)
Netherlands.add_to(mi_mapa)                    #este mapa representa el top 10 de paises más felices del mundo, como podemos comprobar se situan 
                                                # en los extremos de los polos (o muy al norte o muy al sur)
Switzerland.add_to(mi_mapa)
Sweden.add_to(mi_mapa)
New_Zealand.add_to(mi_mapa)
Canada.add_to(mi_mapa)
Austria.add_to(mi_mapa)
print ("hola")       