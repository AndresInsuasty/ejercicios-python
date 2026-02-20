import pandas as pd

df = pd.read_sql("""
    SELECT 
        c.nombre as cliente,
        b.nombre as bicicleta,
        v.cantidad,
        v.precio_unitario,
        v.fecha_compra
    FROM ventas v
    JOIN clientes c ON v.cliente_id = c.id
    JOIN bicicletas b ON v.bicicleta_id = b.id
    ORDER BY v.fecha_compra DESC
""", "sqlite:///data/bicicletas_tienda.db")

print("=== HISTORIAL DE VENTAS ===\n")
for _, fila in df.iterrows():
    total = fila['cantidad'] * fila['precio_unitario']
    print(f"Fecha: {fila['fecha_compra']}")
    print(f"  Cliente: {fila['cliente']}")
    print(f"  Bicicleta: {fila['bicicleta']}")
    print(f"  Cantidad: {fila['cantidad']} × {fila['precio_unitario']:.2f}€ = {total:.2f}€\n")
