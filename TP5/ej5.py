# 5. Un club deportivo que organiza para sus alumnos una serie de competencias para el fin de semana cerró las inscripciones a los eventos y se desea a procesarlas. Dada la siguiente estructura de datos simplificada:
#     * **alumnos.csv** (con datos en el formato `alumno_dni;alumno_apellido;alumno_nombre`)
#     * **eventos.csv** (con datos en el formato `evento_codigo;deporte_codigo;evento_nombre;evento_descripción`)
#     * **deportes.csv** (con datos en el formato `deporte_codigo;deporte_nombre`)
#     * **alumnos_deportes** (con datos en el formato `alumno_dni;deporte_codigo`)
#     * **inscripciones.csv** (con datos en el formato `alumno_dni;evento_codigo`)

#     se pide:
#     * cargar los datos en memoria usando las estructuras adecuadas, y procesar la cola de inscripciones a los eventos deportivos registrando los datos en un nuevo archivo ***alumnos_eventos.csv*** con el formato `alumno_dni;evento_codigo;numero_inscripcion`.
#     Se debe verificar que los datos cargados en la cola sean válidos (es decir que el dni exista en alumnos, que el código de deporte exista en deportes, que el código de evento exista en eventos, y que el evento en el que se inscribe el alumno sea de un deporte que el alumno realiza en el club *(un alumno puede realizar mas de un deporte)*).
#      Si hay un registro en inscripciones que no es correcto no se debe procesar y se debe almacenar en una pila con los datos `dni_alumno; evento_nombre`.
#     * luego al finalizar las inscripciones imprimir por pantalla el orden inverso al que se ejecutaron las inscripciones válidas (utilizando la pila del inciso anterior).
#     * de las inscripciones válidas se pueden calcular estadísticas: mostrar cuantos inscriptos tiene cada evento, cual es el evento con mayor inscriptos, cual es el que tiene menor inscriptos, cual es el que su cantidad de inscriptos se aproxima más al promedio de `inscriptos/eventos`.

def datos_alumnos(ruta):
    lista = []
    primera_linea = True  # Variable para verificar si es la primera línea
    
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if primera_linea:
                primera_linea = False
                continue  # Saltar la primera línea
            
            dni, apellido, nombre = linea.strip().split(";")
            alumno = {
                "dni": dni.strip(),
                "apellido": apellido.strip(),
                "nombre": nombre.strip(),
            }
            lista.append(alumno)
    
    return lista

def datos_eventos(ruta):
    lista = []
    primera_linea = True  # Variable para verificar si es la primera línea
    
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if primera_linea:
                primera_linea = False
                continue  # Saltar la primera línea
            
            evento_codigo,deporte_codigo,evento_nombre,evento_descripción = linea.strip().split(";")
            evento = {
                 "evento_codigo ": evento_codigo.strip(),
                 "deporte_codigo": deporte_codigo.strip(),
                 "evento_nombre": evento_nombre.strip(),
                 "evento_descripción": evento_descripción.strip()
            }
            lista.append(evento)
    
    return lista

def datos_deportes(ruta):
    lista = []
    primera_linea = True  # Variable para verificar si es la primera línea
    
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if primera_linea:
                primera_linea = False
                continue  # Saltar la primera línea
            
            deporte_codigo,deporte_nombre = linea.strip().split(";")
            deporte = {
                "deporte_codigo" : deporte_codigo.strip(),
                "deporte_nombre": deporte_nombre.strip()
            }
            lista.append(deporte)
    
    return lista

def datos_alumnos_deportes(ruta):
    lista = []
    primera_linea = True  # Variable para verificar si es la primera línea
    
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if primera_linea:
                primera_linea = False
                continue  # Saltar la primera línea
            
            alumno_dni,deporte_codigo = linea.strip().split(";")
            alumno_deporte = {
                "dni": alumno_dni.strip(),
                "deporte_codigo" : deporte_codigo.strip()
            }
            lista.append(alumno_deporte)
    
    return lista

def datos_inscripciones(ruta):
    lista = []
    primera_linea = True  # Variable para verificar si es la primera línea
    
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if primera_linea:
                primera_linea = False
                continue  # Saltar la primera línea
            
            alumno_dni,evento_codigo = linea.strip().split(";")
            inscripcion = {
                "dni": alumno_dni.strip(),
                "evento_codigo" : evento_codigo.strip()
            }
            lista.append(inscripcion)
    
    return lista

def comparar_valores_clave(list1, list2, clave):
    # Obtener una lista de los valores de la clave en la primera lista
    valores_list1 = [diccionario[clave] for diccionario in list1]
    
    # Iterar a través de la segunda lista y verificar si algún valor coincide
    for diccionario in list2:
        if diccionario[clave] in valores_list1:
            return True
    
    # Si no se encuentra ninguna coincidencia, devolver False
    return False

def alumnos_eventos (alumnos, eventos, deportes, alumnos_deportes, inscripciones):

        if comparar_valores_clave(inscripciones, alumnos, "dni"): #dni exista en alumnos
            if comparar_valores_clave(inscripciones, eventos, "evento_codigo"): #código de evento exista en eventos
                if comparar_valores_clave(eventos, deportes, "deporte_codigo"): #código de deporte exista en deportes
                    if 

#cargar los datos en memoria usando las estructuras adecuadas, y procesar la cola de inscripciones a los eventos deportivos registrando los datos en un nuevo archivo ***alumnos_eventos.csv*** con el formato `alumno_dni;evento_codigo;numero_inscripcion`.
# y que el evento en el que se inscribe el alumno sea de un deporte que el alumno realiza en el club *(un alumno puede realizar mas de un deporte)