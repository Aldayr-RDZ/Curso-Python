# Un condicional es una esteuctura de control 

#Condicional IF
print("##### Ejemplo 1 #####")
color= "verde" 
#color = input("Adivina cual es mi color favorito: ")
if color == "rojo":
    print("\n chido we")
    print("color correcto ")
else: 
    print("\nel color es incorrecto ")

"""
# Operadores de comparacion 
== iugal 
!= diferente
< menor que 
> mayor que 
<= menor igual que 
>= mayor igual que 
"""
# Ejemplo 2
print("\n########## Ejemplo 2 ##########")
year = 2020 
#year = int(input("¿En que año estamos?: "))
if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Es un año anterior a 2021")

# Ejemplo 3
print("############## Ejemplo 3 ###############")

nombre = "Angel Aldayr"
ciudad = "N.L"
Continente = "Europeo"
edad = 18
mayoria_edad = 18

if edad >= mayoria_edad:
    print("{} es mayor de edad".format(nombre))
    if Continente != "America del Norte":
        print("el usuario no es americano")
    else: 
        print("Es de america del norte y de {}".format(ciudad))
else: 
    print(f"{nombre} no es mayor de edad")
#Ejemplo 4
print("############# Ejemplo 4 ################")
dia = 2
#dia = int(input("Introduce el dia de la semana: "))
"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
             print("Es jueves")
            else:
                if dia== 5:
                 print("Es viernes")
                else:
                    print("Es fin de semana")
"""
# if dia == 1:
#     print ("Es lunes ")
# elif dia == 2:
#     print("Es martes")
# elif dia == 3:
#     print("Es miercoles")
# elif dia == 4:
#     print("Es jueves")
# elif dia == 5:
#     print("Es viernes")
# else: print("Es fin de semana")

# #Ejemplo 5
# print("############# Ejemplo 5 ################")

# edad_minima = 18 
# edad_maxim = 65
# edad_oficial = int(input("Ingresa tu edad: "))
# #edad_oficial =17
# if edad_oficial >= 18 and edad_oficial <= 65:
#         print("Esta en edad de trabajar")
# else:
#     print("No esta en edad de trabajar")

#Ejemplo 5
print("############# Ejemplo 6 ################")

pais ="Alemania"

if pais=='Mexico' or pais=='España' or pais == 'Colombia':
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispanas")