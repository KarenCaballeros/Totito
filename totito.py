import funciones
print("BIENVENIDO A TOTITO!")
menu= 1
while menu != 2:

	if menu == 1:
		
		lista= [["A","B","C"],
			["D","E","F"],
			["G","H","I"]]
		print(funciones.mostrar(lista))
		
		print("Jugador X ")
		elec= input("Ingrese la letra de la ubicacion deseada: ")
		print(funciones.cjug1(elec.upper(),lista))
		print(funciones.ganador(lista))

		cont = 4
		while cont > 0:

			if funciones.ganador(lista) != "JUGADOR X GANO" and funciones.ganador(lista) != "JUGADOR O GANO" :
				print("Jugador O ")
				elec= input("Ingrese la letra de la ubicacion deseada: ")
				print(funciones.cjug2(elec.upper(),lista))
				print(funciones.ganador(lista))
			
				if funciones.ganador(lista) != "JUGADOR O GANO" :
					print("Jugador X ")
					elec= input("Ingrese la letra de la ubicacion deseada: ")
					print(funciones.cjug1(elec.upper(),lista))
					print(funciones.ganador(lista))
				
			cont= cont - 1 		
	

		print("Si desea jugar de nuevo presione 1.")
		print("Si desea salir presione 2.")
		menu= int(input("Presione el numero de su eleccion: "))		

	elif menu == 2:
		print("Gracias por jugar!")		

	else:
		print("Opcion invalida.")
		print("Si desea jugar de nuevo presione 1.")
		print("Si desea salir presione 2.")
		menu= int(input("Presione el numero de su eleccion: "))	

	

		