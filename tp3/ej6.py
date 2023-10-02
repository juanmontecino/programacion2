
# Puedes acceder a la información de cada persona utilizando sus nombres como clave.

personas = {'Persona1': 45, 'Persona2': 75, 'Persona3': 21, 'Persona4': 49, 'Persona5': 77, 'Persona6': 60, 'Persona7': 50, 'Persona8': 92, 
'Persona9': 88, 'Persona10': 21, 'Persona11': 20, 'Persona12':18, 'Persona13': 63, 'Persona14': 11, 'Persona15': 50, 
'Persona16': 13, 'Persona17': 30, 'Persona18': 66, 'Persona19': 75, 'Persona20': 9}


def cortar_edad (dicc, parametro):
    lista = [nombre for nombre,edad in dicc.items() if edad >= parametro]
    return lista

parametro = int(input("ingrese una edad para buscar las personas que tengas mas de esa edad = "))
lista = cortar_edad (personas, parametro)
print (lista)

# Puedes acceder a la información de cada persona utilizando sus nombres como clave.
