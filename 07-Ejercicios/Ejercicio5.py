"""
Ejercicio 5
Hacer un programa que muestre todos los numeros entre dos numeros que nos diga el usuario 

"""
numero1= int(input("Ingrsa el primer numero:"))
numero2= int(input("Ingrsa el segundo numero:"))

if numero1 < numero2 :
    for i in range(numero1, numero2+1):
        print(i)

