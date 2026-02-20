# Instrucciones para Agentes de IA

## 🎯 Propósito

Este es un repositorio de **ejercicios prácticos de Python** con **18 ejercicios progresivos**. Cada ejercicio resuelve un problema cotidiano para que sea fácil de entender sin necesidad de conocimientos técnicos previos.

- **Ejercicios 1-5:** Python puro (sin dependencias)
- **Ejercicios 6-15:** Análisis de datos con pandas
- **Ejercicios 16-18:** Consultas SQL con SQLite

## 🔧 Instalación y Ejecución

### Requisitos
- **Python 3.11+**
- **Gestor de paquetes:** `uv` (instalación rápida)

### Primeros pasos
```bash
# Instalar todas las dependencias del proyecto (pandas, sqlalchemy)
uv sync

# Ejecutar un script específico
uv run soluciones/nombre_del_archivo.py

# Ver contenido de datos
cat data/compras_semana.csv
```

## 📊 Estructura del Proyecto

```
ejercicios-python/
├── README.md                           # Guía principal8 ejercicios
├── crear_db.py                         # Script para crear base de datos
├── pyproject.toml                      # Dependencias (pandas)
├── .github/
│   └── copilot-instructions.md         # Este archivo
├── data/                               # Datos sintéticos en CSV, JSON y SQLite
│   ├── compras_semana.csv
│   ├── deportes_mes.csv
│   ├── recetas.json
│   ├── peliculas_favoritas.json
│   ├── libros_biblioteca.json
│   ├── supermercado_gastos.csv
│   └── bicicletas_tienda.db           # Base de datos SQLite (3 tablas)
└── soluciones/                         # Código resuelto (18 archivos)
    ├── 01_hola_mundo.py
    ├── 02_suma_numeros.py
    ├── ...
    ├── 15_actividad_favorita.py
    ├── 16_listar_bicicletas.py        # SQL: SELECT simple
    ├── 17_ingresos_totales.py         # SQL: SUM (agregación)
    └── 18_historial_ventas.py         # SQL: JOIN
    └── 15_actividad_favorita.py
```

## 📝 Estilo de Código

### Principios
- **Claridad sobre optimización**: El código debe ser fácil de leer y entender
- **Sin jerga técnica**: Explica conceptos como si fuera una receta
- **Nombres descriptivos**: `gasto_total`, `categoria_mayor`, no `x`, `tmp`
- **Comentarios útiles**: Explica el "por qué", no el "qué"

### Ejemplos

```python
# ✅ Bien: pandas con operaciones claras
import pandas as pd

df = pd.read_csv("data/compras.csv")
df["gasto"] = df["precio"] * df["cantidad"]
total = df["gasto"].sum()
print(f"Gasto total: {total:.2f}€")

# ❌ Evitar: código críptico sin contexto
import pandas as pd
d=pd.read_csv("data/c.csv");print(sum(pd.Series([float(r[1])*int(r[2])for r in open('data/c.csv').readlines()[1:]]).sum()))
```

## 🎯 Tipos de Ejercicios

### Ejercicios Básicos (1-5): Python Puro
- **SIN pandas**, **SIN dependencias externas**
- Conceptos: variables, input, for, if, strings
- Máximo 10 líneas de código

**Ejemplo estructura:**
```python
# Ejercicio simple sin dependencias
nombre = input("¿Cuál es tu nombre? ")
print(f"¡Hola {nombre}!")
```

### Ejercicios con Datos (6-15): Pandas
- **SIEMPRE usan pandas** para leer datos
- Operaciones: filtrar, agrupar, sumar, contar
- Datos en CSV o JSON (nunca TXT desestructurado)

**Ejemplo estructura:**
```python
import pandas as pd

# Leer datos estructurados
df = pd.read_csv("data/archivo.csv")

# O

### Ejercicios con Base de Datos (16-18): SQL con Pandas
- **Usan pandas.read_sql()** para consultar SQLite
- Conceptos: SELECT, SUM(), JOIN, ORDER BY
- Datos en archivo .db con tablas relacionadas
- **IMPORTANTE:** Mantienen consistencia con pandas

**Ejemplo estructura:**
```python
import pandas as pd

# Leer datos desde SQLite usando pandas
df = pd.read_sql("SELECT * FROM tabla", "sqlite:///data/archivo.db")

# O con consultas más complejas
df = pd.read_sql("""
    SELECT c.nombre, COUNT(*) as compras
    FROM compras c
    GROUP BY c.nombre
""", "sqlite:///data/archivo.db")

# Iterar sobre resultados
for _, fila in df.iterrows():
    print(f"Cliente: {fila['nombre']}")
```peración clara
resultado = df["columna"].sum()  # o .max(), .groupby(), etc.

# Mostrar respuesta amigable
print(f"Resultado: {resultado}")
```

## 💡 Pautas para Nuevos Ejercicios

### Cuando añadas un ejercicio:

1. **Define una pregunta cotidiana real**
   - ✅ "¿Cuánto dinero gasté esta semana?"
   - ❌ "Implementar un árbol binario de búsqueda"

2. **Crea datos sintéticos estructurados**
   - Usa CSV o JSON (datos rectangulares)
   - Evita TXT desestructurado
   - Incluye 6-10 filas de ejemplo

3. **Escribe la solución con pandas**
   - Importa: `import pandas as pd`
   - Lee datos: `pd.read_Tipo | Ejercicios |
|-----------|----------|------|-----------|
| **Compras/Gastos** | `compras_semana.csv`, `supermercado_gastos.csv` | CSV+Pandas | 6, 10, 12 |
| **Recetas** | `recetas.json` | JSON+Pandas | 7, 11 |
| **Deportes** | `deportes_mes.csv` | CSV+Pandas | 8, 13, 15 |
| **Películas** | `peliculas_favoritas.json` | JSON+Pandas | 9 |
| **Libros** | `libros_biblioteca.json` | JSON+Pandas | 14 |
| **Tienda de Bicicletas** | `bicicletas_tienda.db` | SQLite+SQL | 16, 17, 18 |

### Base de datos SQLite: Estructura

La BD `bicicletas_tienda.db` contiene:

```
TABLA: bicicletas
├── id (PRIMARY KEY)
├── nombre (TEXT)
├── modelo (TEXT)
├── precio (REAL)
├── stock (INTEGER)
└── tipo (TEXT)

TABLA: clientes
├── id (PRIMARY KEY)
├── nombre (TEXT)
├── email (TEXT)
├── telefono (TEXT)
├── ciudad (TEXT)
└── fecha_registro (DATE)

TABLA: ventas
├── id (PRIMARY KEY)
├── cliente_id (FOREIGN KEY)
├── bicicleta_id (FOREIGN KEY)
├── cantidad (INTEGER)
├── precio_unitario (REAL)
└── fecha_compra (DATE)
```
   - Referencia al archivo de datos

### Patrones comunes de pandas a usar

```python
# Leer datos
df = pd.read_csv("data/archivo.csv")
df = pd.read_json("data/archivo.json")

# Operaciones
df["nueva_columna"] = df["col1"] * df["col2"]    # Crear columna
total = df["columna"].sum()                       # Sumar
maximo = df["columna"].max()                      # Máximo
minimo = df.loc[df["col"].idxmin()]              # Fila con mínimo
conteos = df["tipo"].value_counts()              # Contar ocurrencias
agrupado = df.groupby("categoria")["valor"].sum() # Agrupar y sumar
filtrado = df[df["precio"] > 100]                # Filtrar por condición
```

## 🔄 Categorías de Datos

El proyecto usa estos temas cotidianos:

| Categoría | Archivos | Ejercicios |
|-----------|----------|-----------|
| **Compras/Gastos** | `compras_semana.csv`, `supermercado_gastos.csv` | 6, 10, 12 |
| **Recetas** | `recetas.json` | 7, 11 |
| **Deportes** | `deportes_mes.csv` | 8, 13, 15 |
| **Películas** | `peliculas_favoritas.json` | 9 |
| **Libros** | `libros_biblioteca.json` | 14 |

## ⚠️ Qué Evitar

- ❌ Importar pandas pero no usarlo (trampas)
- ❌ Código que solo lee sin procesar datos
- ❌ Archivos TXT desestructurados (usa CSV/JSON)
- ❌ Ejercicios sin datos reales
- ❌ Explicaciones técnicas sin contexto
- ❌ Dependencias innecesarias (solo pandas)

## ✅ Checklist para Ejercicios Nuevos

- [ ] Pregunta es cotidiana y clara
- [ ] Datos en CSV o JSON (nunca TXT)
- [ ] Solución USA pandas (no solo lo importa)
- [ ] Máximo 10 líneas de código funcional
- [ ] Comentarios mínimos, código auto-explicativo
- [ ] Resultado impreso en formato legible
- [ ] Documentado en `ejercicios.md`
- [ ] Ejecutable con: `uv run soluciones/NNN_nombre.py`

## 🧪 Pruebas y Ejecución

```bash
# Instalar dependencias
uv sync

# Ejecutar un ejercicio
uv run soluciones/06_gasto_total_compras.py

# Ver los datos que usa
head -5 data/compras_semana.csv
```

## 🎓 Objetivo Educativo

El propósito es que **cualquier persona pueda aprender Python** viendo código que resuelve sus problemas cotidianos. No importa si nunca ha programado—cada línea debe ser entendible como una receta de cocina.
