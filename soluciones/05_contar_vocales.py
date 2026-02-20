palabra = "python"
vocales = "aeiouáéíóú"

cantidad_vocales = 0

for letra in palabra:
    if letra.lower() in vocales:
        cantidad_vocales += 1

print(f'La palabra "{palabra}" tiene {cantidad_vocales} vocal(es).')
