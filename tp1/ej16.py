cadena = input("Ingrese una cadena de texto = ")

palabras = cadena.split()

palabra_mas_larga = ""
longitud_ams_larga = 0

for palabra in palabras:
    
    if len(palabra_mas_larga) < len(palabra):
        palabra_mas_larga = palabra

print(f"La palabra mas larga es {palabra_mas_larga} y tiene {len(palabra_mas_larga)} letras")

