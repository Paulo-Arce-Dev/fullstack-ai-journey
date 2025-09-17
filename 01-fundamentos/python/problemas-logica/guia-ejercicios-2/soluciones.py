# Ejercicio 1

horas_trabajadas = int(input("Ingrese la cantidad de sus horas trabajadas: "))
valor_pago_hora = float(input("Ingrese el valor que se paga por hora trabajada: "))

sueldo = round(horas_trabajadas, 2) * valor_pago_hora
print(f"Su sueldo total es de: {sueldo} USD")



# Ejercicio 2 

numero_uno = int(input("Ingrese un número por favor: "))
numero_dos = int(input("Ingrese un segundo número por favor: "))

print(f"Su primer número es: {numero_uno}")
print(f"Su segundo número es: {numero_dos}")

# intercambiamos sus valores
aux = numero_uno
numero_uno = numero_dos
numero_dos = aux 

print("------------------------------------------------")
print(f"Su primer número ahora es: {numero_uno}")
print(f"Su segundo número ahora es: {numero_dos}")



# Ejercicio 3

sueldo_fijo = 5000
pago_por_auto_vendido = 700

autos_vendidos = int(input("Ingrese la cantidad de autos vendidos por favor: "))
monto_total_autos_vendidos = pago_por_auto_vendido * autos_vendidos

sueldo_total = sueldo_fijo + monto_total_autos_vendidos
print(f"Su sueldo total a pagar es de: {sueldo_total} USD")



# Ejercicio 4
asientos_totales_avion = int(input("Ingresa la cantidad de asientos totales del avión: "))
cantidad_pasajes_ocupados = int(input("Ingresa la cantidad de pasajes ocupados: "))

porcentaje_ocupacion = (cantidad_pasajes_ocupados * 100) / asientos_totales_avion
porcenjade_desocupado = 100 - porcentaje_ocupacion

print(f"El porcenjae de ocupación del avión es del: {porcentaje_ocupacion}%")
print(f"El porcentaje sin ocupar es del: {porcenjade_desocupado}%")