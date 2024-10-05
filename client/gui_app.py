import tkinter as tk
from tkinter import ttk
from model.eventos_dao import crear_tabla, borrar_tabla, listar


 
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height = 300)
    
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)

    menu_inicio.add_command(label='Crear Registro en DB', command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Registro en DB', command=borrar_tabla)
    menu_inicio.add_command(label='Salir', command=root.destroy)

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()

        self.tabla_log()

    

    def tabla_log(self):
        self.lista_eventos = listar()
        self.lista_eventos.reverse()
        self.tabla = ttk.Treeview(self,
        column = ('Descripcion de alarma', 'Zona', 'Fecha', 'Hora'))
        self.tabla.grid(row = 2, column = 0, columnspan=5, sticky = 'nse')

        #Scrollbar para la tabla
        self.scroll = ttk.Scrollbar(self,
        orient= 'vertical', command= self.tabla.yview)
        self.scroll.grid(row = 2, column = 5, sticky = 'nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)


        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Descripcion')
        self.tabla.heading('#2', text='Zona')
        self.tabla.heading('#3', text='Fecha')
        self.tabla.heading('#4', text='Hora')

        #Iterar la lista de películas
        for p in self.lista_eventos:
            self.tabla.insert('',0, text=p[0],
            values = (p[1], p[2], p[3], p[4]))
            #values = ('Alarma de Temp. Alta', 'Ensamble', '29/04/2024', '18:45'))