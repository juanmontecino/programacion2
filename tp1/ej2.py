
largo = float (input ("Ingrese el largo de su habitacion =  "))
ancho = float (input ("Ingrese el ancho de su habitacion = "))
alto = float (input ("Ingrese el alto de su habitacion = "))


area_pintable = (largo * alto) * 2 + (ancho * alto) * 2 - (0.8 * 2)
litros = area_pintable/10
print (f"el area pintable de tu habitacion es = {area_pintable} metros cuadrados. Para eso vas a necesitar {litros} litros")

cant_manos = float(input ("Cuantos manos desea dar? = "))

print (f"Para pintar su habitacion {cant_manos:.0f} veces se necesitan {cant_manos*litros :.2f} litros de pintura") # :.2f define la cantidad de decimales a mostrar
