from flask import Flask

from modelos.model_libro import inicializar_libros
from controladores.control_libros import libros_bp

from modelos.model_socios import inicializar_socios
from controladores.control_socios import socios_bp

from modelos.model_prestamo import inicializar_prestamos
from controladores.control_prestamos import prestamos_bp

app = Flask(__name__)

inicializar_libros()
app.register_blueprint(libros_bp)

inicializar_socios()
app.register_blueprint(socios_bp)

inicializar_prestamos()
app.register_blueprint(prestamos_bp)

