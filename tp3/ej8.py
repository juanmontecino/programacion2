lista_con_duplicados = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]
#lista_reducida = list(set(lista_con_duplicados)) set crea un conjunto , un conjunto no permite elementos duplicados.
lista_reducida = []
[lista_reducida.append (x) for x in lista_con_duplicados if x not in lista_reducida]
print(lista_reducida)
