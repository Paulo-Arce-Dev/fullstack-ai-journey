# Ejercicios de listas

"""  
3-4. Lista de invitados: Si pudieras invitar a cenar a alguien, vivo o fallecido, ¿a quién invitarías? Haz una lista que incluya al menos tres personas a las que te gustaria invitar a cenar. 
Luego use su lista para imprimir un mensaje para cada persona, invitándolas a cenar.

3-5. Cambio de lista de invitados: Acabas de enterarte que uno de tus invitados no puede asistir a la cena, por lo que debes enviar un nuevo conjunto de invitaciones. Tendrás que pensar en alguien más a quien invitar.

  - Comience su programa del Ejercicio 3-4. Agregue una llamada print() al final de su programa, indicando el nombre del invitado que no puede asistir.
  
  - Modifica tu lista, reemplazando el nombre del húesped que no puede asistir con el nombre de la nueva persona que estás invitando.

  - Imprima un segundo conjunto de mensajes de invitación, uno para cada persona que aún esté en tu lista.
  
  
3-6. Más invitados: Acaba de encontrar una mesa de comedor más grande, por lo que hay más espacio disponible. Piensa en tres invitados más para invitar a cenar.

  - Comience su programa del Ejercicio 3-4 o 3-5. Agregue una llamada print() al final de su programa, informando a las personas que encontró una tabla más grande.
  
  - Utilice insert() para agregar un nuevo invitado al principio de su lista.
  
  - Utilice insert() para agreagr un nuevo invitado al medio de su lista.
  
  - Utilice append() para agreagr un nuevo invitado al final de su lista.
  
  - Imprima un nuevo conjunto de mensajes de invitación, uno para cada persona de su lista.
  
  
3-7. Lista de invitados cada vez más reducida: Acaba de descubrir que su nueva mesa no llegará a tiempo para la cena y ahora tiene espacio para solo dos invitados.
  - Comience su programa con el Ejercicio 3-6. Agregue una nueva línea que imprima un mensaje que indique que solo puede invitar a dos personas a cenar.
  
  - Utilice pop() para eliminar invitados de su lista uno a la vez hastra que solo queden dos nombres de su lista. Cada vez que saque un nombre de su lista, imprima su mensaje para esa persona haciéndole saber que lamenta no poder invitarla a cenar.
  
  - Imprima un mensaje para cada una de las dos personas que aún están en su lista, de modo que tenga una lista vacía.
    Imprima su lista para asegurarse de tener una lista vacía al final de su programa. 
"""

# 3-4
lista_invitados_cenar = ['Messi', 'Warren Buffet','Elon Musk']
invitado_1 = lista_invitados_cenar[0]
print(f"Me dirigo a {invitado_1} para invitarlo a una cena que recordará como el espacio donde pude ser")

invitado_2 = lista_invitados_cenar[1]
print(f"Me dirigo a {invitado_2} para invitarlo a una cena que recordará como el espacio donde pude ser")

invitado_3 = lista_invitados_cenar[2]
print(f"Me dirigo a {invitado_3} para invitarlo a una cena que recordará como el espacio donde pude ser")

print(f"{invitado_3} no podrá asistir a la cena por motivos de agenda.")

# 3-5
eliminar_invitado_ausente = lista_invitados_cenar.remove(invitado_3)
invitado_nuevo = 'Zenón de Citio'
lista_invitados_cenar.append(invitado_nuevo)
# print(lista_invitados_cenar)

print(f"Me dirigo a {invitado_1} para invitarlo a una cena que recordará como el espacio donde pude ser")
print(f"Me dirigo a {invitado_2} para invitarlo a una cena que recordará como el espacio donde pude ser")
print(f"Me dirigo a {invitado_nuevo} para invitarlo a una cena que recordará como el espacio donde pude ser")