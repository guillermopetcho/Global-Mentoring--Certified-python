import tkinter as tk
from tkinter import ttk, messagebox

# ventana principal
ventana = tk.Tk()
ventana.geometry('300x130')
ventana.title('Login')
ventana.iconbitmap('icono.ico')
ventana.resizable(0,0)

# configuración del grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=3)

# usuario
usuario_etiqueta = ttk.Label(ventana, text='Usuario:')
usuario_etiqueta.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
usuario_entrada = ttk.Entry(ventana)
usuario_entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

# password
password_etiqueta = ttk.Label(ventana, text='Password:')
password_etiqueta.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
password_entrada = ttk.Entry(ventana, show='*')
password_entrada.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

# boton Login
def login():
    messagebox.showinfo('Datos Login',
                        f'usuario: {usuario_entrada.get()}, Password: {password_entrada.get()}')

login_boton = ttk.Button(ventana, text='Login', command=login)
login_boton.grid(row=3, column=0, columnspan=2)

# Ejecutar la ventana
ventana.mainloop()