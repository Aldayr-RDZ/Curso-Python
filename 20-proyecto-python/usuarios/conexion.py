import psycopg2


def conectar():
    #Conexion a la base de datos 
    conexion = psycopg2.connect(database="Servicio", user="postgres", password="1801769")

    #Creacion del cursor
    cursor=conexion.cursor()

    return [conexion, cursor]