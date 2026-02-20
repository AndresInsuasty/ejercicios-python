import pandas as pd

with open("data/tareas_dia.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

lineas = contenido.split("\n")

en_lunes = False
contador_tareas = 0

for linea in lineas:
    if linea.strip() == "Lunes":
        en_lunes = True
        continue
    
    if en_lunes:
        if linea.strip() and linea.strip()[0].isupper() and " - " not in linea:
            break
        
        if linea.strip() and " - " in linea:
            contador_tareas += 1

print(f"El lunes tienes {contador_tareas} tareas programadas.")
