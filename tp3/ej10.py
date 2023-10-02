lista = [1,2,3,4,5,6,7,8,9,10]

pares = [x for x in lista if x % 2 == 0]
impares = [x for x in lista if x % 2 != 0]

print (f"lista pares = {pares}")
print (f"lista impares = {impares}")
