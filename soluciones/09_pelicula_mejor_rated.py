import pandas as pd

df = pd.read_json("data/peliculas_favoritas.json")

pelicula_mejor = df.loc[df["puntuacion"].idxmax()]

print(f"La película mejor calificada es '{pelicula_mejor['titulo']}' con {pelicula_mejor['puntuacion']} puntos.")
