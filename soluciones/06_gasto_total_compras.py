import pandas as pd

df = pd.read_csv("data/compras_semana.csv")

df["gasto"] = df["precio"] * df["cantidad"]
gasto_total = df["gasto"].sum()

print(f"Gasto total de la semana: {gasto_total:.2f}€")
