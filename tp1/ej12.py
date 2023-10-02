nro = int(input(" Ingrese un nro entero positivo. el programa finalizara cuando ingrese 0 = "))

if nro <0 :
 print("error")

else:
    array = []
    while nro != 0:
       array.append (nro)
       nro = int(input(" Ingrese un nro entero positivo. el programa finalizara cuando ingrese 0 = "))


if array == sorted(array):
    print("ESTA ORDENADO")
else:
    print(" NO ESTA ORDENADO")