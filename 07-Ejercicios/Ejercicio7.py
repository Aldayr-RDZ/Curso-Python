"""
Ejercicio 7 
Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario 
"""

numero1= int(input("Ingrese el primer numero: "))
numero2= int(input("Ingrese el segundo numero: "))

if(numero1 < numero2):
    for numero in range( numero1, numero2+1):
        if(numero %2 != 0 ):
            print(numero)