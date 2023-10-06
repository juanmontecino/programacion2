def validar_fecha (stringfecha):
    separados= stringfecha.split('-')
    if (len(separados)==3):
        try:
            dia = int(separados[0])
            mes = int(separados[1])
            anio = int(separados[2])
        except ValueError:
            return False
        return True
    

if validar_fecha("2d-09-2004"):
    print("todo ok")
else:
    print("todo mal")