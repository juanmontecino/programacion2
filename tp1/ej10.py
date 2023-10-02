alto = int (input(" Ingrese el alto de la pared = "))
ancho = int (input(" Ingrese el ancho de la pared = "))

for i in range (0,alto):
    print()#salto de linea
    for j in range (0, ancho):
        print("*", end= " ")
    