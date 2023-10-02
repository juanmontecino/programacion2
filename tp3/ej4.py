diccionario = {
    "Aardvark": "Un mamífero insectívoro de África, conocido por su hocico largo y su lengua pegajosa.",
    "Bosque": "Un área extensa cubierta de árboles, generalmente con una gran diversidad de vida vegetal y animal.",
    "Catarata": "Una gran caída de agua, a menudo con una fuerte corriente, como las Cataratas del Niágara.",
    "Dinosaurio": "Un grupo de reptiles extintos que vivieron en la Tierra hace millones de años.",
    "Elefante": "Un mamífero terrestre grande y herbívoro, conocido por su trompa larga.",
    "Fotografía": "El arte o proceso de capturar imágenes con una cámara.",
    "Guitarra": "Un instrumento musical de cuerdas que se toca con los dedos o una púa.",
    "Hipopótamo": "Un gran mamífero acuático herbívoro, conocido por su tamaño y colmillos.",
    "Isla": "Una porción de tierra rodeada de agua por todos lados.",
    "Jirafa": "Un mamífero africano de cuello largo y patas altas.",
    "Kangaroo": "Un marsupial saltador nativo de Australia.",
    "León": "Un gran felino carnívoro conocido por su melena en los machos.",
    "Montaña": "Una elevación natural de la superficie de la Tierra con pendientes empinadas.",
    "Nube": "Una colección visible de pequeñas gotas de agua o cristales de hielo en la atmósfera.",
    "Orquídea": "Una planta con flores exóticas y a menudo coloridas.",
    "Pájaro": "Un animal vertebrado con alas y plumas, generalmente capaz de volar.",
    "Química": "La ciencia que estudia la composición y las propiedades de la materia.",
    "Reptil": "Un grupo de animales vertebrados de sangre fría, como lagartos y serpientes.",
    "Serpiente": "Un reptil sin patas, a menudo venenoso.",
    "Tigre": "Un gran felino rayado y carnívoro.",
    "Universo": "Todo lo que existe, incluyendo estrellas, planetas y galaxias.",
    "Volcán": "Una montaña que entra en erupción y emite lava, ceniza y gases.",
    "Whale": "Una ballena, un mamífero marino gigante.",
    "Xilófono": "Un instrumento musical de percusión que consta de láminas de madera.",
    "Yak": "Un animal de montaña nativo del Himalaya, conocido por su pelaje largo.",
    "Zorro": "Un mamífero carnívoro, generalmente de cola larga y pelaje rojizo."
}

# Puedes acceder a las definiciones de las palabras según sea necesario.
letra = input("ingrese una letra = ")
letra = letra.upper()

lista = [clave for clave in diccionario if clave[0]== letra]

print(lista)