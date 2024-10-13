import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Componentes')
ventana.iconbitmap('icono.ico')

def crear_tabs():
    # Creamos un tab control, para ello usamos la clase Notebook
    control_tabulador = ttk.Notebook(ventana)

    # Agregamos un marco (frame) para agregar dentrol del tab y organizar elementos
    tabulador1 = ttk.Frame(control_tabulador)
    # Agregamos el tabulador al control de tabuladores
    control_tabulador.add(tabulador1, text='Tabulador 1')
    # Mostramos el tabulador
    control_tabulador.pack(fill='both')

    # Agregar una etiqueta y un componente de entrada
    etiqueta1 = ttk.Label(tabulador1, text='Nombre:')
    etiqueta1.grid(row=0, column=0, sticky=tk.E)
    entrada1 = ttk.Entry(tabulador1, width=30)
    entrada1.grid(row=0, column=1, padx=5, pady=5)
    # Agregamos un botón
    def enviar():
        messagebox.showinfo('Mensaje', f'Nombre: {entrada1.get()}')
    boton1 = ttk.Button(tabulador1, text='Enviar', command=enviar)
    boton1.grid(row=1, column=0, columnspan=2)

crear_tabs()

ventana.mainloop()