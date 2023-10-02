from functools import reduce

cadenas = ["Hola", "Mundo", "Python", "Programación", "Cadenas", "Listas"]
cadena = reduce (lambda x , y :  x+y, cadenas)
print (cadena)