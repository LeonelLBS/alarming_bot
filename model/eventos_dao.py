from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE eventos(
        id_evento INTEGER,
        descripcion VARCHAR(100),
        zona VARCHAR(20),
        fecha VARCHAR(10),
        hora VARCHAR(10),
        PRIMARY KEY(id_evento AUTOINCREMENT)
    )
    '''

    conexion.cursor.execute(sql)
    conexion.cerrar()

def borrar_tabla():
    conexion = ConexionDB()

    sql = 'DROP TABLE eventos'
    conexion.cursor.execute(sql)
    conexion.cerrar()

class Evento:
    def __init__(self, descripcion, zona, fecha, hora):
        self.id_evento = None
        self.descripcion = descripcion
        self.zona = zona
        self.fecha = fecha
        self.hora = hora
    
    def __str__(self):
        return f'Evento[{self.descripcion}, {self.zona}, {self.fecha}, {self.hora}]'

def guardar(evento):
    conexion = ConexionDB()

    sql = f'''INSERT INTO eventos (descripcion, zona, fecha, hora)
    VALUES('{evento.descripcion}', '{evento.zona}', '{evento.fecha}', '{evento.hora}')'''

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo ='Conexion al Registro'
        mensaje = 'La tabla peliculas no está creado en la base de datos'
        messagebox.showerror(titulo, mensaje)

def listar():
    conexion = ConexionDB()
    
    lista_eventos = []
    sql = 'SELECT * FROM eventos'
    
    try:
        conexion.cursor.execute(sql)
        lista_eventos = conexion.cursor.fetchall()
        conexion.cerrar
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Crea la tabla en la Base de Datos'
        messagebox.showerror(titulo, mensaje)
    return lista_eventos