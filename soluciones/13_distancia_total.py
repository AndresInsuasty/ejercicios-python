import pandas as pd

df = pd.read_csv("data/deportes_mes.csv")

distancia_total = df["distancia_km"].sum()

print(f"Distancia total recorrida en febrero: {distancia_total} km")
