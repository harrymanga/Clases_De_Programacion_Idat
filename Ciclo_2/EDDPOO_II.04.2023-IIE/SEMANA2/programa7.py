""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *

ventana = Tk() # instanciando (crear un objeto) de la clase Tk()

ventana.title("Mi ventana")

ventana.geometry("750x200")

etiqueta = Label(ventana, text = "Hola", font = ("Arial Bold", 20))

etiqueta.grid(column = 0, row =0)

def click():
    
    etiqueta.configure(text = "Hisiste click en el boton...!!!")
    
boton = Button(ventana, text = "Clic aqui ...!!!", bg = "orange", fg = "red", command = click)

boton.grid(column = 1, row = 0)

texto = Entry(ventana, width = 20)

texto.grid(column = 2, row = 0)

ventana.mainloop()