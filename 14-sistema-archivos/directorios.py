import os, shutil

#Crear carpeta 
if not os.path.isdir("./micarpeta"):
    os.mkdir("./micarpeta")
else:
    print("ya existe la carpeta ")




#Copiar  
# ruta_original ="./micarpeta"
# ruta_nueva =  "./micarpeta_COPIADA"

# shutil.copytree(ruta_original, ruta_nueva)

#Eliminar 
# os.rmdir("./micarpeta_COPIADA")

print("contenido de mi carpeta:")
contenido = os.listdir("./micarpeta")
print(contenido)

for fichero in contenido:
    print(fichero)