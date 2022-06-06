"""
    Ejercicio 3, Escribir un programa que muestre los cuadrados
    (un numero multiplicado por si mismo) de los 60 primeros numeros
    naturales 

    Resolverlo con el For y con While

"""

#WHILE
tope=1
while tope<=60:
    i = tope
    cuadrado = i*i
    print(f"El cuadrado de {i} es : {cuadrado}")
    tope=tope+1


#FOR
for numero in range(1, 61):
    cuadrado = numero*numero
    print(f'El cuadrado de {numero} es: {cuadrado}')