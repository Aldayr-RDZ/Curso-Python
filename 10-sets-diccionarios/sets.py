"""
set es un tipo de dato, para tener una coleccion de valores, 
pero no tienen ni indice ni orden 

"""

personas = {
    "Victor",
    "Manuel",
    "Alberto",
}

personas.add("Aldayr")

print(personas)

personas.remove("Victor")
print(personas)

print(type(personas))