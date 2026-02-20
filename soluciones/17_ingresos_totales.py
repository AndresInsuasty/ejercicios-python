import pandas as pd

df = pd.read_sql("""
    SELECT 
        SUM(cantidad * precio_unitario) as ingresos_totales
    FROM ventas
""", "sqlite:///data/bicicletas_tienda.db")

ingresos = df['ingresos_totales'][0]

print(f"💰 Ingresos totales por ventas: {ingresos:.2f}€")
