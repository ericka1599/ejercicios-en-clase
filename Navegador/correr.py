from navegador import Navegador
from tab import Tabs

print ("Hola!")

if self.abierto == False:
	desa = int(input("Deseas abrir el navegador?" '\n' "1. Si" '\n' "2. No"))
	if desa == 1:
		self.abierto == True
	else: 
		print ("Mm bueno (._. )")
		while desa == 2:
			desa = int(input("Y ahora?" '\n' "1. Abrir navegador" '\n' "2. Nope"))

else:	
	deso =int(input("Ahora que quieres hacer?"  '\n' "1. Crear un nuevo tab" '\n' "2. Cambiar la url de un tab" '\n' "3. Cerrar un tab" '\n' "4. Cerrar todos los tab" '\n' "5. Mostrar todos mis tabs" '\n' "6. Guardar mis tabs" '\n' "7.Cerrar el navegador" '\n' "8. Salir"))

	if deso == 1:
		url = input("Ingresa la URL: ")
		url.agregar_tabs()

	elif deso == 2:
		url = input("Ingresa la url que quieres cambiar: ")
		urlc = input("Ingresa la url por la que la cambiaras: ")

	elif deso == 3:
		#Podria mostrarse la lista y que se ingrese como numero
		cerr = input 
