import pandas as pd
import folium 

df = pd.read_csv("./country_data.csv")    # """dataset para conseguir la localizacion (latitud y longitud) de los paises"""
df2 = pd.read_csv("./world.csv")    #dataset que queremos analizar(paises ordenados por indice de felicidad)


paises = []
for x in df.name:
    paises.append(x)

latitudes = []
for l in df.latitude:
    latitudes.append(l)

longitud = []
for lon in df.longitude:
    longitud.append(lon)

def latitud(nombre):
    for n in paises:                  #funcion para conseguir la latitud de un pais por su nombre
        if n == nombre:
            a = paises.index(n)
            return latitudes[a]


def longitudee(cosa):
    for x in paises:
        if x == cosa:                          #funcion para sacar la longitud al ingresar el nombre
            b = paises.index(x)
            return longitud[b]

paises_lista= []
for p in df2["Country (region)"]:
    paises_lista.append(p)

paises_up = paises_lista[:10]           #lista de los 10 paises más felices del mundo por orden
paises_up   

def mapa2(nombre):  #Hago el zoom mas pequeño para que se vea todo el mundo
    lat = latitud(nombre)
    lon = longitudee(nombre)
    map = folium.Map(location=[lat, lon], zoom_start=2)
    return map