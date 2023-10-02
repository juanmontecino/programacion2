numeros = list(range(1, 101))
def contar_divisores (numero):
    divisores = 0
    for x in range (1, numero+1):
        if numero%x == 0:
            divisores +=1
    return divisores

primos = [numero for numero in numeros if contar_divisores(numero) == 2]

print (primos)