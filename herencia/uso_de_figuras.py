from cuadrado import Cuadrado
from triangulo import Triangulo

des = True

while des == True:

	elec = int(input("1. Crear una figura \n 2. Salir \n"))

	if elec == 1:
		de = int(input("1. Crear un triangulo \n 2. Crear un cuadrado \n 3. Salir \n"))

		if de == 1:

			triangulob = int(input("Ingrese la base: "))
			trianguloh = int(input("Ingrese la altura: ")
			mi_triangulo = Triangulo(triangulob, trianguloh)

			print ("Area: " tr.calcular_area())
			print (tr.imprimir())


		elif de == 2:
			cul = int(input("Ingrese el lado del cuadrado"))
			cuadrado = Cuadrado(cul)

			print ("Area: ", cuadrado.calcular_area())
			print (cuadrado.imprimir())

		else: 
			des = False
			print 

	else:

		des = False
		print ("Adios")
