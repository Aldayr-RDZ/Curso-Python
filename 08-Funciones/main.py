"""
Una funcion es un conjunto de instrucciones agrupadas bajo un nombre 
concreto que pueden reutilizarse invocando a la funcion tantas veces como sea necesario 

def nombreDeLaFuncion(parametros):
    ##BLOQUE DE CODIGO

nombreDeLaFuncion(mi_parametro):
"""

print("\n## Ejemplo 1 ##")
###EJEMPLO 1####
## definimos la funcion 



def mostrarNombre():
    print("Angel Aldayr Rodriguez Gonzalez")


## Invocamos la funcion 
mostrarNombre()


print("\n## Ejemplo 2 ##")
###EJEMPLO 2 ###

nombre = 'Angel Aldayr Rodriguez Gonzalez'
def mostrarNombre(nombre, edad):
    print(f'Tu numbre es: {nombre}')
    if edad>=18:
        print("Y eres mayor de edad")
    else:
        print("Y eres menor de edad")

# nombre = input("Ingrese su nombre: ") 
# edad= int(input("Ingrese su edad: "))
# mostrarNombre(nombre, edad)


print("\n## Ejemplo 3 ##")
###EJEMPLO 3 ###

def tablaMultiplicar(numero):
    print(f'La tabla de multiplicar del numero: {numero}')
    
    for cabecera in range(1, 11):
       print(f'{numero} X {cabecera} = {numero * cabecera}')

# Numero = int(input("Ingrese un número: "))
# tablaMultiplicar(Numero)


print("\n## Ejemplo 3.1 ##")

for numeroDeTabla in range(1,11):
    tablaMultiplicar(numeroDeTabla)


print("\n## Ejemplo 4 ##")
## EJEMPLO 4 ###
#parametros opcionales#

def getEmpleado(nombre, dni= None):
    print("EMPLEADO")
    print(f'Nombre: {nombre}')
    if dni != None:
        print(f'DNI: {dni}')

getEmpleado('Angel','dsdfds1')



print("\n## Ejemplo 5 ##")
## EJEMPLO 5##
## PARAMETROS OPCIONALES Y RETURN O DEVOLVER DATOS##

def saludo(nombre):
    saludo= f'hola, saludos {nombre}'

    return saludo
print(saludo('alda'))

print("\n## Ejemplo 6 ##")
def calculadora(numero1, numero2, basicas= False):
    
    suma= numero1+numero2
    resta= numero1-numero2
    multiplicacion = numero1*numero2
    division = numero1/numero2

    cadena=''
    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += '\n'
        cadena += "Resta: " + str(resta)
        cadena += '\n'
    else:
        cadena += "Multiplicación: " + str(multiplicacion)
        cadena += '\n'
        cadena += "Division: " + str(division)

    return cadena

print(calculadora(56,5, True))

print("\n## Ejemplo 7 ##")
## funciones dentro de funciones ##
def getNombre(nombre):
    texto = f'El nombre es: {nombre}'
    return texto

def getApellidos(apellidos):
    texto = f'los apellidos son: {apellidos}'
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre)+ "\n" + getApellidos(apellidos)
    return texto

# print(getNombre("Aldayr"), getApellidos("RDZ"))
print(devuelveTodo("Aldayr", "Rdz"))

## Funcion lambda##
print("\n## Ejemplo 8 ##")

dime_el_year = lambda year: f'El año es {year *2}'
print(dime_el_year(2022))
