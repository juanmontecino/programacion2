cadena = input (" Ingrese una cadena de texto = ")
contador = 0

for vocal in cadena :
    if vocal == "a" or vocal == "e" or vocal  == "i" or vocal == "o" or vocal == "u":
        contador +=1
print(f"La cadena tiene {contador} vocales")


# forma mas optimizada de hacerlo y que toma las vocales en mayusculas :
# cadena = input("Ingrese una cadena de texto: ").lower()  # Convertir la cadena a minúsculas
# contador = 0
# vocales = set("aeiou")  # Conjunto de vocales

# for letra in cadena:
#     if letra in vocales:
#         contador += 1

# print(f"La cadena tiene {contador} vocales")
