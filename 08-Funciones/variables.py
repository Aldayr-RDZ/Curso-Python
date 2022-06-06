"""
Variabes locales: se definen  dentro de la funcin y no se puede usar fuera de ella, 
solo estan disponibles dentro. a no ser que hagamos un return 

Variables globales: son las que se declaran uera de una funcion y estan disponibles dentro y fuera de ellas.
"""
# Variable global 

frase = 'Pienso y luego existo'
print(frase)


def holaMundo():
    # frase = 'Hola mundo!!'
    print(frase)

    year = 2021
    print(year)

    global website
    website= 'aldayr.com'
    print(website)
    return "Dato devuelto " + str(year)

print(holaMundo())