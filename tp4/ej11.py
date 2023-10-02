from functools import reduce
lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]
suma =reduce(lambda x, y: x + y['nota'], lista_dic, 0)
promedio = suma / len(lista_dic)

print("La suma de las notas es:", suma)
print("El promedio de las notas es:", promedio)