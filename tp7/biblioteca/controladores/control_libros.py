from flask import Flask, request, jsonify, Blueprint
from modelos.model_libro import lista_libros
libros_bp = Blueprint("libros", __name__)

@libros_bp.route("/libros/obtener", methods=["GET"])
def obtener_libros():
    return jsonify(lista_libros)

@libros_bp.route("/libros/obtener/<int:id>", methods=["GET"])
def obtener_libro_id(id):
    libro_encontrado = [libro for libro in lista_libros if libro ["id"] == id]

    if len(libro_encontrado) == 0:
        return jsonify({"message": "Error no se encontró el libro"}), 404
    else:
        return jsonify(libro_encontrado[0])

@libros_bp.route("/libros/crear", methods=["POST"])
def crear_libro():
    if request.is_json:
        if "titulo" and "autor" and "año_publicacion" in request.json: 
            nuevo_libro = request.get_json()
            nuevo_libro["id"] = lista_libros [-1]["id"] + 1
            lista_libros.append(nuevo_libro)
            return jsonify({"message": "Libro creado exitosamente"},nuevo_libro), 200
        else:
            return jsonify({"message": "Error, falta alguno de los campos obligatorios"}), 400  
    else:
        return jsonify({"message": "Error, el contenido no es JSON"}), 400

@libros_bp.route("/libros/modificar/<int:id>", methods=["PUT"])
def mod_libro(id):
    if request.is_json:
        libro_mod = request.get_json()

        libro_encontrado = [libro for libro in lista_libros if libro ["id"] == id]

        if len(libro_encontrado) == 0:
            return jsonify({"message": "Error no se encontró el libro"}), 404
       
        else:
            for campo, valor in libro_mod.items():
                if campo in libro_encontrado[0]:
                    libro_encontrado[0][campo] = valor
            return  jsonify({"message": "Libro modificado exitosamente"}, libro_encontrado[0]), 200
    else:
        return jsonify({"message": "Error, el contenido no es JSON"}), 400
                        