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

# Ejecutar la ventana
ventana.mainloop()