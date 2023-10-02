salir = False
while not salir:
    palabra = input("Ingrese una palabra, ingrese salir para finalizar el programa :")
    palabra = palabra.lower()
    if palabra == "salir":
        print ("que putoooooooooooooooooo")
        salir = True

    else:
        contador = 0
        contador = sum(1 for vocal in palabra if vocal in "aeiou")
        mensaje = ("la palabra ingresada no contiene vocales" if contador == 0 else f"La palabra ingresada contiene {contador} vocales")
        print (mensaje)