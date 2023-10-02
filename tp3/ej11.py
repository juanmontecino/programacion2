estudiantes = [
    {
        "nombre_apellido": "Juan Pérez",
        "legajo": "12345",
        "nota_parcial1": 85,
        "nota_parcial2": 90,
        "nota_final": 88
    },
    {
        "nombre_apellido": "María Rodríguez",
        "legajo": "23456",
        "nota_parcial1": 78,
        "nota_parcial2": 82,
        "nota_final": 80
    },
    {
        "nombre_apellido": "Carlos López",
        "legajo": "34567",
        "nota_parcial1": 92,
        "nota_parcial2": 88,
        "nota_final": 90
    },
    {
        "nombre_apellido": "Ana Gómez",
        "legajo": "45678",
        "nota_parcial1": 75,
        "nota_parcial2": 80,
        "nota_final": 78
    },
    {
        "nombre_apellido": "Laura Martínez",
        "legajo": "56789",
        "nota_parcial1": 88,
        "nota_parcial2": 90,
        "nota_final": 89
    }
]

def aprobados (lista):
    lista_aprobado = [alumno ["nombre_apellido"] for alumno in estudiantes if alumno["nota_parcial1"] >=90 or alumno["nota_parcial2"] >=90 or alumno["nota_final"] >=90]
    return lista_aprobado
lista_aprobados = aprobados (estudiantes)
print(lista_aprobados)
