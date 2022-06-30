from tkinter import *
from tkinter import messagebox as MessageBox
ventana = Tk()

ventana.config(
    bd=70
)

def sacarAlerta():
    MessageBox.showinfo("Alerta", "Hola soy una alerta")


Button(ventana, text="Mostrar alerta", command=sacarAlerta).pack()


def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "¿Quieres continuar ejecutando la aplicacion?")

    if resultado != "yes":
        MessageBox.showinfo("Adios",f'hasta luego {nombre}')
        ventana.destroy()


Button(ventana, text="Salir", command=lambda: salir("Aldayr")).pack()

ventana.mainloop()