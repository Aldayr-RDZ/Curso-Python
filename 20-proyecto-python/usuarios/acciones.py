import usuarios.usuario as model 
import notas.acciones

class Acciones:
    def registro(self):
        print("\nRegistrate en el sistema")
        nombre= input("¿Cual es tu nombre?: ")
        apellidos= input("¿Cuales son tus apellidos?: ")
        email= input("¿Introduce tu email?: ")
        password= input("¿Introduce tu contraseña?: ")

        usuario= model.Usuario(nombre=nombre, apellidos= apellidos, email=email, password=password)
        registro= usuario.registrar()
        
        if registro[0]>=1:
            print(f'\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}')
        else:
            print("\n No te has registrado")
    
    def login(self):
        print("\nIndentificate en el sistema")
        try:
            email= input("¿Introduce tu email?: ")
            password= input("¿Introduce tu contraseña?: ")

            usuario = model.Usuario('','', email= email, password=password)
            login = usuario.identificar()

            if email== login[3]:
                print(f'\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]} ')
                self.proximasAcciones(login)

        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print(f'Login incorrecto')
    
    def proximasAcciones(self, usuario):
        print("""
        -Crear nota (crear)
        -Mostrar nota (mostrar)
        -Eliminar nota (eliminar)
        -Salir (salir)
        """)
        
        accion = input("¿Que quieres hacer?")
        hazEl = notas.acciones.Acciones()

        if accion == 'crear':
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == 'mostrar':
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == 'eliminar':
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == 'salir':
            print(f'Hasta luego {usuario[1]}')
            exit()