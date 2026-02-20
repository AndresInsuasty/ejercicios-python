import pandas as pd

df = pd.read_sql(
    "SELECT nombre, modelo, precio, stock FROM bicicletas",
    "sqlite:///data/bicicletas_tienda.db",
)

print("=== INVENTARIO DE BICICLETAS ===\n")
for _, fila in df.iterrows():
    print(f"• {fila['nombre']} ({fila['modelo']})")
    print(f"  Precio: {fila['precio']:.2f}€ | Stock: {fila['stock']} unidades\n")
