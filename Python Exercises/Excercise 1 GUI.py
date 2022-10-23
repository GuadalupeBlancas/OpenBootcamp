import tkinter
from tkinter import *

def seleccionar():
    if opcion.get() == 1:
        monitor.configure(text='opcion 1')
    if opcion.get() == 2:
        monitor.configure(text='opcion 2')
    if opcion.get() == 3:
        monitor.configure(text='opcion 3')
    if opcion.get() == 4:
        monitor.configure(text='opcion 4')

def reset():
    opcion.set(None)
    monitor.config(text='')

window = tkinter.Tk()
opcion = tkinter.IntVar()

r1 = tkinter.Radiobutton(window, text='si', value=1, variable=opcion, command=seleccionar)
r2 = tkinter.Radiobutton(window, text='No', value=2, variable=opcion, command=seleccionar)
r3 = tkinter.Radiobutton(window, text='sip', value=3, variable=opcion, command=seleccionar)
r4 = tkinter.Radiobutton(window, text='Nop', value=4, variable=opcion, command=seleccionar)

r1.grid(column=0, row=1, padx=5, pady=5)
r2.grid(column=0, row=2, padx=5, pady=5)
r3.grid(column=0, row=3, padx=5, pady=5)
r4.grid(column=0, row=4, padx=5, pady=5)

monitor = tkinter.Label(window)
monitor.grid(column=0, row=5, padx=5, pady=5)

boton = tkinter.Button(window, text='Haz clic sobre mi', command=reset)
boton.grid(column=0, row=6, padx=5, pady=5)

window.mainloop()