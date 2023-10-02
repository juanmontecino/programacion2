class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
def estado (nota):
    if nota >=40:
        return "Aprobrado"
    else:
        return "Desaprobado"

lista_alumnos = []
while True:

    nombre = input("Nombre del alumno (o ingrese 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break


    nota = int (input("Ingrese la nota del estudiante = "))

    alumno = Alumno(nombre, nota)
    lista_alumnos.append(alumno)

print("\nALUMNOS NOTA ESTADO ")

for Alumno in lista_alumnos:
    mensaje = estado(Alumno.nota)
    print (f"{Alumno.nombre, Alumno.nota, mensaje}")