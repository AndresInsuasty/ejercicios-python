# Ejercicios de Python

## 📚 Parte 1: Ejercicios Básicos (Muy Fáciles)

Estos ejercicios son **sin datos externos**. Solo necesitas escribir código simple en la terminal.

---

### **Ejercicio 1: Hola Mundo**

Escribe un programa que muestre el mensaje "¡Hola, mundo!" en la pantalla.

**Esperado:**
```
¡Hola, mundo!
```

**Solución:** [soluciones/01_hola_mundo.py](soluciones/01_hola_mundo.py)

---

### **Ejercicio 2: Suma de dos números**

Escribe un programa que sume dos números (3 + 5) y muestre el resultado.

**Pista:** Usa la variable para guardar los números, luego suma ellos.

**Esperado:**
```
La suma de 3 + 5 es: 8
```

**Solución:** [soluciones/02_suma_numeros.py](soluciones/02_suma_numeros.py)

---

### **Ejercicio 3: Tu nombre**

Escribe un programa que pida tu nombre y luego salude con un mensaje personalizado.

**Pista:** Usa `input()` para pedir el nombre al usuario.

**Esperado:**
```
¿Cuál es tu nombre? María
¡Hola María! Bienvenida a Python.
```

**Solución:** [soluciones/03_saludar_persona.py](soluciones/03_saludar_persona.py)

---

### **Ejercicio 4: Tabla de multiplicar**

Escribe un programa que muestre la tabla de multiplicar del 5 (del 1 al 10).

**Pista:** Usa un bucle `for` para repetir 10 veces.

**Esperado:**
```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

**Solución:** [soluciones/04_tabla_multiplicar.py](soluciones/04_tabla_multiplicar.py)

---

### **Ejercicio 5: Contar vocales**

Escribe un programa que cuente cuántas vocales (a, e, i, o, u) tiene la palabra "python".

**Pista:** Usa un bucle para revisar cada letra de la palabra.

**Esperado:**
```
La palabra "python" tiene 1 vocal(es).
```

**Solución:** [soluciones/05_contar_vocales.py](soluciones/05_contar_vocales.py)

---

## 🔍 Parte 2: Ejercicios con Datos (10 Ejercicios)

En esta sección usaremos **datos reales guardados en archivos** (`data/`). Cada ejercicio responde una pregunta cotidiana usando esos datos.

---

### **Ejercicio 6: Compras - ¿Cuál fue el gasto total?**

**Pregunta:** Tienes una lista de todas tus compras de la semana en un archivo. ¿Cuánto dinero gastaste en total?

**Archivo de datos:** [data/compras_semana.csv](data/compras_semana.csv)

**Qué debes hacer:**
1. Lee el archivo CSV
2. Calcula la cantidad de dinero gastado en cada producto (precio × cantidad)
3. Suma todos los gastos
4. Muestra el total

**Esperado:**
```
Gasto total de la semana: 48.70€
```

**Solución:** [soluciones/06_gasto_total_compras.py](soluciones/06_gasto_total_compras.py)

---

### **Ejercicio 7: Recetas - ¿Cuál es la receta más rápida?**

**Pregunta:** Tienes 5 recetas guardadas. ¿Cuál puedes preparar en menos tiempo?

**Archivo de datos:** [data/recetas.json](data/recetas.json)

**Qué debes hacer:**
1. Lee el archivo JSON
2. Busca la receta con el menor tiempo de preparación
3. Muestra el nombre y cuántos minutos toma

**Esperado:**
```
La receta más rápida es 'Ensalada César' en 15 minutos.
```

**Solución:** [soluciones/07_receta_rapida.py](soluciones/07_receta_rapida.py)

---

### **Ejercicio 8: Deportes - ¿Cuántas calorías quemaste en el mes?**

**Pregunta:** Tienes un registro de todas tus actividades deportivas del mes. ¿Cuántas calorías quemaste en total?

**Archivo de datos:** [data/deportes_mes.csv](data/deportes_mes.csv)

**Qué debes hacer:**
1. Lee el archivo CSV
2. Suma todas las calorías quemadas
3. Muestra el total

**Esperado:**
```
Calorías quemadas en febrero: 3710 kcal
```

**Solución:** [soluciones/08_calorias_quemadas.py](soluciones/08_calorias_quemadas.py)

---

### **Ejercicio 9: Películas - ¿Cuál es la película mejor calificada?**

**Pregunta:** Tienes una lista de tus películas favoritas con puntuaciones. ¿Cuál es la mejor?

**Archivo de datos:** [data/peliculas_favoritas.json](data/peliculas_favoritas.json)

**Qué debes hacer:**
1. Lee el archivo JSON
2. Encuentra la película con la puntuación más alta
3. Muestra el título y su puntuación

**Esperado:**
```
La película mejor calificada es 'El viaje de Chihiro' con 8.9 puntos.
```

**Solución:** [soluciones/09_pelicula_mejor_rated.py](soluciones/09_pelicula_mejor_rated.py)

---

### **Ejercicio 10: Supermercado - ¿Cuanto ahoraste con descuentos?**

**Pregunta:** Tienes un registro de compras con algunos descuentos. ¿Cuánto dinero ahorraste gracias a ellos?

**Archivo de datos:** [data/supermercado_gastos.csv](data/supermercado_gastos.csv)

**Qué debes hacer:**
1. Lee el archivo CSV
2. Calcula cuánto dinero fue descuento en cada compra (precio × cantidad × descuento / 100)
3. Suma todos los ahorros
4. Muestra el total de dinero ahorrado

**Esperado:**
```
Dinero ahorrado con descuentos: 4.70€
```

**Solución:** [soluciones/10_ahorros_descuentos.py](soluciones/10_ahorros_descuentos.py)

---

### **Ejercicio 11: Recetas - ¿Cuál es la receta con menos calorías?**

**Pregunta:** De todas tus recetas, ¿cuál es la más ligera (menos calorías)?

**Archivo de datos:** [data/recetas.json](data/recetas.json)

**Qué debes hacer:**
1. Lee el archivo JSON
2. Busca la receta con el menor número de calorías
3. Muestra el nombre y cuántas calorías tiene

**Esperado:**
```
La receta más ligera es 'Sopa de verduras' con 150 calorías.
```

**Solución:** [soluciones/11_receta_luz.py](soluciones/11_receta_luz.py)

---

### **Ejercicio 12: Compras - ¿Cuál es la categoría que más costo tiene?**

**Pregunta:** Tienes un registro de todas tus compras organizadas por categoría. ¿En cuál categoría gastaste más dinero?

**Archivo de datos:** [data/compras_semana.csv](data/compras_semana.csv)

**Qué debes hacer:**
1. Lee el archivo CSV
2. Agrupa por categoría y suma el gasto total de cada una (precio × cantidad)
3. Encuentra cuál tiene el mayor gasto
4. Muestra la categoría y su gasto total

**Esperado:**
```
La categoría con mayor gasto es 'proteínas' con 9.50€
```

**Solución:** [soluciones/12_categoria_mayor_gasto.py](soluciones/12_categoria_mayor_gasto.py)

---

### **Ejercicio 13: Deportes - ¿Cuál fue tu distancia total recorrida?**

**Pregunta:** Tienes un registro de tus actividades deportivas con las distancias. ¿Cuántos kilómetros recorriste en total en febrero?

**Archivo de datos:** [data/deportes_mes.csv](data/deportes_mes.csv)

**Qué debes hacer:**
1. Lee el archivo CSV
2. Suma todas las distancias recorridas
3. Muestra el total en kilómetros

**Esperado:**
```
Distancia total recorrida en febrero: 75.5 km
```

**Solución:** [soluciones/13_distancia_total.py](soluciones/13_distancia_total.py)

---

### **Ejercicio 14: Libros - ¿Cuántos libros has leído?**

**Pregunta:** Tienes una bibioteca de libros. ¿Cuántos ya leíste?

**Archivo de datos:** [data/libros_biblioteca.json](data/libros_biblioteca.json)

**Qué debes hacer:**
1. Lee el archivo JSON
2. Cuenta cuántos libros tienen `"leido": true`
3. Muestra el número de libros leídos y el total

**Esperado:**
```
Has leído 3 de 6 libros en tu biblioteca.
```

**Solución:** [soluciones/14_libros_leidos.py](soluciones/14_libros_leidos.py)

---

### **Ejercicio 15: Deportes - ¿Cuál fue tu actividad favorita?**

**Pregunta:** Según tus registros de actividades, ¿cuál tipo de deporte hacías más?

**Archivo de datos:** [data/deportes_mes.csv](data/deportes_mes.csv)

**Qué debes hacer:**
1. Lee el archivo CSV
2. Cuenta cuántas veces hiciste cada tipo de actividad (Correr, Ciclismo, Natación, etc.)
3. Encuentra la que más repetiste
4. Muestra el nombre y cuántas veces la hiciste

**Esperado:**
```
Tu actividad favorita es 'Correr', la hiciste 5 veces en febrero.
```

**Solución:** [soluciones/15_actividad_favorita.py](soluciones/15_actividad_favorita.py)

---

## 🎯 Cómo empezar

### Instalación inicial
```bash
uv sync
```

1. **Básicos:** Ejecuta los ejercicios 1-5 directamente
   ```bash
   uv run soluciones/01_hola_mundo.py
   ```

2. **Con datos:** Primero revisa el archivo de datos, luego intenta resolver el ejercicio
   ```bash
   cat data/compras_semana.csv
   uv run soluciones/06_gasto_total_compras.py
   ```

3. **Consulta soluciones:** Si te atascas, puedes ver cómo se resuelve abriendo el archivo de solución
