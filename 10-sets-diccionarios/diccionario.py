""""
Diccionario:
Un tipo de dato que almacena un conjunto de datos.
Es formato clave > valor
Es parecido a un array asociativo o un objeto json 

"""

persona = {
    "nombre":"Aldayr",
    "apellidos":"Rodriguez",
    "edad": "22 años"
}

# print(persona["edad"])

#Lista con diccionarios 

contactos = [
    {
        'nombre':'Aldayr',
        'email':'aldayr@gmail.com'
    },
    {
        'nombre':'Roberto',
        'email':'roberto@gmail.com'
    },
    {
        'nombre':'Salvador',
        'email':'salvador@gmail.com'
    }
]

print(contactos[0]['nombre'])

print("\n Listado de contactos: ")
print("-------------------------------------------")
for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email de contacto {contacto['email']}")
    print("-------------------------------------------")