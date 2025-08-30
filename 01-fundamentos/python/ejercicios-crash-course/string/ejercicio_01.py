# Ejercicios de string

"""  
2-3. Mensaje personal: Utilice una variable para presentar el nombre de una álabra e imprima un mensaje para esa persona. Tu mensaje debe ser simple, como "Hola paulo, ¿Te gustaria aprender algo de python hoy?"

2-4. Casos de nombre: Use una variable para representar el nombre de una persona y luego imprima el nombre de esa persona en minúsculas, mayúaculas y en formato título.

2-5 Cita famosa: Encuentre una cita de una persona famosa que admire. Imprima la cita y el nombre de su autor. Su resultado deberia verse similar a la siguiente, incluidas las comillas:
    Albert Einstein dijo una vez: "Una persona que nunca cometió un error nunca intentó nada nuevo".
    
2-6 Cita famosa 2: Repita el ejercicio 2-5, pero esta vez, represente el nombre de la persona famosa usando una variable llamada persona_famosa. Luego redacte su mensaje y represéntelo con una nueva variable llamada mensaje. Imprime tu mensaje. 

2-7. Eliminación de nombres: Utilice una variable para representar el nombre de una persona e incluya algunos caracteres de espacio en blanco al principio y al final del nombre. Asegurese de utilizar cada combinacion de caracteres, "\t" y "\n", al menos una vez.
    Imprima el nombre una vez, para que se muestre el espacio en blanco alrededor del nombre.
Luego imprima el nombre usando cada una de las tres funciones de eliminación, lstrip(), rstrip() y strip().

2-8. Extensiones de archivo: Python tiene un metodo removesuffix() que funciona exactamente como removeprefix(). Asigne el valor 'python_notes.txt' a una variable llamada nombre de archivo. Luego use el método removesuffix() para mostrar el nombre del archivo en la extensión del archivo, como lo hacen algunos exploradores de archivos.      
"""


# 2-3
nombre_persona = "Paulo";
mensaje = f"Hola {nombre_persona}, ¿Te gustaria aprender algo de python hoy?"
print(mensaje)

# 2-4 
nombre_completo = 'paulo arce'
print(nombre_completo.lower()) # minúsculas
print(nombre_completo.upper()) # mayúsculas
print(nombre_completo.title()) # title

# 2-5
autor = 'Warren Buffett'
frase = "Lo que aprendemos de la historia es que las personas no aprenden de la historia"
print(f'{autor} dijo una vez: "{frase}"')

# 2-6 
persona_famosa = 'Marco Aurelio'
mensaje = "La tranquilidad viene cuando dejas de preocuparte por lo que dirán"
print(f'{persona_famosa} una vez dijo: "{mensaje}"')

# 2-7 
futbolista_favorito = '  \nLionel \tMessi  '
print(futbolista_favorito)
print(futbolista_favorito.rstrip()) # elimina espacios del lado derecho
print(futbolista_favorito.lstrip()) # elimina espacios del lado izquierdo
print(futbolista_favorito.strip()) # elimina espacios extras

# 2-8
nombre_de_archivo = 'python_notes.txt'
print(nombre_de_archivo.removesuffix('.txt'))