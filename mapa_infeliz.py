import folium
from funciones import latitud
from funciones import longitudee
import pandas as pd 
from funciones import mapa2

df2 = pd.read_csv("./world.csv")

paises_lista= []
for p in df2["Country (region)"]:
    paises_lista.append(p)

paises_infeliz= paises_lista[len(paises_lista)-10:len(paises_lista)]
paises_infeliz

mapa_infeliz= mapa2("Spain")

# aádimos los 10 paises mas infelices

Haiti = folium.Marker(location=(latitud("Haiti"), longitudee("Haiti")))
Botswana = folium.Marker(location=(latitud("Botswana"), longitudee("Botswana")))
Syria = folium.Marker(location=(latitud("Syria"), longitudee("Syria")))
Malawi = folium.Marker(location=(latitud("Malawi"), longitudee("Malawi")))
Yemen = folium.Marker(location=(latitud("Yemen"), longitudee("Yemen")))
Rwanda = folium.Marker(location=(latitud("Rwanda"), longitudee("Rwanda")))
Tanzania = folium.Marker(location=(latitud("Tanzania"), longitudee("Tanzania")))
Afghanistan = folium.Marker(location=(latitud("Afghanistan"), longitudee("Afghanistan")))
Central_African_Republic = folium.Marker(location=(latitud("Central African Republic"), longitudee("Central African Republic")))
South_Sudan = folium.Marker(location=(latitud("Sudan"), longitudee("Sudan")))

Haiti.add_to(mapa_infeliz)
Botswana.add_to(mapa_infeliz)
Syria.add_to(mapa_infeliz)
Malawi.add_to(mapa_infeliz)
Yemen.add_to(mapa_infeliz)
Rwanda.add_to(mapa_infeliz)
Tanzania.add_to(mapa_infeliz)
Afghanistan.add_to(mapa_infeliz)
Central_African_Republic.add_to(mapa_infeliz)
South_Sudan.add_to(mapa_infeliz)
mapa_infeliz      