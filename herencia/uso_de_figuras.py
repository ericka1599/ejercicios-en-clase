from cuadrado import Cuadrado
from triangulo import Triangulo

des = True

while des == True:

	elec = int(input(" 1. Crear una figura \n 2. Salir \n"))

	if elec == 1:
		de = int(input(" 1. Crear un triangulo \n 2. Crear un cuadrado \n 3. Salir \n"))

		if de == 1:
			trb= int(input("Ingrese la base: "))
			tra = int(input("Ingrese la altura: "))
			tr = Triangulo (trb , tra)

			print ("Area: ", tr.calcular_area())
			print (tr.imprimir())


		elif de == 2:
			cul= int(input("Ingrese el lado del cuadrado: "))
			cu = Cuadrado(cul)

			print ("Area: ", cu.calcular_area())
			print (cu.imprimir())

		elif de == 3: 
			des = False
			print ("Ok bye c:")

		else:
			print ("Eso no era una opcion ._.")

	elif elec == 2:

		des = False
		print ("Adios")

	else:
		print ("Elegi otro numero ._.")
