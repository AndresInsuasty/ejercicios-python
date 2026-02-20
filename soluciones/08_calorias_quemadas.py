import pandas as pd

df = pd.read_csv("data/deportes_mes.csv")

total_calorias = df["calorias_quemadas"].sum()

print(f"Calorías quemadas en febrero: {int(total_calorias)} kcal")
