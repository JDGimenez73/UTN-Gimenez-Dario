#Hola Mundo
print(f"Hola mundo")

#Pido al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")
# Imprimo el resultado
print(f"Hola {nombre}!")


#Pedir al usuaro que ingrese sus datos
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su lugar de residencia: ")
#Imprimir el resultado    
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")


#Pedir al usuario que ingrese el radio del circulo
radio = float(input("Ingrese el radio del círculo: "))
#Hacer el calculo
area = 3.14159 * (radio ** 2)
perimetro = 2 * 3.14159 * radio
# Imprimir el resultado
print(f"El área del círculo es: {area} y su perímetro es:{perimetro}.")


# Pedir al usuario la cantidad de segundos
segundos = int(input("Ingrese la cantidad de segundos: "))
# Convertir segundos a horas
horas = segundos / 3600
# Imprimir el resultado
print(f"La cantidad de segundos {segundos} equivale a {horas} horas")


# Pedir un número al usuario
numero = int(input("Ingrese un número: "))
# Imprimir la tabla de multiplicar
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")  # Imprimir


# Pedir dos números enteros al usuario
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
# Validar que los números enteros sean distintos de 0
while num1 == 0 or num2 == 0:
    print("Error: Los números enteros no pueden ser 0")
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))
    # Mostrar el resultado de sumarlos, dividirlos, multiplicarlos y restar
    print(f"La suma de {num1} y {num2} es: {num1 + num2}")
    print(f"La división de {num1} entre {num2} es: {num1 / num2}")
    print(f"La multiplicación de {num1} y {num2} es: {num1 * num2}")
    print(f"La resta de {num1} y {num2} es: {num1 - num2}")


# Pido al usuario su altura y su peso
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
# Calculo el índice de masa corporal
imc = peso / (altura ** 2)
# Imprimo el resultado
print(f"Su índice de masa corporal es: {imc:.2f}")


# Pedir al usuario una temperatura en grados Celsius
temperatura_celsius = float(input("Ingrese una temperatura en grados Celsius: "))
# Convertir la temperatura de Celsius a Fahrenheit
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
# Imprimir la temperatura en grados Fahrenheit
print(f"La temperatura en grados Fahrenheit es: {temperatura_fahrenheit}°F")


# Pedir 3 números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
# Calcular el promedio de los 3 números
promedio = (num1 + num2 + num3) / 3
# Imprimir el promedio por pantalla
print("El promedio de los 3 números es: ", promedio)

