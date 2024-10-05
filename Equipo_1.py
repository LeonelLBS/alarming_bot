from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from OPC_read_write import read_input_value
import snap7
import snap7.client as c
from snap7.util import *
from snap7.types import *
#from snap7.common import ADict


w = [0,0,0,0,0,0,0,0,0,0] 

#----------------- Metodos --------------------#
def sendAviso(data, byte, bit, contacto, mensaje, n,wait):
	global w

	Alarm = get_bool(data,byte,bit)

	if Alarm == True and w[n] == 0:
		try:
			w[n] = 1
			#pywhatkit.sendwhatmsg_to_group_instantly("L1n0zzsjhxf7DA19pRRIDp",mensaje,14,True,20)
			grupo_path = '//span[contains(@title,'+ contacto +')]'
			grupo = wait.until(EC.presence_of_element_located((By.XPATH,grupo_path)))
			grupo.click()
			message_box_path='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]'
			message_box=wait.until(EC.presence_of_element_located((By.XPATH,message_box_path)))
			message_box.send_keys(mensaje + Keys.ENTER)
			print("Valor:", w[n])
			print(mensaje)

		except:
			w[n] = 0
			print("error en el envio")
			print(w[n])
	elif Alarm == True:
		w[n] = 0
		print("fin")

def automata_1(mensajes,contacto,wait):		#def automata_1(En_Linea,plcEquipo_1,mensajes,contacto,wait):
	
	try:		

		plcEquipo_1 = c.Client()
		plcEquipo_1.connect('192.168.10.50',0,0) 

		#----------------- Conexion al Equipo1 - Estatus --------------------#
		Estatus = plcEquipo_1.get_cpu_state()
		print("Estatus PLC :", Estatus)

		En_Linea = plcEquipo_1.get_connected()
		print("PLC Online:", En_Linea)
		data1 = plcEquipo_1.read_area(Areas['DB'],1,0,1)
	except:
		En_Linea = False
	
	if En_Linea == False:
		try:
			plcEquipo_1 = c.Client()
			plcEquipo_1.connect('192.168.10.50',0,0) #estructura metodo connect: plcEquipo_1.connect('IP del PLC', Rack , slot)
		except:
			En_Linea = False
			print('Estatus Equipo 1: ',En_Linea)
	if En_Linea ==True:
		try:
			data1 = plcEquipo_1.read_area(Areas['DB'],1,0,1)	
			print("try")
			pass

		except:
	#------------------ Mensajes Datos DBXX--------------------#
			sendAviso(data1,0,0,contacto,mensajes[0],0,wait)

		sendAviso(data1,0,0,contacto,mensajes[0],0,wait)

	
	
#def automata_01():
