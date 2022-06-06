from coche import Coche

carro = Coche("Amarrillo", "Renault", "Clio", 150, 200, 4)
carro2 = Coche("Verde", "Seat", "Panda", 150, 200, 4)
carro3 = Coche("Azul", "Citroen", "Xara", 150, 200, 4)

print(carro.getInformacion())
print(carro2.getInformacion())
print(carro3.getInformacion())

carro3 = "Aleatorio"
if type(carro3) == Coche:
    print("Es un objeto correcto !!")
else: 
    print("No es un objeto")

# Visibilidad
print(carro.soy_publico)
# print(carro.__soy_privado)
print(carro.getPrivado())