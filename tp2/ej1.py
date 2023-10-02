def reverso (palabra):
    palabra = palabra.lower()
    palabra_invertida = palabra [::-1]
    print(f"El reverso de la palabra es {palabra_invertida}")

    return palabra_invertida

def palindromo (palabra, inverso):
    if palabra == inverso:
        print("La palabra es palindromo")
    else:
        print("La palabra NO es palindromo")


palabra = input("Ingrese una palabra = ")
inverso = reverso(palabra)
palindromo (palabra, inverso)

