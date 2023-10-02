#Lee el contenido de un archivo de texto llamado "datos.txt" y crea una lista con todas las líneas del archivo, utilizando list comprehensions.
nombre = "datos.txt"
archivo = open (nombre, "r", encoding="utf-8")
lista = [linea for linea in archivo]

print(lista)