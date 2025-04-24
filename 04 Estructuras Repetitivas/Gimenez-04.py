
import random

# Actividad 1: Imprime todos los números del 0 al 100, uno por línea.
def actividad_1():
    for i in range(101):
        print(i)

# Actividad 2: Solicita un número entero y muestra cuántos dígitos tiene.
def actividad_2():
    numero = input("Ingresa un número entero: ")
    print(f"El número tiene {len(numero.strip('-'))} dígitos.")

# Actividad 3: Suma todos los números enteros entre dos valores ingresados por el usuario (excluyéndolos).
def actividad_3():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    suma = sum(range(min(a, b)+1, max(a, b)))
    print(f"La suma es: {suma}")

# Actividad 4: Suma secuencialmente los números ingresados por el usuario hasta que se ingrese un 0.
def actividad_4():
    total = 0
    while True:
        numero = int(input("Ingresa un número (0 para terminar): "))
        if numero == 0:
            break
        total += numero
    print(f"La suma total es: {total}")

# Actividad 5: Juego para adivinar un número aleatorio entre 0 y 9.
def actividad_5():
    secreto = random.randint(0, 9)
    intentos = 0
    while True:
        intento = int(input("Adivina el número (0-9): "))
        intentos += 1
        if intento == secreto:
            print(f"¡Correcto! Lo lograste en {intentos} intentos.")
            break
        else:
            print("Incorrecto. Intenta de nuevo.")

# Actividad 6: Imprime los números pares del 100 al 0 en orden decreciente.
def actividad_6():
    for i in range(100, -1, -1):
        if i % 2 == 0:
            print(i)

# Actividad 7: Suma todos los números desde 0 hasta un número ingresado por el usuario.
def actividad_7():
    n = int(input("Ingresa un número entero positivo: "))
    total = sum(range(n + 1))
    print(f"La suma es: {total}")

# Actividad 8: Ingresa 100 números y cuenta pares, impares, negativos y positivos.
def actividad_8():
    cantidad = 100  # Cambiar este valor para pruebas
    pares = impares = negativos = positivos = 0
    for _ in range(cantidad):
        numero = int(input("Ingresa un número entero: "))
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        if numero >= 0:
            positivos += 1
        else:
            negativos += 1
    print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

# Actividad 9: Ingresa 100 números y calcula la media.
def actividad_9():
    cantidad = 100  # Cambiar este valor para pruebas
    suma = 0
    for _ in range(cantidad):
        numero = int(input("Ingresa un número entero: "))
        suma += numero
    media = suma / cantidad
    print(f"La media es: {media}")

# Actividad 10: Invierte los dígitos de un número ingresado por el usuario.
def actividad_10():
    numero = input("Ingresa un número: ")
    invertido = numero[::-1]
    print(f"Número invertido: {invertido}")

# Menú para seleccionar y ejecutar las actividades
def menu():
    while True:
        print("\nMenú de Actividades:")
        for i in range(1, 11):
            print(f"{i}) Actividad {i}")
        print("0) Salir")
        opcion = input("Elegí una opción: ")
        if opcion == '0':
            break
        elif opcion == '1':
            actividad_1()
        elif opcion == '2':
            actividad_2()
        elif opcion == '3':
            actividad_3()
        elif opcion == '4':
            actividad_4()
        elif opcion == '5':
            actividad_5()
        elif opcion == '6':
            actividad_6()
        elif opcion == '7':
            actividad_7()
        elif opcion == '8':
            actividad_8()
        elif opcion == '9':
            actividad_9()
        elif opcion == '10':
            actividad_10()
        else:
            print("Opción no válida.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu()
