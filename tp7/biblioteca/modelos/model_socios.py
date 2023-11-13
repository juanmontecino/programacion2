lista_socios = []

def inicializar_socios():
    global lista_socios
    
    with open("modelos\socios.csv", "r", encoding="utf-8") as csvfile:
        lineas = csvfile.readlines()
        lineas.pop(0)

        for linea in lineas:
            campos = linea.strip().split(",")

            socio = {
                "id": int(campos[0]),
                "dni": int(campos[1]),
                "nombre": campos[2],
                "apellido": campos[3],
                "telefono": campos[4],
                "email": campos[5]
            }
            lista_socios.append(socio)

def guardar_socios_en_csv(socios_lista):
    # Nombre del archivo CSV
    archivo_csv = "modelos/socios.csv"

    # Guardar datos en el archivo CSV
    with open(archivo_csv, "w", newline="", encoding="utf-8") as file:
        # Escribir la primera línea
        headers = ["id", "dni", "nombre", "apellido", "telefono", "email"]
        file.write(",".join(headers) + "\n")

        # Escribir datos de socios
        for socio in socios_lista:
            linea = f"{socio['id']},{socio['dni']},{socio['nombre']},{socio['apellido']},{socio['telefono']},{socio['email']}\n"
            file.write(linea)