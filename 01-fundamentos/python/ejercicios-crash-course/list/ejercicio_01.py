# Ejercicios de listas []

"""  
3-1. Nombres: Almacena los nombres de algunos de sus amigos en una lista llamada nombres.
Imprime el nombre de cada persona accediendo a cada elemento de la lista, uno a la vez.

3-2. Saludos: Comience con la lista que utilizó en el ejercicio anterior, pero en lugar de simplemente imprimir el nombre de cada persona, imprima un mensaje para ellos.
El texto de cada mensaje debe ser el mismo, pero cada mensaje debe estar personalizado con el nombre de la persona.

3-3. Tu propia lista: Piensa en tu medio de transporte favorito, como una motocicleta o un automóvil, y haz una lista que contenga varios ejemplos.
Utilice su lista para imprimir una serie de declaraciones sobre estos elementos, como "Me gustaria tener una moto Honda".
"""

# 3-1
nombres = ['Gabriel', 'Sebastian', 'Jonathan']
print(nombres[0].title())
print(nombres[1].title())
print(nombres[2].title())

# 3-2
print(f"Con mi amigo {nombres[0].title()} las risas nunca faltan")
print(f"Con mi amigo {nombres[1].title()} las risas nunca faltan")
print(f"Con mi amigo {nombres[2].title()} las risas nunca faltan")

# 3-3
autos_favoritos = ['Nissan Skyline', 'Golf GTI', 'Mercedes-AMG Clase A Hatchback', 'Audi RS 3 Sportback']
print(f"Me gustaría tener un {autos_favoritos[0]} gris y azúl")
print(f"Tendría un {autos_favoritos[1]} para viajar con tranqulidad")
print(f"Uno de los autos que sueño tener es el {autos_favoritos[2]}")
print(f"Mi mayor anhelo de vehículo es un {autos_favoritos[3]}")