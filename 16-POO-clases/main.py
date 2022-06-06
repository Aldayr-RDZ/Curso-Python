#Programación orientada a objetos (POO o OOP)

#Definir una clase (molde para crear mas objetos de ese tipo
# (coche) con caracteristicas similares)

class Coche:
    
    # Atributos o propiedades (variables)
    # Caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Metodos, son acciones que hace el objeto (coche) (funciones)
    def setColor(self, color):
        self.color=color

    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo=modelo

    def getModelo(self):
        return self.modelo


    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -=1
    
    def getVelocidad(self):
        return self.velocidad
    

# Fin definicion clase 

# Crear un objeto / instanciar una clase
print("-------------------------------------------")
print("Coche 1")
coche = Coche()


coche.setColor("Amarillo")
coche.setModelo("Murcielago")


print(coche.marca,coche.getModelo(), coche.getColor())
print("Velocidad acutal:",coche.velocidad)
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
print("Velocidad acutal:",coche.velocidad)

print("-------------------------------------------")
print("Coche 2")
#Multiples objetos 
coche2 = Coche()
coche2.setColor("Verde")
coche2.setModelo("Gallardo")
print(coche2.marca ,coche2.getColor(), coche2.getModelo())