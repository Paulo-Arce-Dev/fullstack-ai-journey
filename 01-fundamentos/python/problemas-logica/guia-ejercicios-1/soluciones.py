# ejercicio 1 

def calculadora_suma (num1, num2):
  return num1 + num2

print(f"El resultado de la suma es {calculadora_suma(34, 56)}")


# ejercicio 2
"""  
num_usuario = int(input("Ingrese un número para elevarlo al cubo "))

resultado = (num_usuario * num_usuario) * num_usuario
print(f"El número {num_usuario} elevado al cubo es: {resultado}")
"""

# ejercicio 3
"""  
ano_actual = int(input("Ingrese el año actual en número "))
ano_fecha_nacimiento = int(input("Ingrese el año de su nacimiento "))

edad_usuario = ano_actual - ano_fecha_nacimiento
print(f"Su edad es {edad_usuario} años")
"""


# ejercicio 4

# teniendo en cuenta que tiempo = distancia / velocidad
"""  
distancia_entre_ciudades = float(input("Ingrese la distancia entre dos ciudades en kilometros: "))
velocidad_promedio_vehiculo = float(input("Ingrese la velocidad promedio de su vehículo en Km/H: "))

tiempo_en_hora = distancia_entre_ciudades / velocidad_promedio_vehiculo
tiempo_formateado = round(tiempo_en_hora, 2)

if (tiempo_formateado < 1):
  tiempo_en_minutos = tiempo_formateado * 60
  print(f"El tiempo estimado de llegada es de: {tiempo_en_minutos} minutos")
else:
  print(f"El tiempo estimado de llegada es de: {tiempo_formateado} horas")
"""

  
# ejercicio 5

"""  
# sueldo fijo en ARS
SUELDO = 15000

# comision en porcentaje sobre el total facturado
COMISION = 5 / 100

total_facturado = int(input("Ingrese el total facturado del empleado: "))
total_a_pagar = (total_facturado * COMISION) + SUELDO

print(f"El sueldo total a pagar al empleado es de: {total_a_pagar} ARS")
"""

# ejercicio 6
"""  
nota_uno = int(input("Ingrese una nota de su exámen: "))
nota_dos = int(input("Ingrese una segunda nota de su exámen: "))
nota_tres = int(input("Ingrese una tercera nota de su exámen: "))

promedio_notas = (nota_uno + nota_dos + nota_tres) / 3
print(f"Su promedio es de: {round(promedio_notas, 2)}")
"""


# ejercicio 7 
""" 
metros_cuadrados_totales = float(input("Ingresa los metros cuadrados totales del predio: "))
metros_cuadrados_cubiertos = float(input("Ingresa los metros cuadrados cubiertos del predio: "))

# calcular el porcentaje de m/2 cubiertos y el porcentaje de m/2 descubierto
porcentaje_metros_cubiertos = (metros_cuadrados_cubiertos * 100) / metros_cuadrados_totales
print(f"El procentaje de metros cubiertos es de: {round(porcentaje_metros_cubiertos, 2)} %")

porcentaje_metros_descubiertos = 100 - porcentaje_metros_cubiertos
print(f"El procentaje de metros descubiertos es de: {round(porcentaje_metros_descubiertos, 2)} %")
"""

# ejercicio 8

descuento = 15 / 100

monto_total = float(input("Ingrese el monto toal de su compra: "))
total_pagar = monto_total - (monto_total * descuento)

print(f"El monto total a pagar es de: ${total_pagar} ARS con un 15% de descuento")
 

