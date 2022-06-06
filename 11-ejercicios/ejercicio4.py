"""
Ejercicio 4. Crear un script que tenga 4 variables, una lista, un string, un entero y un booleano y que imprima
un mensaje segun el tipo de dato de cada variable 

"""

def traducirTexto(tipo):
    Texto=None
    if tipo == str:
        Texto = 'Cadena de texto'
    elif tipo == list:
        Texto = 'Lista'
    elif tipo == int:
        Texto = 'Numero entero'
    elif tipo == bool:
        Texto = 'Booleano'
    
    return Texto

def comprobar(dato, tipo):
    testing = isinstance(dato, tipo)
    result= ''
    if testing:
        result =f"Este dato es del tipo {traducirTexto(tipo)}"
    else: None

    return result


mi_lista =["Hola mundo", 77]
titulo = "El limite no existe"
numero = 7
verdarero= True

print(comprobar(mi_lista, type(mi_lista)))
print(comprobar(titulo, type(titulo)))
print(comprobar(numero, type(numero)))
print(comprobar(verdarero, type(verdarero)))