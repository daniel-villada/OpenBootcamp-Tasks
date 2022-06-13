import random
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Primer GUI en Python")

#Geometria con pack
#label1 = tk.Label(window, text='Label1', bg='black', fg='white')
#label1.pack(ipadx=45, ipady=10, fill='x')

#label2 = tk.Label(window, text='Label2', bg='purple', fg='white')
#label2.pack(ipadx=45, ipady=10, fill='x')

#Geometria con Grid

#window.columnconfigure(0, weight=1)
#window.columnconfigure(1, weight=3)

#username = ttk.Label(window, text='Username: ')
#username.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
#username_entry = ttk.Entry(window)
#username_entry.grid(column=1, row=0, sticky=tk.W, pady=5, padx=5)

#password = ttk.Label(window, text='Password: ')
#password.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
#password_entry = ttk.Entry(window, show='*')
#password_entry.grid(column=1, row=1, sticky=tk.W, pady=5, padx=5)

#boton
#boton = ttk.Button(window, text="Login")
#boton.grid(column=1, row=3, sticky=tk.W, pady=5, padx=5)
#mantiene la ventana abierta

#Geometria con place


colors = ['blue', 'red', 'yellow', 'purple', 'white']

for x in range(0, 10):
    color = random.randint(0, len(colors)-1)
    color2 = random.randint(0, len(colors)-1)
    label = ttk.Label(window, text='etiqueta', background=colors[color], foreground=colors[color2])
    label.place(x=random.randint(0, 100), y=random.randint(0, 100))

window.mainloop()