import datetime
fecha_actual = datetime.date.today()
lista_alumnos = [{"nombre":"Joaquin", "fecha_nacimiento":datetime.date(1990, 11, 5), "telefono":"123456789"}, { "nombre":"Maria", "fecha_nacimiento":datetime.date(1995, 5, 16), "telefono":"123456789"}, { "nombre":"Pedro", "fecha_nacimiento":datetime.date(1990, 10, 12), "telefono":"123456789"}, { "nombre":"Ana", "fecha_nacimiento":datetime.date(1991, 9, 22), "telefono":"123456789"}, { "nombre":"Florencia", "fecha_nacimiento":datetime.date(1994, 12, 8), "telefono":"123456789"}, { "nombre":"Hector", "fecha_nacimiento":datetime.date(1993, 4, 30), "telefono":"123456789"}]
nocumplieron= list(filter (lambda x : x["fecha_nacimiento"].month >= fecha_actual.month and x["fecha_nacimiento"].day > fecha_actual.day, lista_alumnos))
nocumplieron_ordenados = sorted (nocumplieron, key=lambda x : x["fecha_nacimiento"])
print (f"la lista de personas que todavia no cumplieron son \n: {nocumplieron}")
print (f"la lista de personas que todavia no cumplieron son \n:{nocumplieron_ordenados}")