#Implemente una función que dada una lista de nombres, devuelva una nueva lista que contenga solo los nombres
#que tengan una longitud mayor o igual a una cantidad de caracteres pasada por parámetro, utilizando list comprehensions.

nombres = ["Juan", "María", "Carlos", "Ana", "Luis", "Laura", "Pedro", "Isabel", "Andrés", "Sofía", "Elena", "José", "Marta", "Pablo", "Raquel", "Ricardo", "Verónica", "Esteban", "Carmen", "Fernando", "Gabriela"]

nombres_mayores7 = [nombre for nombre in nombres if len(nombre) >= 7]

print(nombres_mayores7)