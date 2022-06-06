"""
Modulos: son funcionalidades ya hechas para reutulizar. 
En python por defecto hay muchos modulos 

Podemos conseguir modulos que ya vienen en el lenguaje 
modulos en internet, y tambien podemos crear nuestros modulos 
"""

#Importar modulo propio 
# import mimodulo
# from mimodulo import holaMundo
from mimodulo import *
print(holaMundo("Angel Aldayr Rdz Gzz"))


#modulo de fechas
import datetime
print(datetime.date.today())
# import datetime
# from re import T
# import pytz
# import calendar 

# today = datetime.datetime.now()
# timezone= pytz.timezone('America/Monterrey')
# aware = datetime.datetime.now(timezone)
# print("dia",aware.strftime("%Y-%m-%d"))
# print("hora",aware.strftime("%H:%M:%S"))
# print("-------------------------")
# print(today.strftime("El dia  %Y-%m-%d"))
# print(today.strftime("%H:%M:%S"))

#modulo matematicas
import math
print(f'Raiz cuadrada de 10: {math.sqrt(10)}')
print("Numero pi", float(math.pi))

print("Redondear: ", math.ceil(6.5443))
print("Redondear: ", math.floor(6.5443))


#modulo random 
import random
print("Número aleatorio entre 15 y 67: ", random.randint(15,67))