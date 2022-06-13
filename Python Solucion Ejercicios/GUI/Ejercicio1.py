# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga
# un botón de reinicio para que deje todo como al principio.
# Al principio no tiene que haber una opción seleccionada.

import tkinter as tk

def getValor():
    window.config(text='{}'.format(opt.get()))

def reset():
    opt.set(None)
    window.config(text='')

window = tk.Tk()
window.title("Ejercicio 1")
opt = tk.IntVar()

rad1 = tk.Radiobutton(window, text='Enero', variable=opt, value=1, command=getValor).pack(anchor='w')
rad2 = tk.Radiobutton(window, text='Febrero', variable=opt, value=2, command=getValor).pack(anchor='w')
rad3 = tk.Radiobutton(window, text='Marzo', variable=opt, value=3, command=getValor).pack(anchor='w')
rad4 = tk.Radiobutton(window, text='Abril', variable=opt, value=4, command=getValor).pack(anchor='w')

window = tk.Label(window)
window.pack(anchor='w')
btn = tk.Button(window, text="Reiniciar", command=reset).pack()




window.mainloop()
