"""
Ejercicio 1. Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente:

- (LISTO) Recorrer la lista y mostrarla
- (LISTO) Hacer una funcion que recorra lista de numeros y devuelva un string
- (LISTO) Ordenarla y mostrarla X
- (LISTO) Mostrar su longuitud X
- Buscar algun elemento (que el usuario pida por teclado)

"""
#Creamos la lista
Lista = [1,2,3,4,10,33,100,88,4,22]

#Recorrer la lista
# print("----Recorrer la lista----")

# for elemento in Lista:
#     print(elemento)

# print("----Crear Funcion para recorrer la lista----")
#Hacer una funcion
def mostrarLista(List):
    resultado = ''
    for numero in List:
        resultado += 'Elemento: '+ str(numero)
        resultado += "\n"
    return resultado

# print(mostrarLista(Lista))
# Ordenar y mostrar 
# print("##### Ordenar y mostrar ######")
Lista.sort()
# print(mostrarLista(Lista))

# 

#busqueda en la lista 
try:
    Busqueda = int(input("Ingrse el número: "))

    comprobar = isinstance(Busqueda, int)
    while not comprobar or Busqueda <= 0:
        Busqueda = int(input("Ingrse el número: "))
    else:
        print(f'Has introducido el {Busqueda}')

    print(f'Buscar en la lista el numero {Busqueda}')


    search= Lista.index(Busqueda)
    print(f'El numero buscado existe en la lista, es el indice {search}')
except:
    print("El numero no esta en la lista ")
