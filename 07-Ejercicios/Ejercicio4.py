"""
Ejercicio 4
    Pedir 2 numeros al usuario y hacer todas las operaciones basicas 
    de una calculadora y mostrarlo por pantalla 

"""


from __future__ import division
from audioop import mul


numero1 = int(input("Introduce el primer número: "))

numero2= int(input("Introduce el segundo número: "))

suma= numero1 + numero2
resta= numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2 

print(f"El resultado de la suma es: {suma}")
print(f"El resultado de la resta es: {resta}")
print(f"El resultado de la multiplicacion es: {multiplicacion}")
print(f"El resultado de la division es: {division}")