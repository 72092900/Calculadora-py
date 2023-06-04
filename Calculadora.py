from tkinter import *
from typing import TextIO

ventana = Tk()
ventana.title("Calculadora")

i = 0

texto = Entry(ventana, font=("Fantacy 34"))
texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


def click_boton(valor):
    global i
    texto.insert(i, valor)
    i += 1

def borrar():
    texto.delete(0, END)
    i = 1

def operacion():
    ecuacion = texto.get()
    resultado = eval(ecuacion)
    texto.delete(0, END)
    texto.insert (0, resultado)
    i = 0
        

boton1 = Button(ventana, text="1", font=("Fantacy 25"), width=5, height=0, command = lambda: click_boton(1))
boton2 = Button(ventana, text="2", font=("Fantacy 25"), width=5, height=0, command = lambda: click_boton(2))
boton3 = Button(ventana, text="3", font=("Fantacy 25"), width=5, height=0, command = lambda: click_boton(3))
boton4 = Button(ventana, text="4", font=("Fantacy 25"), width=5, height=0, command = lambda: click_boton(4))
boton5 = Button(ventana, text="5", font=("Fantacy 25"), width=5, height=0, command = lambda: click_boton(5))
boton6 = Button(ventana, text="6", font=("Fantacy 25"), width=5, height=0, command = lambda: click_boton(6))
boton7 = Button(ventana, text="7", font=("Fantacy 25"), width=5, height=0, command = lambda: click_boton(7))
boton8 = Button(ventana, text="8", font=("Fantacy 25"), width=5, height=0, command = lambda: click_boton(8))
boton9 = Button(ventana, text="9", font=("Fantacy 25"), width=5, height=0, command = lambda: click_boton(9))
boton0 = Button(ventana, text="0", font=("Fantacy 25"), width=12, height=0, command = lambda: click_boton(0))

boton_borrar = Button(ventana, text="Borrar", font=("Fantacy 25"), width=5, height=0, command = lambda: borrar())
boton_parentesis1 = Button(ventana, text="(", font=("Fantacy 25"), width=5, height=0, command = lambda: click_boton("("))
boton_parentesis2 = Button(ventana, text=")", font=("Fantacy 25"), width=5, height=0, command = lambda: click_boton(")"))
boton_punto = Button(ventana, text=".", font=("Fantacy 25"), width=5, height=0, command = lambda: click_boton("."))

boton_suma = Button(ventana, text="+", font=("Fantacy 25"), width=5, height=0, command = lambda: click_boton("+"))
boton_Resta = Button(ventana, text="-", font=("Fantacy 25"), width=5, height=0, command = lambda: click_boton("-"))
boton_Multiplicacion = Button(ventana, text="x", font=("Fantacy 25"), width=5, height=0, command = lambda: click_boton("*"))
boton_Divicion = Button(ventana, text="÷", font=("Fantacy 25"), width=5, height=0, command = lambda: click_boton("/"))
boton_igual = Button(ventana, text="=", font=("Fantacy 25"), width=5, height=0, command = lambda: operacion())


boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_Divicion.grid(row=1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_Multiplicacion.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_Resta.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_suma.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
boton_punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)


ventana.mainloop()