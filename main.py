import pandas as pd 
import requests 
import json
import funciones
import folium
from funciones import latitud
from funciones import longitudee


def mapa(pais):
    lat = latitud(pais)
    lon = longitudee(pais)                                      #funcion que devulve el mapa del pais 
    map = folium.Map(location=[lat, lon], zoom_start=6)
    return map

def mapa2(nombre):  #Hago el zoom mas pequeño para que se vea todo el mundo
    lat = latitud(nombre)
    lon = longitudee(nombre)
    map = folium.Map(location=[lat, lon], zoom_start=2)
    return map
