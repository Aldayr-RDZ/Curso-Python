"""
Ejercicio 8
¿Cuanto es el x porciento de X numero?
20% de 150 

"""

numero = int(input("Introduce el numero: "))
porcentaje = int(input(f"¿Que porcentaje quieres sacar de {numero}?: "))

resultado = ( numero * (porcentaje/100))
print(f"El {porcentaje} % de {numero} es: {resultado}")
