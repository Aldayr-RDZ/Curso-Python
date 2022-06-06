#Capturar excepciones y manejar errores en código 
#suceptible a fallos/erroes 



# try:
#     nombre= input("¿Cual es tu nombre?: ")
#     if len(nombre) > 1:
#         nombre_usuario = 'El nombre de usuario es: ' + nombre
#     print(nombre_usuario)
# except:
#     print("Ha ocurrido un error, mete bien el nombre")
# else:
#     print("Todo ha funcionado correctamente!!")
# finally:
#     print("Fin de la iteracion")


#Multiples excepciones
# try:
#     numero = int(input("Numero para elevarlo al cuadrado: "))
#     print("El cuadrado es: "+str( numero * numero ))
# except TypeError:
#     print("Debes convertir tus cadenas a enteros en el codigo!!")
# # except ValueError:
# #     print("Introduce un numero correcto")
# except Exception as e:
#     print(type(e))
#     print("Ha ocurrido un error: ", type(e).__name__)

#Excepciones personalizadas o lanzar excepcion 

try:
    nombre = input("Introduce el nombre: ")
    edad= int(input("Introduzca la edad: "))


    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <=1:
        raise ValueError("El nombre no esta completo ")
    print(f"Bienvenido al master en python {nombre} !!")
except ValueError:
    print("introduce los datos correctamente")
except Exception as e:
    print("Existe un error: ", e)