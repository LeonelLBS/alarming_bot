def MensajesAlarmas(url,mensaje):
	f = open(url,"r")
	data = f.readlines()
	f.close()
	#print(data)
	for line in data:
		mensaje.append(line.rstrip())
		print(line.rstrip())

	return mensaje
