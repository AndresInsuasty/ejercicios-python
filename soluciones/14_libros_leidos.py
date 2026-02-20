import pandas as pd

df = pd.read_json("data/libros_biblioteca.json")

libros_leidos = df["leido"].sum()
total_libros = len(df)

print(f"Has leído {int(libros_leidos)} de {total_libros} libros en tu biblioteca.")
