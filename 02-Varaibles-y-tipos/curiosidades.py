mi_texto = '"Hola"'
mi_texto2 = "Mundo \"HOLA\""

texto_unido= mi_texto + " " + mi_texto2
print(texto_unido)

#
print(mi_texto + " \n " + mi_texto2) #Salto de linea
print(mi_texto + " \t " + mi_texto2) #un tabulador
print(mi_texto + " \r " + mi_texto2) #borra la primera variable mi_texto

"""
print(f"{mi_texto} {mi_texto2}")


print("{} {}".format(mi_texto,mi_texto2))
"""