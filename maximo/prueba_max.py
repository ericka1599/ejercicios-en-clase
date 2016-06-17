from maximo import Maximo 
re = int(input("Desea ingresar un numero? Si = 1 No = 2 "))
lista = []
while re == 1:
	num = input("Ingrese el numero: ")
	lista.append (num)
	re = int(input("Desea ingresar un numero? Si = 1 No = 2 "))

print (Maximo(lista))