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

# último elemento de una lista

# pop() elimina el último elemento de la lista, pero permite trabajar con ese elemento después de eliminarlo.
moto_rota = motos_2.pop()
print(motos_2)
print(moto_rota)

ultima_moto = motos_2.pop()
print(f"la última moto que tuve fue una {ultima_moto}")

# pop() también elimina un elemento en cualquier posición
primera_moto = motos_2.pop(0)
print(f"Mi primera moto fue {primera_moto}")

# NOTA: cuando desee eliminar un elemento de una lista y no utilizar ese elemento de ninguna manera, utilice la instrucción "del"
# Si desea utilizar un elemento mientras lo elimina, utilice el método pop().

# eliminar un elemento por valor

# A veces no sabrás la posición del valor que deseas eliminar de una lista. 
# Si solo conoce el valor del elemento que desea eliminar, puede utilizar el método remove(). 
# El método remove() elimina solo la primera aparición del valor que especifica.
print(motos)
motos.remove('Ducati')
print(motos)

demasiado_caro = 'KTM'
motos.remove(demasiado_caro)
print(motos)
print(f"\nUna {demasiado_caro.title()} es demasiado cara para mi en este momento.")