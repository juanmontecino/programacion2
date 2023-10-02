numero = input(" Ingrese un numero = ")
if numero.isdigit():
    digitos = []

    for digito_str in numero:
        digito_num = int(digito_str)
        digitos.append(digito_num)

    digito_mayor = max(digitos)
    indice = digitos.index(digito_mayor)

    print(f"El digito mayor de {numero} es {digito_mayor} y se encuentra en la posicion {indice}")
    
else:
    print("Te pedi un numero boludito")