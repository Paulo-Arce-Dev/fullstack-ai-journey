# String -> cadena de textos

nombre = 'ada lovelace'

# el método title() con mayúscula solo la primer letra de cada palabra.
print(nombre.title()) # -> Ada Lovelace

nombre_2 = 'Thomas Shelby'

# método upper() -> vuelve una cadena de texto a mayúsculas
print(nombre_2.upper())

# método lower() -> vuelve una cadena de texto a minúsculas
print(nombre_2.lower())

primer_nombre = 'Ragnar'
apellido = 'Lodbrok'

# f string -> python formatea la cadena reemplazando el nombre de la variable por su valor
nombre_completo = f"{primer_nombre} {apellido}"
print(nombre_completo)

print(nombre_completo.title())

# agregar espacio en blanco o nuevas líneas
# agregar tabulación
print("\tPython")

# salto de línea
print("Lenguajes: \nPython \nJavasscript \nSQL")

# tabulación y salto de línea
print("Lenguajes: \n\tPythton \n\tJavascript \n\tSQL")

# eliminar espacios en blanco extras (izquierda y derecha)
frase = "     Pensar claro es programar fuera del sistema   "
print(frase.strip())

# elimina espacios del lado derecho
frase_2 = 'Lo simple es genial   '
print(frase_2.rstrip())

# elimina espacios del lado izquierdo
frase_3 = '   Programa con propósito, no con prisa'
print(frase_3.lstrip())

# eliminar prefijos
URL_GOOGLE = 'https://google.com/'
sin_prefijo_url = URL_GOOGLE.removeprefix('https://')
print(sin_prefijo_url)