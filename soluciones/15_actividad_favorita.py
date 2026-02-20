import pandas as pd

df = pd.read_csv("data/deportes_mes.csv")

conteos = df["tipo_actividad"].value_counts()
actividad_favorita = conteos.idxmax()
cantidad = conteos.max()

print(f"Tu actividad favorita es '{actividad_favorita}', la hiciste {cantidad} veces en febrero.")
