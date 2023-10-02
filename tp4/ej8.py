import random

# Generar una lista de 10 números aleatorios en el rango de 0 a 100
lista_aleatoria = [random.randint(0, 100) for _ in range(10)]
lista_fahrenheit = list(map(lambda x :(x * 9/5) + 32, lista_aleatoria))
# Imprimir la lista
print(lista_aleatoria)
print (lista_fahrenheit)
