# Importacion del archivo
import pandas as pd


df = pd.read_excel("Usuario y Grupos FCL.xlsx", sheet_name = "ARGENTINA")

print(df.head())


