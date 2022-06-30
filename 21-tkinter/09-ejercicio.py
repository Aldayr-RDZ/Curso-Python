"""
Calculadora 
--Dos campos de texto 
--4 botones para las operaciones 
--Mostrar el resulado en una alerta

"""


from tkinter import *
from tkinter import messagebox


ventana = Tk()
ventana.title("Ejercicio completo con Tkinter | Aldayr-RDZ")
ventana.geometry("400x400")
ventana.config(bd=25,)

def cFloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        messagebox.showerror("Error", "Introduce bien los datos")

    return result

def sumar():
    try:
        resultado.set(cFloat(numero1.get()) + cFloat(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce bien los datos")
    

def restar():
    try:
        resultado.set(cFloat(numero1.get()) - cFloat(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce bien los datos")
    

def multiplicar():
    try:
        resultado.set(cFloat(numero1.get()) * cFloat(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce bien los datos")
    
    

def dividir():
    try:
        resultado.set(cFloat(numero1.get()) / cFloat(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce bien los datos")
    



def mostrarResultado():
    messagebox.showinfo("Resultado", f"El resultado de la operecion es: {resultado.get()}")
    numero1.set("")
    numero2.set("")


numero1= StringVar()
numero2= StringVar()
resultado = StringVar()

marco = Frame(ventana, width=340, height=200)
marco.config(
    bd=5,
    relief=SOLID
    
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer numero").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo numero").pack()
Entry(marco, textvariable=numero2,justify="center").pack()

Label(marco, text='').pack()

Button(marco, text="Sumar", command=sumar).pack(side='left', fill= X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side='left', fill= X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side='left', fill= X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side='left', fill= X, expand=YES)

ventana.mainloop()