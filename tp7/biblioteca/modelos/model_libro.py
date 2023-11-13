lista_libros = []

def inicializar_libros():
    global lista_libros
    
    with open("modelos\libros.csv", "r", encoding="utf-8") as csvfile:
        lineas = csvfile.readlines()
        lineas.pop(0)

        for linea in lineas:
            campos = linea.strip().split(",")

            libro={
                "id": int(campos[0]),
                "titulo": campos[1],
                "autor": campos[2],
                "año_publicacion": int(campos[3])
            }
            lista_libros.append(libro)

