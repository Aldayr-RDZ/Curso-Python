"""
Ejercicio 5. Crear una lista con el contenido de esta tabla:
Accion      Aventura            Deportes
GTA         Assins               Fifa 21      
COD         Crash                Pro 21
PUGB        Prince of Persia     Moto Gt 21

"""

Tabla = [
    {
        "categoria": "ACCIÓN",
        "juegos": ["GTA","Call of Duty","PUBG"],
    },
    {
        "categoria":"AVENTURA",
        "juegos":["Assins, Crash","Price of persia"]
    },
    {
        "categoria":"DEPORTES",
        "juegos": ["FIFA 21","PES 21", "MOTO GP 21"]
    }     
]

for categoria in Tabla:
    print(f"------------{categoria['categoria']}---------------")
    for juego in categoria['juegos']:
        print(juego)