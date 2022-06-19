
from datetime import datetime
import hashlib
import usuarios.conexion as conexion

connect = conexion.conectar()
conexion_basededatos = connect[0]
cursor = connect[1]

class Usuario:
    
    def __init__(self, nombre, apellidos, email, password):
        self.nombre= nombre
        self.apellidos= apellidos
        self.email= email
        self.password= password
    
    def registrar(self):
        fecha= datetime.now()
        #Cifrar contraseña 
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf-8'))
        sql = 'INSERT INTO usuarios (nombre, apellidos, email, password, fecha) VALUES(%s, %s, %s, %s, %s)'
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
        try:
            cursor.execute(sql, usuario)
            conexion_basededatos.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    def identificar(self):
        #Consulta para comprobar si existe el usuario 
        sql = 'SELECT * FROM usuarios WHERE email= %s and password= %s'

        #Cifrado de contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf-8'))

        #datos para la consulta
        usuario =(self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)

        result= cursor.fetchone()

        return result