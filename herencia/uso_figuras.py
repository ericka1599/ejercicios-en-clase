from cuadrado import Cuadrado
from triangulo import Triangulo

mi_cuadrado1 = Cuadrado(5)
mi_cuadrado2 = Cuadrado(10)
tri = Triangulo(10, 5)

print ("Area: ", mi_cuadrado1.calcular_area())
print (mi_cuadrado1.imprimir())

print ("Area: ", mi_cuadrado2.calcular_area())
print (mi_cuadrado2.imprimir())


print ("Area: ", tri.calcular_area())
print (tri.imprimir())