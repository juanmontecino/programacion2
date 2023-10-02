
a = float (input ("Ingrese el valor del primer lado de su triangulo = "))
b = float (input ("Ingrese el valor del segundo lado de su triangulo = "))
c = float (input ("Ingrese el valor del tercer lado de su triangulo = "))

if a == b == c :
    print ("Usted ha ingresado un triangulo equilatero")

elif a == b or b == c or a == c:
    print ("Usted ha ingresado un triangulo isosceles")

else:
    print ("Usted ha ingresado un triangulo escaleno")