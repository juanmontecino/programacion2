from flask import Flask, request, jsonify, Blueprint
from modelos.model_prestamo import lista_prestamos  # Cambia a "model_prestamo" si ese es el nombre del módulo
from modelos.model_prestamo import guardar_prestamos_en_csv
from modelos.model_socios import lista_socios  #importamos las listas para verificar que los datos que nos mandan en json sean correctos
from modelos.model_libro import lista_libros

prestamos_bp = Blueprint("prestamos", __name__)

@prestamos_bp.route("/prestamos/obtener", methods=["GET"])
def obtener_prestamos():
    if len(lista_prestamos) == 0:
        return jsonify({"message": "Error, la lista de préstamos está vacía"}), 404
    else:
        return jsonify(lista_prestamos)

@prestamos_bp.route("/prestamos/obtener/<int:id>", methods=["GET"])
def obtener_prestamo_id(id):
    prestamo_encontrado = [prestamo for prestamo in lista_prestamos if prestamo["id"] == id]

    if len(prestamo_encontrado) == 0:
        return jsonify({"message": "Error, no se encontró el préstamo"}), 404
    else:
        return jsonify(prestamo_encontrado[0])

@prestamos_bp.route("/prestamos/crear", methods=["POST"])
def crear_prestamo():
    if request.is_json:
        nuevo_prestamo = request.get_json()
        socio_dni = nuevo_prestamo["socio_dni"]
        libro_id = nuevo_prestamo["libro_id"]
        if (dni_valido (socio_dni) == True):
            if (libro_disponible(libro_id) == True):
                if "fecha_retiro" and "fecha_devolucion" in request.json:
                    
                    if len(lista_prestamos) == 0:
                        nuevo_prestamo["id"] = 1
                    else:
                        nuevo_prestamo["id"] = lista_prestamos[-1]["id"] + 1

                    lista_prestamos.append(nuevo_prestamo)
                    guardar_prestamos_en_csv(lista_prestamos)
                    return jsonify({"message": "Préstamo creado exitosamente"}, nuevo_prestamo), 200
                else:
                    return jsonify({"message": "Error, falta la fecha de retiro o devolucion"}), 400
            else:
                return jsonify({"message": "Error, el libro no esta disponible o no existe"}), 400
        else:
            return jsonify({"message": "Error, el dni del socio no es válido"}), 400
    else:
        return jsonify({"message": "Error, el contenido no es JSON"}), 400

@prestamos_bp.route("/prestamos/modificar/<int:id>", methods=["PUT"])
def mod_prestamo(id):
    if request.is_json:

        prestamo_encontrado = [prestamo for prestamo in lista_prestamos if prestamo["id"] == id]

        if len(prestamo_encontrado) == 0:
            return jsonify({"message": "Error, no se encontró el préstamo"}), 404
        else:
            for i, prestamo in enumerate(lista_prestamos):
                if prestamo ["id"] == id:
                    lista_prestamos.pop(i)
                    guardar_prestamos_en_csv(lista_prestamos)
                    return jsonify({"message": "Prestamo devuelto exitosamente"}), 200
    else:
        return jsonify({"message": "Error, el contenido no es JSON"}), 400


def dni_valido(dni):
    socio_encontrado = [socio for socio in lista_socios if socio["dni"] == dni] 
    if len(socio_encontrado) == 0:
        return False
    else:
        return True

def libro_disponible(libro_id):
    libro_existe = [libro for libro in lista_libros if libro["id"] == libro_id]
    if len(libro_existe) == 0:
        return False
    else:
        if len(lista_prestamos) == 0:
            return True
        else:
            libro_disponible = [libro for libro in lista_prestamos if libro["libro_id"] == libro_id]
            if len(libro_disponible) == 0:
                return True
            else:
                return False
            