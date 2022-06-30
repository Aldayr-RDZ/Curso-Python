from tkinter import *
from turtle import right

ventana = Tk()
ventana.geometry("700x600")

texto = Label(ventana, text="Bienvenido a mi programa")

texto.config(
            fg="white",
            bg="black", 
            padx=50,
            pady=20,
            font=('Consolas', 30)
)


texto.pack()

def pruebas(nombre, pais, anios):
    return f'Hola esto es una prueba para {nombre} que vive en {pais} y tiene {anios} años'

texto = Label(ventana, text=pruebas(nombre="Aldayr", pais="Mexico", anios='22'))
texto.config(
            height=3,
            font=("Arial", 10),
            padx=10,
            pady=20,
            bg='green'
)
texto.pack()


ventana.mainloop()
