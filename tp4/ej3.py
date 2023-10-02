variable1 = float (input("Ingrese un numero : "))
variable2 = float (input("Ingrese un numero : "))

mayor = lambda x,y : x if x>y else y

print(f"el numero mayor es {mayor (variable1, variable2)}")
