from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import snap7.client as c
from snap7.util import *
from snap7.types import *
from datetime import datetime
from time import sleep
from MensajesTXT import MensajesAlarmas
from MsgPeriodico import controlTime, evento_alrm
import tkinter as tk
from client.gui_app import barra_menu, Frame
from model.eventos_dao import crear_tabla, borrar_tabla

from Equipo_1 import automata_1
import threading
from opcua import Client, ua
from OPC_read_write import read_input_value as rinvalue


def periodical():
	while True:
		hora = datetime.now()
		fecha = datetime.today()
		horaActual = hora.strftime("%H:%M")
		fechaActual = fecha.strftime("%d/%m/%Y")
		print(horaActual)
		print(fechaActual)
		
				
		'''
		try:
			plcEquipo_1 = c.Client()
			plcEquipo_1.connect('192.168.10.50',0,0) 

			#----------------- Conexion Horno Glasston - Estatus --------------------#
			Estatus = plcEquipo_1.get_cpu_state()
			print("Estatus PLC :", Estatus)

			En_Linea = plcEquipo_1.get_connected()
			print('Estado de alarmas')
			print("PLC Online:", En_Linea)
			data1 = plcEquipo_1.read_area(Areas['DB'],1,0,2)
			print('Valor obtenido del PLC:', data1)
			#Alarm01 = get_bool(data1,0,0)
			#Alarm02 = get_bool(data1,0,1)
			#Alarm03 = get_bool(data1,0,2)
			#Alarm04 = get_bool(data1,0,3)
			#Alarm05 = get_bool(data1,0,4)
			#Alarm06 = get_bool(data1,0,5)
			#Alarm07 = get_bool(data1,0,6)
			#Alarm08 = get_bool(data1,0,7)
			#Alarm09 = get_bool(data1,1,0)
			Alarm10 = get_bool(data1,1,1)
			#Alarm11 = get_bool(data1,1,2)
			#Alarm12 = get_bool(data1,1,3)
			#Alarm13 = get_bool(data1,1,4)
			#Alarm14 = get_bool(data1,1,5)
			#Alarm15 = get_bool(data1,1,6)
			#Alarm16 = get_bool(data1,1,7)
			print('Estado de alarma01: ', Alarm10, sep='\n')
			
		except:
			print('Error')
			En_Linea = False
			'''
		
		rinvalue('ns=4;i=5')


		controlTime(mensajes_2, contacto,horaActual,wait)						#Mensaje peripodico Bot Operativo - Online
		event = evento_alrm(mensajes_2, mensajes_3, horaActual, fechaActual)	#Añade mensaje de alarma a la base de datos
		if event == 1:
			app.tabla_log()														#Actualziamos la tabla de alarmas
		sleep(10)

#----------------- Inicio de Ciclo --------------------#

if __name__ == '__main__':
	#-------------------Abriendo wspp-----------------------------
	chrome_options = Options()
	chrome_options.add_argument("user-data-dir=C:/Users/LEONEL/AppData/Local/Google/ChromeUser Data")
	driver = webdriver.Chrome(options=chrome_options)
	print('Estoy aqui')
	driver.get('https://web.whatsapp.com')
	global wait
	wait = WebDriverWait(driver,2000)
	#driver.quit()

	#-------------------Grupo de wspp que recibirá mensajes-----------------------------
	#contacto = '"☀️🏖️⛱️🕶️FIEE G4 - Modo Verano-2024"'
	contacto = '"LBS BOT"'


	#----------------- Mensajería a enviar --------------------#
	mensajes_1 = []
	mensajes_2 = "Aviso: Bot Operativo - Online"
	mensajes_3 = "Zona Corte Laser"
	mensajes = MensajesAlarmas("C:/Users/LEONEL/OneDrive - Universidad Nacional Mayor de San Marcos/Documents/Bot_Project/03. 060424/2_python_L/GeneralAlarms.txt", mensajes_1)

	#---------------------OPC Client------------------------#
	client = Client('opc.tcp://192.168.10.50:4840')
	try:
		client.connect()
		root = client.get_root_node()
		print('Object root is: ', root)
	except:
		print('Error en la conexión OPC')

	#----------------- Interfaz gráfica --------------------#
	root = tk.Tk()
	root.title('LBS Log')     
	root.iconbitmap('img/LBS_PERFIL.ico')      #Para modificar el ícono de la ventana
	root.resizable(1,1) 
	barra_menu(root)  
	app = Frame(root=root)
	#----------------- Creación de tabla en DB --------------------#
	try:
		crear_tabla()
	except:
		pass

	hilo = threading.Thread(target=periodical).start()		#Hilo para el bot
	
	app.mainloop()