def mostrar(lista):
	resultado = ""
	for i in lista:
		for j in i:
			resultado += j + " "
		resultado += "\n"
	return resultado 


def cjug1(elec,lista):
		print(lista)
		elec_val = ord(elec) - 65
		lista[elec_val // 3][elec_val % 3] = "X"
		return mostrar(lista)

def cjug2(elec,lista):
		elec_val = ord(elec) - 65
		lista[elec_val // 3][elec_val % 3] = "O"
		return mostrar(lista)

def ganador(lista):
	lista2= []
	suma= []
	for i in lista:
		suma_fila= []
		for j in i:
			if j == "X":
				suma_fila.append(1)
			elif j == "O":
				suma_fila.append(-1)	
			else:
				suma_fila.append(0)	
		suma.append(suma_fila)				

	suma_d1= 0
	suma_d2 = 0			
	
	for i in suma:
		lista2.append(sum(i))
	for i in range (3):
		lista2.append(suma[0][i] + suma[1][i] + suma[2][i])
	for i in range (3):
		suma_d1+= suma[i][i]
		suma_d2+= suma[i][2 - i] 
		lista2.append(suma_d1)
		lista2.append(suma_d2)

	if 3 in lista2:
		return "JUGADOR X GANO"
	elif -3 in lista2:
		return "JUGADOR O GANO"
	else:
		return " "	
