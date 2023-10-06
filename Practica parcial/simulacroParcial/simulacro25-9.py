# complete con su fecha de nacimiento, nombre , legajo y dni
# Al finalizar subir el archivo al aula virtual.
import os
from functools import reduce
mifecha='22-09-2004'  
minombre='juan cruz montecino'
milegajo=21000
midni=30000000
# 1) implemente una funcion hashFecha(stringfecha) y sume el numero del día, el numero del mes y el numero del año y devuelva el resto de dividirlo por 3.
# ejemplo fecha 01-01-1989 = (01+ 01 +1989) % 3 = 1992 % 3 = 2
def es_bisiesto (anio):
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return True
    else:
        return False

def validar_fecha (fecha_string):
    fecha_separada = fecha_string.split("-")

    if len(fecha_separada) == 3:
        try:
            dia = int (fecha_separada[0])
            mes = int(fecha_separada[1])
            anio = int(fecha_separada[2])
        except ValueError:# si hay un error de conversion
            return False
        if ((dia > 31 or dia < 1) or (mes>12 or mes < 1) or (anio<1900)):
            return False
        elif (mes==2 and dia>28 and not es_bisiesto(anio)) or (mes==2 and dia>29 and es_bisiesto(anio)):
            return False
        elif (mes in [4, 6, 9, 11] and dia > 30):
            return False
        else:
            return True
    else:
        return False


def hashFecha(stringfecha):
    if validar_fecha (stringfecha):
        fecha_separada = stringfecha.split("-")
        dia = int (fecha_separada[0])
        mes =int (fecha_separada[1])
        anio = int(fecha_separada[2])
        return (dia+mes+anio)%3
    else:
        return False

# 2) Explique el funcionamiento y describa el algoritmo de ordenamiento que le corresponda según su resultado anterior: 0=burbuja, 1=inserción, 2=selección.    
# Funcionamiento: Teniendo una lista...
# Algoritmo: ...compara...

# 3)  Usando el archivo CSV "datos.csv" que contiene información sobre productos. El archivo tiene el siguiente formato:
# Nombre, Precio, Cantidad
# Producto1, 10.99, 50
# Producto2, 5.99, 30
# Producto3, 8.49, 75

#Crea una lista de diccionarios donde cada diccionario represente un producto. Los diccionarios deben tener tres claves: "Nombre" del tipo string, "Precio" del tipo float 
# y "Cantidad" del tipo entero, y  los valores deben corresponder a los datos del archivo CSV
def archivo_existe (ruta):
    if os.path.isfile (ruta):
        return True
    else:
        return False
        
def crearStock(ruta):
    if archivo_existe(ruta):
        lista=[]
        archivo = open(ruta, "r", encoding="utf-8")

        for linea in archivo:
            try:
                nombre, precio, cantidad = linea.strip().split(",")
                nombre = str(nombre)
                precio = float(precio)
                cantidad = int(cantidad)

                producto = {
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                }
                lista.append(producto)
            except ValueError:
                # Manejar la excepción aquí o imprimir un mensaje de error
                print(f"Error al procesar la línea: {linea}")

        archivo.close()
        return lista
    else:
        return False


# 4) Crear dos funcion que utilizando la estructura del punto 3, una que nos devuelva el producto mas caro y la otra que nos devuelva el producto con menor cantidad.
def productoMasCaro(lista):
    lista_productos_mas_caros = sorted (lista, key=lambda x : x ["precio"], reverse= True)
    return lista_productos_mas_caros [0]

def productoMenorCantidad(lista):
    lista_productos_menor_cantidad = sorted (lista, key= lambda x : x ["cantidad"])
    return lista_productos_menor_cantidad [0]

# 5) Implemente una funcion que nos devuelva el total de la posible ganancia. Esto es, Cantidad * Precio para cada producto y que sume todos los resultados. (¿Se puede usar reduce? Fundamente)
def totalGanancia(lista):
    ganancia = reduce (lambda acum, producto: acum + producto ["cantidad"] * producto ["precio"], lista, 0)
    return ganancia

ruta = input ("Ingrese la ruta de su archivo: ")

print("\nEl resultado de mi fecha es : ", hashFecha(mifecha), "\n")
lista = crearStock (ruta)
prod_mas_caro = productoMasCaro (lista)
prod_menor_cant = productoMenorCantidad (lista)
ganancia = totalGanancia (lista)

print ("El producto mas caro es : ", prod_mas_caro ["nombre"], "con un valor de ", prod_mas_caro ["precio"], "\n")
print ("El producto con menor cantidad es : ", prod_menor_cant ["nombre"], "con un total de ", prod_menor_cant ["cantidad"], " unidades \n")
print ("La ganancia total de la lista es : ", ganancia)


