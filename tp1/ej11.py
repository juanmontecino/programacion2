nro = int (input("Ingrese un nro entero positivo, para salir ingrese o uno negativo = "))
suma = 0
contador = 0
while nro > 0:
    contador+=1
    suma +=nro
    nro = int (input("Ingrese un nro entero positivo, para salir ingrese o uno negativo = "))
print (f"El promedio es {suma/contador}, se ingresaron {contador} numeros")