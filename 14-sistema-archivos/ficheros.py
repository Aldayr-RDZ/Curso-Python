from io import open
import pathlib 
import shutil
import os

#Abrir archivo 
archivo = open(str(pathlib.Path().absolute()) + "/fichero_texto.txt", 'a+')

#Escribir 
archivo.write("******** ESCRIBIR un texto desde python *********\n")

#Cerrar archivo 
archivo.close()

#Abrir archivo 
archivo_lectura = open(str(pathlib.Path().absolute()) + "/fichero_texto.txt", 'r')

#Leer contenido 
# contenido = archivo_lectura.read()
# print(contenido)

#Leer contenido y guardarlo en una lista 
lista = archivo_lectura.readlines()
archivo_lectura.close()
for frase in lista:
    print("- "+frase.upper())

#Copiar archivos 
# ruta_original =str(pathlib.Path().absolute()) + "/fichero_texto.txt"
# ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
# ruta_alternativa = str(pathlib.Path().absolute())+"/../13-paquetes/fichero_copiado13.txt"
# shutil.copyfile(ruta_original, ruta_alternativa)

# # Mover
# ruta_original =str(pathlib.Path().absolute()) + "/fichero_texto_NUeVo.txt"
# ruta_nueva =str(pathlib.Path().absolute())+"/../13-paquetes/fichero_copiado13.txt"
# shutil.move(ruta_nueva, ruta_original)

#Eliminar archivos 

# ruta =str(pathlib.Path().absolute()) + "/fichero_texto_NUeVo.txt"
# os.remove(ruta)

#Comprobar si existe fichero 
# import os.path
# print(os.path.abspath("./"))
if os.path.isfile(os.path.abspath("./") + "/fichero_texto.txt"):
    print("el archivo existe ")
else:
    print("el archivo no existe")