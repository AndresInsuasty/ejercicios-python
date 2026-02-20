# 🐍 Ejercicios de Python

> **Aprende Python resolviendo problemas cotidianos.** Una colección de 18 ejercicios prácticos con datos reales para principiantes sin experiencia técnica previa.

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)](https://pandas.pydata.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3+-lightblue.svg)](https://www.sqlite.org/)
[![UV](https://img.shields.io/badge/Package%20Manager-UV-brightgreen.svg)](https://docs.astral.sh/uv/)

---

## 🎯 ¿Qué es esto?

Este repositorio contiene **18 ejercicios de Python** diseñados para personas que **nunca han programado**. Cada ejercicio:

✅ Resuelve un **problema del mundo real** (compras, recetas, deportes, películas, libros, tienda de bicicletas)  
✅ Usa **datos estructurados** en archivos CSV, JSON y bases de datos SQLite  
✅ Incluye **explicaciones claras** sin jerga técnica  
✅ Tiene una **solución completa** para consultar

---

## 📚 Contenido

### Parte 1: Ejercicios Básicos (5 ejercicios)
Sin dependencias externas. Solo Python puro.

| # | Tema | Concepto | Solución |
|---|------|----------|----------|
| 1 | Hola Mundo | Primera línea de código | [Ver](soluciones/01_hola_mundo.py) |
| 2 | Suma de números | Variables y operaciones | [Ver](soluciones/02_suma_numeros.py) |
| 3 | Saludar persona | Input del usuario | [Ver](soluciones/03_saludar_persona.py) |
| 4 | Tabla de multiplicar | Bucles for | [Ver](soluciones/04_tabla_multiplicar.py) |
| 5 | Contar vocales | Condiciones y bucles | [Ver](soluciones/05_contar_vocales.py) |

### Parte 2: Ejercicios con Datos (10 ejercicios)
Usando **Pandas** para análisis de datos reales.

| # | Tema | Datos | Pregunta | Solución |
|---|------|-------|----------|----------|
| 6 | 🛒 Compras | CSV | ¿Cuál fue el gasto total? | [Ver](soluciones/06_gasto_total_compras.py) |
| 7 | 🍳 Recetas | JSON | ¿Cuál es la receta más rápida? | [Ver](soluciones/07_receta_rapida.py) |
| 8 | 💪 Deportes | CSV | ¿Cuántas calorías quemaste? | [Ver](soluciones/08_calorias_quemadas.py) |
| 9 | 🎬 Películas | JSON | ¿Cuál es la mejor calificada? | [Ver](soluciones/09_pelicula_mejor_rated.py) |
| 10 | 🛍️ Supermercado | CSV | ¿Cuánto ahorraste con descuentos? | [Ver](soluciones/10_ahorros_descuentos.py) |
| 11 | 🍲 Recetas | JSON | ¿Cuál tiene menos calorías? | [Ver](soluciones/11_receta_luz.py) |
| 12 | 🏷️ Compras | CSV | ¿Quién es la categoría más cara? | [Ver](soluciones/12_categoria_mayor_gasto.py) |
| 13 | 🏃 Deportes | CSV | ¿Cuántos km recorriste? | [Ver](soluciones/13_distancia_total.py) |
| 14 | 📚 Libros | JSON | ¿Cuántos libros leíste? | [Ver](soluciones/14_libros_leidos.py) |
| 15 | 🎯 Deportes | CSV | ¿Cuál es tu deporte favorito? | [Ver](soluciones/15_actividad_favorita.py) |

### Parte 3: Ejercicios con SQL (3 ejercicios)
Usando **Pandas + SQLite** para consultas en bases de datos.

| # | Tema | Concepto SQL | Pregunta | Solución |
|---|------|--------------|----------|----------|
| 16 | 🚲 Tienda Bicicletas | SELECT + Pandas | ¿Cuáles son las bicicletas? | [Ver](soluciones/16_listar_bicicletas.py) |
| 17 | 💰 Ingresos | SUM() + Pandas | ¿Cuál es el ingreso total? | [Ver](soluciones/17_ingresos_totales.py) |
| 18 | 📋 Ventas | JOIN + Pandas | ¿Cuál es el historial de ventas? | [Ver](soluciones/18_historial_ventas.py) |

---

## ⚙️ Instalación

### Requisitos
- **Python 3.11+**
- **[UV](https://docs.astral.sh/uv/)** (gestor de paquetes rápido)

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/usuario/ejercicios-python.git
cd ejercicios-python

# 2. Instalar dependencias
uv sync

# 3. Ejecutar un ejercicio
uv run soluciones/01_hola_mundo.py
```

---

## 🚀 Cómo empezar

### Ejercicios básicos (sin dependencias)
```bash
uv run soluciones/01_hola_mundo.py
uv run soluciones/02_suma_numeros.py
uv run soluciones/03_saludar_persona.py
```

### Ejercicios con datos (con Pandas)
```bash
# Primero, revisa los datos
head data/compras_semana.csv

# Luego, ejecuta el ejercicio
uv run soluciones/06_gasto_total_compras.py
```

### Ver una solución completa
```bash
cat soluciones/06_gasto_total_compras.py
```

---

## 📋 Estructura del proyecto

```
ejercicios-python/
├── README.md                    # Este archivo
├── ejercicios.md               # Guía detallada de todos los ejercicios
├── pyproject.toml              # Configuración de dependencias
├── .github/
│   └── copilot-instructions.md # Guía para agentes IA
├── data/                        # Archivos de datos
│   ├── compras_semana.csv
│   ├── deportes_mes.csv
│   ├── recetas.json
│   ├── peliculas_favoritas.json
│   ├── libros_biblioteca.json
│   └── supermercado_gastos.csv
└── soluciones/                  # Código resuelto de cada ejercicio
    ├── 01_hola_mundo.py
    ├── 02_suma_numeros.py
    ├── ... (hasta 15_actividad_favorita.py)
```

---

## 💡 Principios del Proyecto

Este repositorio fue diseñado con estos principios en mente:

### 🎯 **Claridad sobre Optimización**
El código es fácil de leer y entender, no optimizado al máximo.

### 📖 **Sin Jerga Técnica**
Cada concepto se explica como si fuera una receta de cocina.

### 🌍 **Problemas Reales**
Cada ejercicio responde una pregunta cotidiana.

### 📊 **Datos Estructurados**
CSV y JSON: formatos que usarás en la vida real.

### 🐼 **Aprender con Pandas**
Los ejercicios con datos introducen el análisis real.

---

## 📖 Documentación

Para más detalles sobre cada ejercicio, consulta:
- **[ejercicios.md](ejercicios.md)** - Descripción completa de los 15 ejercicios

---

## 🤝 ¿Quieres contribuir?

### Agregar nuevos ejercicios

¡Este proyecto está abierto para crecer! Si tienes una idea para un nuevo ejercicio:

1. **Define el problema cotidiano** ✏️
   - Ejemplo: "¿Cuál es el gasto promedio por categoría?"

2. **Prepara los datos** 📊
   - Crea archivos CSV/JSON en la carpeta `data/`
   - Usa datos sintéticos pero realistas

3. **Escribe la solución** 💻
   - Usa pandas para consistencia
   - Mantén el código simple y legible
   - Incluye un comentario breve

4. **Documenta en ejercicios.md** 📝
   - Describe el ejercicio con claridad
   - Muestra el resultado esperado

5. **Envía un Pull Request** 🚀
   - Describe tu contribución
   - Include ejemplos de ejecución

### Formato para nuevos ejercicios

```python
# soluciones/NN_descripcion_ejercicio.py
import pandas as pd

# Descripción breve de lo que hace
df = pd.read_csv("data/archivo.csv")

# Lógica principal
resultado = df[...].operation()

# Resultado final
print(f"Respuesta: {resultado}")
```

### Sugerencia de ejercicios faltantes

- Análisis de salarios por región
- Presupuesto familiar y gastos mensuales
- Calificaciones de estudiantes
- Inventario de productos
- Registro de temperaturas por mes
- Ventas por trimestre
- Horas de sueño y productividad

---

## 📝 Licencia

Este proyecto está bajo licencia MIT. Eres libre de usar, modificar y distribuir el código.

---

## 👤 Autor

Creado para que **cualquier persona aprenda Python** viendo código que resuelve problemas reales.

---

## 🌟 Reconocimientos

Inspirado en el principio de que **la mejor forma de aprender es haciendo**. Cada ejercicio conecta con la vida diaria para que el aprendizaje sea significativo.

---

**¿Te gustó? ⭐ Dale una estrella en GitHub si este repositorio te ayudó a aprender Python.**