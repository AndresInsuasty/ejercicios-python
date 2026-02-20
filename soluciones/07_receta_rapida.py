import pandas as pd

df = pd.read_json("data/recetas.json")

receta_rapida = df.loc[df["tiempo_minutos"].idxmin()]

print(f"La receta más rápida es '{receta_rapida['nombre']}' en {receta_rapida['tiempo_minutos']} minutos.")
