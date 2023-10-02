n1 = float(input("Ingrese el primer numero entero = "))
n2 = float(input("Ingrese el segundo numero entero = "))
n3 = float(input("Ingrese el tercer numero entero = "))

if n1 > n2 and n1>n3:
    print (f" El numero mas grande es = {n1:.0f}")
elif n2 > n1 and n2>n3:
    print (f" El numero mas grande es = {n2:.0f}")
else:
    print (f" El numero mas grande es = {n3:.0f}")
