from flask import Flask, request, jsonify, Blueprint
from modelos.model_socios import lista_socios  # Cambiado de model_libro a model_socio
from modelos.model_prestamo import lista_prestamos  # 
from modelos.model_socios import guardar_socios_en_csv
socios_bp = Blueprint("socios", __name__)  # Cambiado de libros_bp a socios_bp

@socios_bp.route("/socios/obtener", methods=["GET"])  # Cambiado de libros a socios
def obtener_socios():
    return jsonify(lista_socios)

@socios_bp.route("/socios/obtener/<int:id>", methods=["GET"])  # Cambiado de libros a socios
def obtener_socio_id(id):
    socio_encontrado = [socio for socio in lista_socios if socio["id"] == id]

    if len(socio_encontrado) == 0:
        return jsonify({"message": "Error no se encontró el socio"}), 404
    else:
        return jsonify(socio_encontrado[0])

@socios_bp.route("/socios/crear", methods=["POST"])  # Cambiado de libros a socios
def crear_socio():
    if request.is_json:
        if "dni" and "nombre" and "apellido" and "telefono" and "email" in request.json: 

            nuevo_socio = request.get_json()
            nuevo_socio["id"] = lista_socios[-1]["id"] + 1
            lista_socios.append(nuevo_socio)
            guardar_socios_en_csv(lista_socios)
            return jsonify({"message": "Socio creado exitosamente"}, nuevo_socio), 200
        else:
            return jsonify({"message": "Error, falta alguno de los campos obligatorios"}), 400  
    else:
        return jsonify({"message": "Error, el contenido no es JSON"}), 400

@socios_bp.route("/socios/modificar/<int:id>", methods=["PUT"])  # Cambiado de libros a socios
def mod_socio(id):
    if request.is_json:
        socio_mod = request.get_json()

        socio_encontrado = [socio for socio in lista_socios if socio["id"] == id]

        if len(socio_encontrado) == 0:
            return jsonify({"message": "Error no se encontró el socio"}), 404
       
        else:
            for campo, valor in socio_mod.items():
                if campo in socio_encontrado[0]:
                    socio_encontrado[0][campo] = valor
            guardar_socios_en_csv(lista_socios)

            return jsonify({"message": "Socio modificado exitosamente"}, socio_encontrado[0]), 200
    else:
        return jsonify({"message": "Error, el contenido no es JSON"}), 400
    
@socios_bp.route("/socios/eliminar/<int:id>", methods=["DELETE"])
def eliminar_socio(id):

    socio_encontrado = [socio for socio in lista_socios if socio["id"] == id]
    print(socio_encontrado)
    if len(socio_encontrado) == 0:
        return jsonify({"message": "Error, no se encontró el socio"}), 404
    else:
            dni = socio_encontrado[0]["dni"]
            prestamo_encontrado = [prestamo for prestamo in lista_prestamos if dni == prestamo["socio_dni"]]

            if len(prestamo_encontrado) == 0:

                for i, socio in enumerate(lista_socios):
                    if socio["id"] == id:
                        socio_eliminado = lista_socios.pop(i)
                        guardar_socios_en_csv(lista_socios)
                        return jsonify({"message": "Socio eliminado exitosamente", "socio_eliminado": socio_eliminado}), 200
                return jsonify({"message": "Error, no se encontró el socio con el ID proporcionado"}), 404
                
            else:
                return jsonify({"message": "Error, el socio tiene préstamos asociados"}), 400



