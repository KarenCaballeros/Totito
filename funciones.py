def mostrar(lista):
	print(lista[0])
	print(lista[1])
	print(lista[2])	
	return "  "

def cjug1(elec,lista):
		if elec == "a":
			lista[0][0] = "X"
			return mostrar(lista)
		elif elec == "b":
			lista[0][1] = "X"
			return mostrar(lista)
		elif elec == "c":
			lista[0][2] = "X"	
			return mostrar(lista)
		elif elec == "d":
			lista[1][0] = "X"	
			return mostrar(lista)
		elif elec == "e":
			lista[1][1] = "X"	
			return mostrar(lista)
		elif elec == "f":
			lista[1][2] = "X"
			return mostrar(lista)
		elif elec == "g":
			lista[2][0] = "X"	
			return mostrar(lista)
		elif elec == "h":
			lista[2][1] = "X"
			return mostrar(lista)
		elif elec == "i":
			lista[2][2] = "X"
			return mostrar(lista)
		else:
			return "Error"	

def cjug2(elec,lista):
		if elec == "a":
			lista[0][0] = "O"
			return mostrar(lista)
		elif elec == "b":
			lista[0][1] = "O"
			return mostrar(lista)
		elif elec == "c":
			lista[0][2] = "O"	
			return mostrar(lista)
		elif elec == "d":
			lista[1][0] = "O"	
			return mostrar(lista)
		elif elec == "e":
			lista[1][1] = "O"	
			return mostrar(lista)
		elif elec == "f":
			lista[1][2] = "O"
			return mostrar(lista)
		elif elec == "g":
			lista[2][0] = "O"	
			return mostrar(lista)
		elif elec == "h":
			lista[2][1] = "O"
			return mostrar(lista)
		elif elec == "i":
			lista[2][2] = "O"
			return mostrar(lista)
		else:
			return "Error"					
	
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