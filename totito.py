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
		print(funciones.gano(lista))

		cont = 4
		while cont > 0:

			if funciones.gano(lista) != "JUGADOR X GANO" and funciones.gano(lista) != "JUGADOR O GANO" :
				print("Jugador O ")
				elec= input("Ingrese la letra de la ubicacion deseada: ")
				print(funciones.cjug2(elec.upper(),lista))
				print(funciones.gano(lista))
			
				if funciones.gano(lista) != "JUGADOR O GANO" :
					print("Jugador X ")
					elec= input("Ingrese la letra de la ubicacion deseada: ")
					print(funciones.cjug1(elec,lista))
					print(funciones.gano(lista))
				
			cont= cont - 1 		
	

		print("Si desea jugar de nuevo presione 1.")
		print("Si desea salir presione 2.")
		menu= int(input("Presione el numero de su eleccion: "))		



	else:
		print("Opcion invalida.")	

	print("Gracias por jugar!")	
	

		