def Suma (lista):
	if len(lista) == 1:
		return lista[0]

	sublis = lista[1:]
	suman = lista[0] + sublis

	return suman