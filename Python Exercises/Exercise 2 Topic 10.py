import tkinter

window = tkinter.Tk()


lista = ['Python', 'Java', 'C#','C++','JavaScrip']
lista_items = tkinter.StringVar(value=lista)
listBox = tkinter.Listbox(window, height=7, listvariable=lista_items )
listBox.grid(column=0, row=0, sticky=tkinter.W)

label1 = tkinter.Label(window, text='¡Soy una etiqueta!', bg='black', fg='red')
label1.grid(column=0, row=1, sticky=tkinter.W)

window.mainloop()