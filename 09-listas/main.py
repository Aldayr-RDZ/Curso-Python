"""
LISTAS (arrays)
colecciones o conjuntos de datos/valores, bajo un unico 
nombre. 
Para acceder a estos valores podemos usar un indice numerico 
"""

Pelicula= 'Batman'
# print(Pelicula)

#Definir lista 
Peliculas= ['Batman', 'Spiderman', 'Iron-man']
cantantes = list(('2pac','Drake','Jennifer lopez'))
year = list(range(2022, 2051))
variada = ["victor", 123, False, "texto"]


# print(variada)
# print(year)
# print(cantantes)
# print(Peliculas)

#indices 
Pelicula = 'otra cosa'
Peliculas[1]= 'Gran Torino'




print(Peliculas[1])
print(Peliculas[-2])
print(cantantes[0:1])
print(Peliculas[0:])


#Añadir elemento a lista 
cantantes.append("kase O")
cantantes.append("Natos y waor")
print(cantantes)

#Recorrer lista




# nueva_pelicula = ""
# while nueva_pelicula != 'parar':
#     nueva_pelicula = input("Introduce la nueva pelicula: ")
#     if nueva_pelicula !='parar':
#         Peliculas.append(nueva_pelicula)


# print("\n*****LISTADO PELICULAS******")
# for pelicula in Peliculas:
#     print(f'{Peliculas.index(pelicula)+1}. {pelicula}')


#Listas multidimensionales 
print("\n******** listado de contactos ***********")

contactos =[
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'Luis',
        'luis@luis.com'
    ],
    [
        'Salvador',
        'salvador@salvador.com'
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: "+elemento)
        else:
            print("Email: "+ elemento)
    print("\n")

# print(contactos[1][1])