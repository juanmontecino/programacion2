cadena =input ("Ingrese una cadena de texto para determinar cuantos espacios tiene = ")
contador = 0

for espacio in cadena:
    if espacio == " ":
        contador += 1

if contador == 0 :
    print(" Usted no ha ingresado una cadena con espacios ")
else : 
    print (f" La cadena ingresada tiene {contador} espacios")