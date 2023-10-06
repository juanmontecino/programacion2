# 1. crear las funciones genéricas que nos permitirán manejar una cola de datos.
#     * encolar(cola,elemento) #agrega elemento al final de la cola
#     * desencolar(cola,elemento) #devuelve el elemento al inicio de la cola y lo elimina de la cola
#     * longitud(cola) #devuelve la longitud de la estructura
#     * esta_vacia(cola) #devuelve True si la estructura está vacía

def encolar (cola, elemento):
    cola.append (elemento)

def desencolar (cola):
    if not esta_vacia (cola):
        return cola.pop (0)
    else:
        return "La cola está vacía"

def longitud (cola):
    return len(cola)

def esta_vacia(cola):
    return len(cola) == 0


