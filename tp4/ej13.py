import random
from functools import reduce

# Generar una lista de 10 números aleatorios en el rango de 0 a 100
lista_aleatoria = [random.randint(0, 100) for _ in range(10)]
def encontrar_mayor (x,y):
    return x if x>y else y
mayor = reduce(encontrar_mayor, lista_aleatoria)
print(lista_aleatoria)
print (mayor)