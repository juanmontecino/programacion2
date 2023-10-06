#3. Usando el módulo random, cree una función que retorne dos listas de longitud aleatoria entre 20 y 50, y cada lista con elementos de valores aleatorios entre 200 y 5000.
import random

def generar_lista_random():
    longitud = random.randint(20, 50)
    lista = [] 

    for x in range(longitud):  
        numero = random.randint(200, 5000)
        lista.insert(x, numero)
    return lista

# 4. Utilizando la función anterior genere dos listas de datos. 
# Con la lista1 se debe generar una sublista con los elementos impares de lista1 multiplicados por el valor menor de la lista2.
#Con la lista2 se debe devolver el menor número primo contenido en la lista, o “-1” si no tiene números primos.


def impares (lista):
    lista_impares = [numero for numero in lista if numero % 2 !=0]
    return lista_impares

def menor_valor (lista):
    menor_valor = lista[0]
    for x in lista:
        if x < menor_valor:
            menor_valor = x
    return menor_valor



def contar_divisores (numero) :
    if numero == 0:
        print ("Error, no se puede dividir por 0")
    else:
        if numero < 0:
            numero = abs(numero)
        divisores = 0
        for x in range (1, numero+1):
            if numero % x == 0:
                divisores +=1
        return divisores

   

lista1 = generar_lista_random()
lista2 = generar_lista_random()
numero_menor = menor_valor(lista2)
sublista_multiplicados = list(map(lambda x : x * numero_menor, lista1))
primos = [numero for numero in lista2 if contar_divisores(numero) == 2]
menor_primo = menor_valor(primos)


print ("la lista 1 es : ", lista1, "\n")
print ("la lista 2 es : ", lista2, "\n")
print ("el menor numero de la lista 2 es : ",numero_menor, "\n")
print ("la sublista es : ", sublista_multiplicados, "\n")
print ("la lista de primos es :", primos, "\n")
print ("el menor de los primos es :", menor_primo, "\n")



    
