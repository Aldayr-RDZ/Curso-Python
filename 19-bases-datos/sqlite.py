import sqlite3

#Conexion 
conexion = sqlite3.connect('pruebas.db')

#Crear cursor 
cursor = conexion.cursor()

#Crear tabla 
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar(255),
    descripcion text,
    precio int(255)
);
""")

#guardar cambios 
conexion.commit()

# #insertar datos
# cursor.execute("INSERT INTO productos VALUES (null, 'segundo producto', 'descripcion del producto', 550)")
# conexion.commit()

#eliminar datos 
cursor.execute("DELETE FROM productos")
conexion.commit()
#insertar muchos registros de golpe 
productos = [
    ( "ordenador portatil", "buen PC", 700),
    ( "teclado", "buen teclado", 200),
    ( "camara portatil", "buea camara", 500),
    ( "ordenador ", "PC", 400),
]
cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productos)
conexion.commit()

#listar datos 
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

for producto in productos:
    print("Titulo:",producto[1])
    print("Descripcion:",producto[2])
    print("Precio:",producto[3])

#Cerrar la conexion 
conexion.close()
