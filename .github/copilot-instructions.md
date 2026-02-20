# Instrucciones para Agentes de IA

## 🎯 Propósito

Este es un repositorio de **ejercicios prácticos de Python**. Cada ejercicio resuelve un problema cotidiano para que sea fácil de entender sin necesidad de conocimientos técnicos previos.

## 🔧 Configuración del Proyecto

### Versión de Python
- **Mínima requerida:** Python 3.11+
- **Gestor de paquetes:** `uv` (instalación rápida de dependencias)

### Primeros pasos para instalar dependencias
```bash
# Instalar todas las dependencias del proyecto
uv sync

# Ejecutar un script específico
uv run nombre_del_archivo.py

# Crear un nuevo ambiente si es necesario
uv venv
```

## 📝 Estilo de Código

### Principios
- **Claridad sobre optimización**: El código debe ser fácil de leer y entender
- **Comentarios útiles**: Explica el "por qué", no el "qué" (el código ya dice el qué)
- **Nombres descriptivos**: Usa nombres como `edad_persona`, `lista_compras`, no `x`, `var1`

### Ejemplos de código bien estructurado
```python
# ✅ Bien: claridad para personas no técnicas
def calcular_descuento(precio, porcentaje_descuento):
    """Calcula el precio final después de aplicar un descuento."""
    descuento_dinero = precio * (porcentaje_descuento / 100)
    precio_final = precio - descuento_dinero
    return precio_final

# ❌ Evitar: código críptico
def calc(p, d):
    return p * (1 - d / 100)
```

## 🏗️ Estructura del Proyecto

Cada ejercicio es un script Python independiente. Se organiza así:

```
ejercicios-python/
├── README.md                              # Info general
├── .github/
│   └── copilot-instructions.md           # Este archivo
├── 01_basicos/                           # Ejercicios básicos
│   ├── hola_mundo.py
│   ├── compra_supermercado.py
│   └── ...
├── 02_funciones/                         # Ejercicios con funciones
│   ├── saludar_personas.py
│   └── ...
└── pyproject.toml                        # Configuración de dependencias (si se necesita)
```

## 💡 Convenciones del Proyecto

### Nombres de archivos
- Usa **snake_case**: `lista_compras.py`, `ordenar_numeros.py`
- Describe qué hace el archivo de forma clara

### Estructura de un ejercicio
```python
"""
Tema: Listas de compras
Objetivo: Crear una lista que permita agregar y eliminar artículos
Contexto: Simulamos las tareas diarias de compra en un supermercado
"""

def crear_lista_compras():
    """Inicia una nueva lista de compras vacía."""
    return []

def agregar_articulo(lista, articulo):
    """Agrega un artículo a la lista de compras."""
    lista.append(articulo)
    return lista

# Uso del programa
if __name__ == "__main__":
    compras = crear_lista_compras()
    agregar_articulo(compras, "Leche")
    agregar_articulo(compras, "Pan")
    print(f"Compras: {compras}")
```

## 🔄 Palabras Clave para Entender el Contexto

Cuando veas estos términos en comentarios o nombres, sabrás qué se espera:

| Término | Significa |
|---------|-----------|
| `cotidiano` | Un problema de la vida real (compras, recetas, horarios) |
| `sencillo` | Fácil de entender sin experiencia previa |
| `sin biblioteca externa` | Solo Python puro, sin instalar paquetes extras |
| `paso a paso` | Explica qué sucede en cada línea |

## 🧪 Pruebas y Ejecución

Ejecuta los ejercicios así:
```bash
# Ejecutar un archivo
python 01_basicos/hola_mundo.py

# O con uv
uv run 01_basicos/hola_mundo.py
```

## 📚 Ejemplos Cotidianos

Cada ejercicio debe relacionarse con la vida diaria:

- **Listas**: Carrito de compras, tareas del día
- **Números**: Cálculo de descuentos, conversión de dinero
- **Textos**: Búsqueda en recetas, reverso de un nombre
- **Bucles**: Repetir 10 veces un recordatorio, procesar múltiples items
- **Condiciones**: "Si llueve, llevar paraguas", "Si el precio es mayor a 100, aplicar descuento"

## ⚠️ Qué Evitar

- ❌ Términos técnicos sin explicación
- ❌ Código "inteligente" que sacrifica clarity
- ❌ Ejercicios sin contexto del mundo real
- ❌ Dependencias innecesarias

## 🎓 Objetivo Educativo

El propósito es que **cualquier persona pueda aprender Python** viendo código que resuelve sus problemas cotidianos. No importa si nunca ha programado—entienda cada línea como si fuera una receta de cocina.
