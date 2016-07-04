from collections import deque
def es_palindromo (frase):
    pila = list(frase)
    cola = deque([pila])
    for i in range(len(frase)):
       if pila.pop() != cola.popleft():
            return False
    return True

