import tkinter as tk
window = tk.Tk()
element = tk.StringVar()
list = tk.Listbox(window)

label = tk.Label(text="Dias de la Semana")
label.pack()

for item in ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]:
    list.insert(tk.END, item)

list.pack()
window.mainloop()
