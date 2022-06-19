import psycopg2
#Conexion a la base de datos 
conexion = psycopg2.connect(database="Servicio", user="postgres", password="1801769")

#Creacion del cursor
cursor=conexion.cursor()




#Query
# sql="insert into articulos(descripcion, precio) values (%s,%s)"
# datos=("naranjas", 50)

#Execute del query con sus datos correspondientes para hacer un insert a la base de datos
# cursor.execute(sql, datos)

#Creacion de tabla con python 
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS vehiculos(
#     id serial,
#     marca varchar(50),
#     modelo varchar(50),
#     precio float,
#     CONSTRAINT pk_vehiculo PRIMARY KEY(id)
# )

# """)


# Inertar datos

# cursor.execute(" INSERT INTO vehiculos values(1,'Opel', 'Astra', 15824)")
# cursor.execute(" INSERT INTO vehiculos values(3,'Nissan', 'Versa', 12220)")
# cursor.execute("SELECT * FROM vehiculos")
# resultado = cursor.fetchall()
# for coche in resultado:
#     print(coche)

# Eliminar
# cursor.execute("DELETE FROM vehiculos WHERE marca='Nissan' ")

# Actualizar 
cursor.execute("UPDATE vehiculos SET precio=10000 where id=1")


conexion.commit()
conexion.close() 