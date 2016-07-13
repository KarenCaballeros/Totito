def mostrar(lista):
	resultado = ""
	for i in lista:
		for j in i:
			resultado += j + " "
		resultado += "\n"
	return resultado 


def cjug1(elec,lista):
		elec_val = ord(elec) - 65
		lista[elec_val // 3][elec_val % 3] = "X"
		return mostrar(lista)

def cjug2(elec,lista):
		elec_val = ord(elec) - 65
		lista[elec_val // 3][elec_val % 3] = 'O'
		return mostrar(lista)

def gano(lista):
	
	if lista[0][0] == lista[0][1] and lista[0][0] == lista[0][2]:
		if lista[0][0] == "X":
			return "JUGADOR X GANO"
		elif lista[0][0] == "O":
			return "JUGADOR O GANO"	

	elif lista[1][0] == lista[1][1] and lista[1][0] == lista[1][2]:
		if lista[1][0] == "X":
			return "JUGADOR X GANO"
		elif lista[1][0] == "O":
			return "JUGADOR O GANO"
	
	elif lista[2][0] == lista[2][1] and lista[2][0] == lista[2][2]:
		if lista[2][0] == "X":
			return "JUGADOR X GANO"
		elif lista[2][0] == "O":
			return "JUGADOR O GANO"

	elif lista[0][0] == lista[1][0] and lista[0][0] == lista[2][0]:
		if lista[0][0] == "X":
			return "JUGADOR X GANO"
		elif lista[0][0] == "O":
			return "JUGADOR O GANO"

	elif lista[0][1] == lista[1][1] and lista[0][1] == lista[2][1]:
		if lista[0][1] == "X":
			return "JUGADOR X GANO"
		elif lista[0][1] == "O":
			return "JUGADOR O GANO"

	elif lista[0][2] == lista[1][2] and lista[0][2] == lista[2][2]:
		if lista[0][2] == "X":
			return "JUGADOR X GANO"
		elif lista[0][2] == "O":
			return "JUGADOR O GANO"

	elif lista[0][0] == lista[1][1] and lista[0][0] == lista[2][2]:
		if lista[0][0] == "X":
			return "JUGADOR X GANO"
		elif lista[0][0] == "O":
			return "JUGADOR O GANO"

	elif lista[0][2] == lista[1][1] and lista[0][2] == lista[2][0]:
		if lista[0][2] == "X":
			return "JUGADOR X GANO"
		elif lista[0][2] == "O":
			return "JUGADOR O GANO"	
	else:
		return ""

	
def get_ganador(totito):
		sumas= []
		MAGIA
		sumas=[5446545465]
		if 3 in sumas:
			return"X Gano"
		elif -3 in sumas:
			return "O gano"
		else:
			return "Nadie Gano"			