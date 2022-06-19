"""
Proyecto Python y PostgreSQL
-- Abrir asistente 
-- login o registro 
-- Si elegimos registro, creara un usuario en la bbdd 
-- Si elegimos login, identifica al usuario y nos preguntara 
-- Crear nota, mostrar nota y eliminar nota 
"""
from usuarios import acciones



print("""Acciones disponibles:
        - 1. Registro
        - 2. Login
""")


hazEl = acciones.Acciones()
caso = str(input("Que deseas hacer?: "))

if caso == 'registro':
    hazEl.registro()
elif caso == 'login':
    hazEl.login()
    