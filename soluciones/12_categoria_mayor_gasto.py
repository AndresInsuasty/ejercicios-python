import pandas as pd

df = pd.read_csv("data/compras_semana.csv")

df["gasto_categoria"] = df["precio"] * df["cantidad"]
gasto_por_categoria = df.groupby("categoria")["gasto_categoria"].sum()
categoria_mayor = gasto_por_categoria.idxmax()
gasto_mayor = gasto_por_categoria.max()

print(f"La categoría con mayor gasto es '{categoria_mayor}' con {gasto_mayor:.2f}€")
