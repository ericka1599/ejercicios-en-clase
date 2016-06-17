def Maximo(lista):
	if len(lista) == 1:
		return lista[0]

	sublista = lista[1:]
	submax = [sublista]

	if lista[0] > sublista :
		return lista[0]
	return submax