from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from model.eventos_dao import Evento, guardar

def controlTime(mensaje,contacto,hora,wait):
	global m
	minutos = int(hora[len(hora)-2]+hora[len(hora)-1])
	cond = (minutos == 0 or minutos % 5 == 0 ) and m == 0
	if cond:
		try:
			m = 1
			grupo_path = '//span[contains(@title,'+ contacto +')]'
			grupo = wait.until(EC.presence_of_element_located((By.XPATH,grupo_path)))
			grupo.click()
			message_box_path='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]'
			message_box=wait.until(EC.presence_of_element_located((By.XPATH,message_box_path)))
			message_box.send_keys(mensaje + Keys.ENTER)
			print("Valor:", m)
			print(minutos)
			print(mensaje)

		except:
			m = 0
			print("error en el envio")
			print(m)
	elif not(minutos == 0 or minutos % 5 == 0 ):
		m = 0
		print(minutos)
		print("Estoy aca")
def evento_alrm(descripcion,zona,hora,fecha):
	global n
	minutos2 = int(hora[len(hora)-2]+hora[len(hora)-1])
	cond2 = (minutos2 == 0 or minutos2 % 5 == 0 ) and n == 0
	if cond2:
		n = 1
		print('Quiero escribir el la DB')
		evento = Evento(
			descripcion,
			zona,
			fecha,
			hora,
			)
		guardar(evento)

	elif not(minutos2 == 0 or minutos2 % 5 == 0 ):
		n = 0
		print('No estoy en la DB')
	return n