""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *

from tkinter import messagebox
 
ventana = Tk() # estamos instanciando la clase Tk (crear un objeto)

ventana.title("Mi calculadora")

ventana.geometry("400x280")

ventana.configure(background = "yellow")
 
# Creamos nuestras etiquetas (Label)
 
lblPrimerNumero = Label(ventana, text = "Primer número", bg = "yellow", fg = "black", font = ("Arial Bold", 15))

lblPrimerNumero.grid(row = 1, column = 1, padx = 5, pady = 5)
 
lblSegundoNumero = Label(ventana, text = "Segundo número", bg = "yellow", fg = "black", font = ("Arial Bold", 15))

lblSegundoNumero.grid(row = 2, column = 1, padx = 5, pady = 5)
 
# Creamos nuestas cajas de texto (Entry)
 
txtPrimerNumero = Entry(ventana, font = ("Arial Bold", 15), justify = CENTER)

txtPrimerNumero.grid(row = 1, column = 2, padx = 5, pady = 5)
 
txtSegundoNumero = Entry(ventana, font = ("Arial Bold", 15), justify = CENTER)

txtSegundoNumero.grid(row = 2, column = 2, padx = 5, pady = 5)
 
# Creamos una variables para el resultado
 
resultado = StringVar()
 
# Definimos las  funciones
 
def cerrar():
    
    ventana.destroy()
 
def suma():
    
    try:
    
        suma = int(txtPrimerNumero.get()) + int(txtSegundoNumero.get())
        
        return resultado.set(suma)
    
    except ValueError:
        
        messagebox.showinfo(title = "ERROR", message = "Datos ingresados incorrectos...!!!")
        
        txtPrimerNumero.delete(0, END)
        
        txtSegundoNumero.delete(0, END)
        
        txtPrimerNumero.focus()
 
def resta():
    
    try:
    
        resta = int(txtPrimerNumero.get()) - int(txtSegundoNumero.get())
        
        return resultado.set(resta)
    
    except ValueError:
        
        messagebox.showinfo(title = "ERROR", message = "Datos ingresados incorrectos...!!!")
        
        txtPrimerNumero.delete(0, END)
        
        txtSegundoNumero.delete(0, END)
        
        txtPrimerNumero.focus()
 
def muultiplicacion():
    
    try:
    
        multiplicacion = int(txtPrimerNumero.get()) * int(txtSegundoNumero.get())
        
        return resultado.set(multiplicacion)
    
    except ValueError:
        
        messagebox.showinfo(title = "ERROR", message = "Datos ingresados incorrectos...!!!")
        
        txtPrimerNumero.delete(0, END)
        
        txtSegundoNumero.delete(0, END)
        
        txtPrimerNumero.focus()
 
def division():
    
    try:
        
        division = int(txtPrimerNumero.get()) / int(txtSegundoNumero.get())
        
        return resultado.set(division)
    
    except ZeroDivisionError:
        
        messagebox.showinfo(title = "ERROR", message = "Datos ingresados incorrectos...!!!")
        
        txtPrimerNumero.delete(0, END)
        
        txtSegundoNumero.delete(0, END)
        
        txtPrimerNumero.focus()
        
    except ValueError:
        
        messagebox.showinfo(title = "ERROR", message = "Datos ingresados incorrectos...!!!")
        
        txtPrimerNumero.delete(0, END)
        
        txtSegundoNumero.delete(0, END)
        
        txtPrimerNumero.focus()
 
# Creamos nuestros botones (Button)
 
btnSuma = Button(ventana, text = "+", bg = "green", fg = "white", width = 12, font = ("Arial Bold", 15), command = suma)

btnSuma.grid(row = 3, column = 1, padx = 5, pady = 5)
 
btnResta = Button(ventana, text = "-", bg = "green", fg = "white", width = 12, font = ("Arial Bold", 15), command = resta)

btnResta.grid(row = 3, column = 2, padx = 5, pady = 5)
 
btnMultiplicacion = Button(ventana, text = "*", bg = "green", fg = "white", width = 12, font = ("Arial Bold", 15), command = muultiplicacion)

btnMultiplicacion.grid(row = 4, column = 1, padx = 5, pady = 5)
 
btnDivision = Button(ventana, text = "/", bg = "green", fg = "white", width = 12, font = ("Arial Bold", 15), command = division)

btnDivision.grid(row = 4, column = 2, padx = 5, pady = 5)
 
btnCerrar = Button(ventana, text = "Cerrar", bg = "gray", fg = "white", width = 33, font = ("Arial Bold", 15), command = cerrar)

btnCerrar.grid(row = 5, column = 1, padx = 5, pady = 5, columnspan = 2)
 
# Creamos una etiqueta para el resultado (Label)
 
lblResultado = Label(ventana, bg = "white", width = 33, font = ("Arial Bold", 15), textvariable = resultado)

lblResultado.grid(row = 6, column= 1, padx = 5, pady = 5, columnspan = 2)
 
ventana.mainloop()