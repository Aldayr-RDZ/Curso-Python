nombre = 'Angel Aldayr'

#Funciones generales
print(nombre)

print(type(nombre))

#Detectar el tipado 
comprobar = isinstance(nombre, str)

if comprobar:
    print("Esa variable es un string")
else:
    print("No es una cadena")

if not isinstance( nombre, float):
    print("La variable no es un numero con decimales")

#Limpiar espacios 
frase = "        mi contenido         "
print(frase)
print(frase.strip())

#Eliminar variables 
year = 2022
print(year)
del year
# print(year)

texto = ' ff  '
if len(texto) <= 0:
    print("la variable esta vacia")
else: 
    print("La variable tiene contenido: ", len(texto))

# Encontrar caracteres 
frase = 'La vida es bella'
print(frase.find("vida"))

#Remplazar palabras en un string 
nueva_frase=  frase.replace("vida", "moto")
print(nueva_frase)

#mayusculas y minusculas 
print(nombre)
print(nombre.lower())
print(nombre.upper())