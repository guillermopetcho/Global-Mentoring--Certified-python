import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Componentes')
ventana.iconbitmap('icono.ico')

def crear_componentes_tabulador1(tabulador):
    # Agregar una etiqueta y un componente de entrada
    etiqueta1 = ttk.Label(tabulador, text='Nombre:')
    etiqueta1.grid(row=0, column=0, sticky=tk.E)
    entrada1 = ttk.Entry(tabulador, width=30)
    entrada1.grid(row=0, column=1, padx=5, pady=5)

    # Agregamos un botón
    def enviar():
        messagebox.showinfo('Mensaje', f'Nombre: {entrada1.get()}')

    boton1 = ttk.Button(tabulador, text='Enviar', command=enviar)
    boton1.grid(row=1, column=0, columnspan=2)

def crear_componentes_tabulador2(tabulador):
    contenido = 'Este es mi texto con el contenido'
    # Creamos el componente de scroll
    scroll = scrolledtext.ScrolledText(tabulador, width=50, height=10, wrap=tk.WORD)
    scroll.insert(tk.INSERT, contenido)
    # Mostramos el componente
    scroll.grid(row=0, column=0)

def crear_componentes_tabulador3(tabulador):
    # Creamos una lista usando data list comprehensions
    datos = [x+1 for x in range(100, 110)]
    combobox = ttk.Combobox(tabulador, width=15, values=datos)
    combobox.grid(row=0, column=0, padx=10, pady=10)
    # Seleccionamos un elemento por default a mostrar
    combobox.current(5)
    # Agregar un boton para saber que opción seleccionó el usuario
    def mostrar_valor():
        messagebox.showinfo('Valor seleccionado', f'Valor seleccionado: {combobox.get()}')

    boton1 = ttk.Button(tabulador, text='Mostrar valor Seleccionado', command=mostrar_valor)
    boton1.grid(row=0, column=1)

def crear_tabs():
    # Creamos un tab control, para ello usamos la clase Notebook
    control_tabulador = ttk.Notebook(ventana)
    # Agregamos un marco (frame) para agregar dentrol del tab y organizar elementos
    tabulador1 = ttk.Frame(control_tabulador)
    # Agregamos el tabulador al control de tabuladores
    control_tabulador.add(tabulador1, text='Tabulador 1')
    # Mostramos el tabulador
    control_tabulador.pack(fill='both')
    # Creamos los componentes del tabulador1
    crear_componentes_tabulador1(tabulador1)
    # Creamos un segundo tabulador
    tabulador2 = ttk.LabelFrame(control_tabulador, text='Contenido')
    control_tabulador.add(tabulador2, text='Tabulador 2')
    # Creamos los componentes del segundo tabulador
    crear_componentes_tabulador2(tabulador2)
    # Crear un tercer tabulador
    tabulador3 = ttk.Frame(control_tabulador)
    control_tabulador.add(tabulador3, text='Tabulador 3')
    # Creamos los componentes del tercer tabulador
    crear_componentes_tabulador3(tabulador3)

crear_tabs()

ventana.mainloop()