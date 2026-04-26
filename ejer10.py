import pandas as pd
import numpy as np


datos= {
    "nombre": ["Ana", "Luis", "Maria", "Carlos"],
    "edad": [25, 30, 22, 28],
    "ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"],
    "calificaciones":[[10,9,8],[9,9,9],[7,8,6],[8,7,7]],
    "materias": ["matematicas", "ciencias", "historia", "lenguaje"]
}
df= pd.DataFrame(datos)
print(df.info())
print(df.describe())
print(df)
