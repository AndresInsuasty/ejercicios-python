import sqlite3
import os

db_path = "data/bicicletas_tienda.db"

# Eliminar si existe
if os.path.exists(db_path):
    os.remove(db_path)

# Conectar a la BD
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Tabla 1: BICICLETAS
cursor.execute("""
CREATE TABLE bicicletas (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    modelo TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL,
    tipo TEXT NOT NULL
)
""")

bicicletas = [
    (1, "Mountain Bike Pro", "XC-2024", 450.00, 12, "Montaña"),
    (2, "Road Racer Elite", "RR-2024", 650.00, 8, "Carretera"),
    (3, "Urban Commuter", "UC-2024", 320.00, 20, "Urbana"),
    (4, "Kids Fun Bike", "KFB-2024", 150.00, 15, "Infantil"),
    (5, "BMX Stunter", "BMX-2024", 280.00, 10, "BMX"),
    (6, "E-Bike Leisure", "EBL-2024", 1200.00, 5, "Eléctrica"),
]

cursor.executemany("INSERT INTO bicicletas VALUES (?, ?, ?, ?, ?, ?)", bicicletas)

# Tabla 2: CLIENTES
cursor.execute("""
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL,
    telefono TEXT,
    ciudad TEXT NOT NULL,
    fecha_registro DATE NOT NULL
)
""")

clientes = [
    (1, "Carlos Martínez", "carlos@email.com", "555-1234", "Madrid", "2025-01-15"),
    (2, "María García", "maria@email.com", "555-5678", "Barcelona", "2025-01-20"),
    (3, "Juan López", "juan@email.com", "555-9012", "Valencia", "2025-02-01"),
    (4, "Ana Rodríguez", "ana@email.com", "555-3456", "Sevilla", "2025-02-05"),
    (5, "Pedro Sánchez", "pedro@email.com", "555-7890", "Bilbao", "2025-02-10"),
    (6, "Laura Fernández", "laura@email.com", "555-2345", "Alicante", "2025-02-12"),
]

cursor.executemany("INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?)", clientes)

# Tabla 3: VENTAS
cursor.execute("""
CREATE TABLE ventas (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    bicicleta_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    precio_unitario REAL NOT NULL,
    fecha_compra DATE NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (bicicleta_id) REFERENCES bicicletas(id)
)
""")

ventas = [
    (1, 1, 3, 1, 320.00, "2025-02-01"),
    (2, 2, 1, 2, 450.00, "2025-02-03"),
    (3, 3, 5, 1, 280.00, "2025-02-05"),
    (4, 1, 4, 2, 150.00, "2025-02-07"),
    (5, 4, 2, 1, 650.00, "2025-02-08"),
    (6, 5, 6, 1, 1200.00, "2025-02-10"),
    (7, 2, 3, 3, 320.00, "2025-02-11"),
    (8, 6, 1, 1, 450.00, "2025-02-12"),
    (9, 3, 4, 2, 150.00, "2025-02-15"),
    (10, 4, 5, 1, 280.00, "2025-02-18"),
]

cursor.executemany("INSERT INTO ventas VALUES (?, ?, ?, ?, ?, ?)", ventas)

conn.commit()
conn.close()

print(f"✅ Base de datos creada en {db_path}")
