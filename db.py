import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('progreso.db')
cursor = conn.cursor()

# Crear tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS progreso(
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    nivel INTEGER
)
''')

# Insertar datos
cursor.execute('INSERT INTO progreso(nombre, nivel) VALUES(?, ?)', ('Juan', 1))

# Leer datos
cursor.execute('SELECT * FROM progreso')
print(cursor.fetchall())

conn.commit()
conn.close()