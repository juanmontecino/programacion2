# 2. crear las funciones genéricas que nos permitirán manejar una pila de datos.
#     * apilar(pila,elemento) #agrega elemento encima de la pila
#     * desapilar(pila,elemento) #devuelve el elemento en la cima de la pila y lo elimina de la pila
#     * longitud(pila) #devuelve la longitud de la estructura (pueden reutilizar el del punto anterior)
#     * esta_vacia(pila) #devuelve True si la estructura está vacía (pueden reutilizar el del punto anterior)

def apilar (pila, elemento):
    pila.append (elemento)
    
def desapilar(pila,):
    if not esta_vacia (pila):
        return pila.pop()
    else:
        return "La pila está vacía"


def longitud(pila):
    return len (pila)

def esta_vacia(pila):
    return len(pila) == 0



