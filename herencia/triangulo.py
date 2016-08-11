from figuras import FiguraGeometrica

#Un triangulo es una figura geometrica
class Triangulo(FiguraGeometrica):

	def __init__ (self, base, altura):
		super(). __init__(base, altura)

	def imprimir (self):
		resultado = ""

		for i in range(self.altura):
			al = altura % 2 
			print (al)
			resultado += " * " * (i + 1) + "\n"
		return resultado

	def calcular_area (self):
		return super(). calcular_area() / 2.0