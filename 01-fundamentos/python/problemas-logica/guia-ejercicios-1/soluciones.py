# ejercicio 1 

def calculadora_suma (num1, num2):
  return num1 + num2

print(f"El resultado de la suma es {calculadora_suma(34, 56)}")

# ejercicio 2
num_usuario = int(input("Ingrese un número para elevarlo al cubo "))

resultado = (num_usuario * num_usuario) * num_usuario
print(f"El número {num_usuario} elevado al cubo es: {resultado}")

# ejercicio 3
ano_actual = int(input("Ingrese el año actual en número "))
ano_fecha_nacimiento = int(input("Ingrese el año de su nacimiento "))

edad_usuario = ano_actual - ano_fecha_nacimiento
print(f"Su edad es {edad_usuario} años")

# ejercicio 4
distancia_entre_ciudades = float(input("Ingrese la distancia entre dos ciudades en kilometros: "))
velocidad_promedio_vehiculo = float(input("Ingrese la velocidad promedio de su vehículo en K/H: "))
