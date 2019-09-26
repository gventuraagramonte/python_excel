# Este programa realiza las siguientes acciones:
# Usa la libreria pandas para trabajar la data que cargamos en el pd read excel
# En la variable lista se deposita los diccionarios requeridos
import pandas as pd

df = pd.read_excel("demosheet.xlsx", header=None).pivot(columns = 0, values = 1)
Lista = {col: df[col].dropna().tolist() for col in df.columns}

print (Lista)