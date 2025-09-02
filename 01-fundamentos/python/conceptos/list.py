# Listas []

bicicletas = ['trek', 'redline', 'cannondale']
print(bicicletas)

# acceder a elementos de lisas
print(bicicletas[0])
print(bicicletas[0].title())
print(bicicletas[1])
print(bicicletas[2])

# último elemento de una lista
print(bicicletas[-1])

mensaje = f"Mi primera bicicleta fue una {bicicletas[0].title()}"
print(mensaje)


# modificar elementos de una lista
motos = ['Honda', 'Yamaha','Suzuki', 'KTM']
print(motos)

# modificando Honda -> Dukati
motos[0] = 'Ducati'
print(motos)

# agregar elemento al final de una lista
motos.append('Kawasaki')
print(motos)

motos_2 = []
motos_2.append('Honda')
motos_2.append('Kawasaki')
motos_2.append('Suzuki')
print(motos_2)

# agregar elemento a lista (cualquier orden)
motos_2.insert(0, 'Ducati')
print(motos_2)

# eliminar elemento de una lista

# si conocemos la posición del elemento
del motos_2[0]
print(motos_2)

# último elemento de una lista -> pop()
motos_2.pop()
print(motos_2)