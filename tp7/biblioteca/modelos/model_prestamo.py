lista_prestamos = []

def inicializar_prestamos():
    global lista_prestamos
    
    with open("modelos\prestamos.csv", "r", encoding="utf-8") as csvfile:
        lineas = csvfile.readlines()
        lineas.pop(0)

        for linea in lineas:
            campos = linea.strip().split(",")

            prestamo = {
                "id": int(campos[0]),
                "socio_dni": int(campos[1]),
                "libro_id": int(campos[2]),
                "fecha_retiro": campos[3],
                "fecha_devolucion": campos[4]
            }
            lista_prestamos.append(prestamo)

def guardar_prestamos_en_csv(prestamos_lista):
    # Nombre del archivo CSV
    archivo_csv = "modelos/prestamos.csv"

    # Guardar datos en el archivo CSV
    with open(archivo_csv, "w", newline="", encoding="utf-8") as file:
        # Escribir la primera línea
        headers = ["id", "socio_dni", "libro_id", "fecha_retiro", "fecha_devolucion"]
        file.write(",".join(headers) + "\n")

        # Escribir datos de préstamos
        for prestamo in prestamos_lista:
            linea = f"{prestamo['id']},{prestamo['socio_dni']},{prestamo['libro_id']},{prestamo['fecha_retiro']},{prestamo['fecha_devolucion']}\n"
            file.write(linea)

