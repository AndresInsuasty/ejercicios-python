import pandas as pd

df = pd.read_json("data/recetas.json")

receta_ligera = df.loc[df["calorias"].idxmin()]

print(f"La receta más ligera es '{receta_ligera['nombre']}' con {receta_ligera['calorias']} calorías.")
