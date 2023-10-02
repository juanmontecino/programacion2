def esbisiesto (año):
    if ((año % 4 == 0) and ((año % 100 != 0) or (año % 400 == 0))):
        return True
    else:
        return False

fecha = (input("Ingrese una fecha en formato dia/mes/año separado por / = "))
partes = fecha.split("/")

if len(partes) == 3:
    dia = int (partes [0])
    mes = int (partes [1])
    año = int (partes [2])

    if esbisiesto(año):
        print(f"El año de la fecha {dia, mes, año} es BISIESTO")

    else:
        print(f"El año de la fecha {dia, mes, año} NO es BISIESTO")
else: 
    print("Pone bien la fecha boludito")