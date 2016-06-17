from collections import deque
def es_palindromo (frase):
	frase.lower()
	cola = deque([])
	pila = []
	for let in frase:
		pila.append (let)
		cola.append (let)
		if pila == cola :
			return True
		return False

