"""
Una variable es un contenedor de informacion 
que dentro guardara un dato, se pueden crear 
muchas variables y que cada una tenga un dato distinto.
"""
texto = "Máster en python "
texto2 = "Que se encuentra en udemy"
numero = 45
decimal = 6.5
#Mostrar el valor de las variables 
print(texto)
print(texto2)
print(numero)

print("------------------------------------------")
#Sustituimos el valor de las variables 
numero= 20
decimal= 10.3

print(numero)
print(decimal)

#Concatenacion 
nombre = "Angel Aldayr"
apellidos = "Rodriguez Gonzalez"
web = "nose.com"

#1era manera (normal bro)
print(nombre+ " " + apellidos + " - "+ web )

#2da manera (mamador medio)
print(f"{nombre} {apellidos} - {web}")

#3ra manera (mamador a lo extremo)
print("Hola me llamo {} {} y mi web es {} ".format(nombre,apellidos,web))