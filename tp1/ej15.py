cadena = input("Ingrese una cadena de texto = ")

contador_caracteres = 0
contador_letras = 0
palabras = cadena.split()

for caracter in cadena:
    contador_caracteres += 1
    if caracter == " ":
        contador_caracteres -= 1

    if caracter.isalpha() :
        contador_letras += 1


print(f"La cadena tiene {contador_caracteres} caracteres ")
print(f"La cadena tiene {contador_letras} letras")
print(f"La cadena tiene {palabras} palabras")