"""
Ejercicio 6 
Mostrar todas las tablas de multiplicar del 1 al 10 
mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10 

"""

for i in range(1, 11):
    print(f"Tabla del {i}")
    
    for j in range(1,11):
        print(f"{i} X {j} = {str(i*j)}")

    print("\n")


