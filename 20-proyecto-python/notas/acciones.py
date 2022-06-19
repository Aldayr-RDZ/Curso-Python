
from re import T
import notas.nota as model

class Acciones:

    def crear(self, usuario):
        print(f'\n{usuario[1]} vamos a crear una nueva nota')
        
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Introduce la descripcion de tu nota: ")

        nota = model.Nota(usuario_id=usuario[0],titulo= titulo, descripcion=descripcion)
        guardar = nota.guardar()

        if guardar[0]>=1:
            print(f'Perfecto haz guardado la nota: {nota.titulo}')
        else:
            print(f'No se ha guardado la nota, lo siento {usuario[1]}')
    
    def mostrar(self, usuario):
        print(f'{usuario[1]} aqui tienes tus notas: ')
        nota = model.Nota(usuario_id=usuario[0])
        notas = nota.listar()
        for nota in notas:
            print("\n********************************")
            print(nota[2])
            print(nota[3])
            print("********************************")
        
    def borrar(self, usuario):
        print(f'{usuario[1]} vamos a borrar notas')
        titulo = input("Introduce el titulo de la nota a borrar: ")
        nota = model.Nota(usuario_id=[0], titulo=titulo)
        eliminar = nota.eliminar(titulo=titulo)

        if eliminar[0] >=1:
            print(f"Hemos eliminado la nota: {nota.titulo}")
        else:
            print("No se ha eliminado la nota, prueba despues")