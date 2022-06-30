# Tkinter 
# Modulo para crear interfaces de usuario 

import os
from tkinter import *

class Programa:

    def __init__(self):
        self.tittle = 'Master en python con victor robles'
        self.icon = './imagenes/raccon.ico'
        self.icon_alt = './21-tkinter/imagenes/raccon.ico'
        self.size= "750x450"
        self.resizable =False

    def cargar(self):
        
        #Crear la ventana raiz 

        ventana = Tk()
        self.ventana= ventana
        #titulo de la ventana 
        ventana.title(self.tittle)

        # Comprobar si existe un archivo 
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono= os.path.abspath(self.icon_alt)

        #icono de la ventana 
        ventana.iconbitmap(ruta_icono)

        # mostrar texto en el programa 
        texto = Label(ventana, text= ruta_icono)
        texto.pack()

        #Cambio en el tamaño de la ventana 
        ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana 
        if self.resizable:
            ventana.resizable(1,1)
        else: 
            ventana.resizable(0,0)

        
    
    def addTexto(self):
        texto = Label(self.ventana, text="Hola desde un metodo")
        texto.pack()
    
    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre 
        
        self.ventana.mainloop()
    
programa = Programa()
programa.cargar()
programa.addTexto()
programa.mostrar()