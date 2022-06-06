"""
Ejercicio 3. Programa que compruebe si una variable esta vacia y si esta vacia, rellenarla con texto en minisculas y mostrarlo en mayusculas

"""

texto =''

if len(texto.strip()) <= 0:
    texto='Soy un texto en minisculas'
    print(texto.upper())
else:
    print("Si hay contenido en la variable", texto)
