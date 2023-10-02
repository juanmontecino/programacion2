a = int (input("Ingrese el primer numero entero positivo = "))
b = int (input("Ingrese el segundo numero entero positivo = "))
x = int (input("Ingrese el tercer numero entero positivo = "))

for i in range (a,b+1):
    if i%x == 0:
        print(i, end= " ")