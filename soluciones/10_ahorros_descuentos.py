import pandas as pd

df = pd.read_csv("data/supermercado_gastos.csv")

df["ahorro"] = (df["precio_unitario"] * df["cantidad"] * df["descuento"]) / 100
total_ahorrado = df["ahorro"].sum()

print(f"Dinero ahorrado con descuentos: {total_ahorrado:.2f}€")
