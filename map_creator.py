#map creation

print("LOADING...")

import os.path
import folium
import pandas as pd
import numpy as np
from folium.plugins import HeatMap

path = "../11_robo"
file = "DB_robos.xlsx"
hoja = "db"

joined_path = os.path.join(path, file)
df = pd.read_excel(joined_path,sheet_name=hoja)

coordenadas = df[["Longitud","Latitud"]]

mapObj = folium.Map([19.52397, -98.99856],zoom_start=10)

HeatMap(coordenadas).add_to(mapObj)

mapObj.save(os.path.join(path,"mapa_robos.html"))

mapObj