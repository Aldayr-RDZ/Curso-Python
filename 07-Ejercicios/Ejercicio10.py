""" 
Ejercicio 10 
El programa tiene que pedor la nota de 15 alumnos y sacar por pantalla cuantos han aprobados 
y cuantos han reprobados
"""

contador = 1
aprobados = 0
reprobados = 0

cantidad_de_alumnos = int(input("¿Cuantos alumnos tiene?: "))

while contador <= cantidad_de_alumnos:
    nota = int(input(f'¿Que nota quiere ponerle al \"alumno {contador}\"?: '))
    
    if(nota>=5):
        aprobados = aprobados +1
    
    else: 
        reprobados=reprobados+1
    
    
    contador = contador + 1

print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos reprobados: {reprobados}")