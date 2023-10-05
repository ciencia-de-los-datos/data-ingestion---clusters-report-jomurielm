"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():

    df =  pd.read_fwf("clusters_report.txt", widths = [9, 16, 16, 80],header=None,
                    names = ["cluster","cantidad_de_palabras_clave","porcentaje_de_palabras_clave", "principales_palabras_clave"],
                    converters = {"porcentaje_de_palabras_clave": lambda x: x.rstrip(" %").replace(",",".")}
                    ).drop(index={0,1,2}).ffill()

    df = df.astype  ({ "cluster": int, 
                    "cantidad_de_palabras_clave": int, 
                    "porcentaje_de_palabras_clave": float,
                    "principales_palabras_clave": str
                    })

    df = df.groupby(["cluster","cantidad_de_palabras_clave","porcentaje_de_palabras_clave"])["principales_palabras_clave"].apply(lambda x: ' '.join(map(str,x))).reset_index()
    df["porcentaje_de_palabras_clave"] = df["porcentaje_de_palabras_clave"].apply(lambda x: round(x,1))
    df["principales_palabras_clave"] = df["principales_palabras_clave"].apply(lambda x: re.sub(r'\s+', ' ',x).rstrip("."))
    
    return df
