from tkinter import *
from turtle import right

ventana = Tk()
# ventana.geometry("700x600")

texto = Label(ventana, text="Bienvenido a mi programa")

texto.config(
            fg="white",
            bg="brown", 
            padx=50,
            pady=20,
           
)
texto.pack(side=TOP)




texto = Label(ventana, text="Basico")


texto.config(
            fg="white",
            bg="green", 
            padx=50,
            pady=20,
            
)
texto.pack(side=LEFT, fill=X, expand=YES)


texto = Label(ventana, text="Basico")


texto.config(
            fg="white",
            bg="black", 
            padx=50,
            pady=20,
            
)



texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Basico")


texto.config(
            fg="white",
            bg="gray", 
            padx=50,
            pady=20,
            
)



texto.pack(side=LEFT, fill=X, expand=YES)

# def pruebas(nombre, pais, anios):
#     return f'Hola esto es una prueba para {nombre} que vive en {pais} y tiene {anios} años'

# texto = Label(ventana, text=pruebas(nombre="Aldayr", pais="Mexico", anios='22'))
# texto.config(
#             height=3,
            
#             padx=10,
#             pady=20,
#             bg='gray'
# )
# texto.pack()


ventana.mainloop()
