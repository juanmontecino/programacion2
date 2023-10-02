tope = int (input (" ingrese la cantidad de numeros que desea sumar = "))
suma = 0
for i in range (0, tope):
    numero_sumar = float (input("Ingrese el numero a sumar = "))
    suma += numero_sumar

print (f"la suma es {suma:.2f} y el promedio es {suma/tope}")