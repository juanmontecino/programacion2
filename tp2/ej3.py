cantidad_notas = int (input("Cuantas notas desea ingresar? "))

arr_notas = []
for i in range (0, cantidad_notas):
    nota = int(input(f"Ingrese la nota n {i+1} = "))
    arr_notas.append(nota)

valor_maximo = max(arr_notas)
indice = arr_notas.index(valor_maximo)

print(f"La nota mas alta es {valor_maximo} y esta en la posicion {indice} del arreglo")