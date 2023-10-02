def tomar_datos (ruta):
    lista = []
    
    archivo =  open (ruta, "r", encoding= "utf-8")

    for linea in archivo:
        id, nombre, precio = linea.strip().split(";")
        producto = {
            "id": int (id),
            "nombre": nombre.strip(),
            "precio": float (precio)
        }
        lista.append(producto)
    archivo.close()
    return lista

def buscar_prod (lista, nombreprod) :

    precio = 0
    for producto in lista:
        if nombreprod == producto ["nombre"]:
            precio = producto ["precio"]
    return precio


ruta = input("Ingrese la ruta del archivo: ")
lista = tomar_datos (ruta)
nombre_prod = input("Ingrese el nombre del producto quede desea buscar : ")
precio = buscar_prod (lista, nombre_prod)
print (f"El producto {nombre_prod} vale {precio}")
