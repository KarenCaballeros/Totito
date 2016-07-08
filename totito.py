import funciones
lista= [["a","b","c"],
		["d","e","f"],
		["g","h","i"]
		]
print("Bienvenido a totito.")
print(funciones.mostrar(lista))	

print("Jugador X ")
elec= input("Ingrese la letra de la ubicacion deseada: ")
print(funciones.cjug1(elec,lista))
print("Jugador O ")
elec= input("Ingrese la letra de la ubicacion deseada: ")
print(funciones.cjug2(elec,lista))
print(funciones.gano(lista))

cont = 4
while cont >= 0:
	print("Jugador X ")
	elec= input("Ingrese la letra de la ubicacion deseada: ")
	print(funciones.cjug1(elec,lista))
	print(funciones.gano(lista))
	print("Jugador O ")
	elec= input("Ingrese la letra de la ubicacion deseada: ")
	print(funciones.cjug2(elec,lista))
	print(funciones.gano(lista))
	cont= cont -1




	