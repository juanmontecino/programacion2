def generar_prom (ruta):

    archivo = open(ruta, "r", encoding= "utf-8")
    lista = []
    for linea in archivo :
        id,n1,n2,n3 = linea.strip().split(";")

        n1 = float(n1)
        n2 = float(n2)
        n3 = float(n3)

        alumno_prom = {
            "id" : id,
            "promedio" : (n1+n2+n3)/3
        }
        lista.append(alumno_prom)
    archivo.close()
    return lista

def tomar_apellidos (ruta):
    archivo = open (ruta, "r", encoding= "utf-8")
    lista = []
    for linea in archivo:
        id, apellido, nombre = linea.strip().split(";")
        alumno = {
            "id" : id,
            "apellido": apellido,
            "nombre": nombre
        }
        lista.append(alumno)
    lista_ordenada = sorted (lista, key=lambda alumno: alumno ["apellido"])
    return lista_ordenada

def generar_lista_aprobados (lista_promedios, lista_alumnos) :

    lista_id_aprobados = []
    for alumno in lista_promedios:
        if alumno ["promedio"] >=7:
            lista_id_aprobados.append(alumno["id"])
    
    lista_aprobados = []

    for alumno in lista_alumnos:
        if alumno["id"] in lista_id_aprobados:
            alumno_aprobado = {
                "apellido" : alumno["apellido"],
                "nombre": alumno ["nombre"]
            }
            lista_aprobados.append(alumno_aprobado)
    lista_aprobados_ordenados = sorted (lista_aprobados, key= lambda alumno: alumno ["apellido"])
    return lista_aprobados_ordenados
    
def generar_archivo (lista):
    nombre = "aprobados.txt"
    archivo = open(nombre, "w", encoding= "utf-8")

    for persona in lista:
        # Escribir el nombre y apellido en el archivo
        archivo.write(f"Nombre: {persona['nombre']}, Apellido: {persona['apellido']}\n")



ruta_prom = input("ruta promedios = ")
promedios = generar_prom (ruta_prom)
ruta = input("ruta alumnos = ")
alumnos = tomar_apellidos (ruta)
lista_aprobados = generar_lista_aprobados(promedios, alumnos)
generar_archivo(lista_aprobados)