import pandas as pd

with open("data/gastos_mensuales.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

lineas = contenido.split("\n")

gastos_por_categoria = {}
categoria_actual = None

for linea in lineas:
    linea = linea.strip()
    
    if linea.startswith("CATEGORÍA:"):
        categoria_actual = linea.replace("CATEGORÍA: ", "")
        gastos_por_categoria[categoria_actual] = 0
    
    elif linea and ":" in linea and categoria_actual:
        partes = linea.split(":")
        if len(partes) == 2:
            try:
                gasto = float(partes[1].replace("€", "").strip())
                gastos_por_categoria[categoria_actual] += gasto
            except ValueError:
                pass

df = pd.DataFrame(list(gastos_por_categoria.items()), columns=["categoria", "gasto"])
categoria_mayor = df.loc[df["gasto"].idxmax(), "categoria"]
gasto_mayor = df["gasto"].max()

print(f"La categoría con mayor gasto es '{categoria_mayor}' con {gasto_mayor:.2f}€")
