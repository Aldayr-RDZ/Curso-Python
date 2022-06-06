""""
Ejercicio 2. Escribir un programa que añada valores a una lista mientras 
que su longuitud sea menor a 120 y luego mostrar la lista 

PLUS: usar while y For

"""

# coleccion = []

# for contador in range (0,120):
#     coleccion.append(f'Elemenrto-{contador}')
#     print("Mostrando el: " + coleccion[contador])

# print(coleccion)

coleccion = []
cont= 0

while cont<120:
    coleccion.append(f'Elemnto-{cont}')
    print("Mostrando el: " + coleccion[cont])
    cont += 1

print(coleccion[77])