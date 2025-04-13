# %%
#10
#Preguntar al usuario en que hemisferio N/S
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Determinar estación
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio inválido"
    
print("Estación:", estacion)


# %%
#9
#Pedir al usuario la magnitud de un terremoto
magnitud = float(input("Ingrese magnitud: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print ("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
elif magnitud >= 7 :
    print("Extremo")

# %%
#8
#Pedir al usuario que ingrese su nombre y el numero 1,2 0 3 para seleccionar una opcion
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese el numero de la opcion que desea seleccionar: ")
# Las opciones
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())

# %%
#7
# Pedir una frase o palabra al usuario
palabra = input("Ingrese una frase o palabra: ")

# Verifico si termina en vocal (minúscula o mayúscula)
if palabra[-1].lower() in 'aeiou':
    palabra += "!"
print(palabra)




# %%
#6
#Tomar la lista de numeros_aleatorios calcular su moda, mediana y media y los compare por sesgo positivo negativo o no hay sesgo
import random
from statistics import mean, median, mode

# Generar la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular media, mediana y moda
media_valor = mean(numeros_aleatorios)
mediana_valor = median(numeros_aleatorios)
moda_valor = mode(numeros_aleatorios)

# Mostrar los valores
print(f"Media: {media_valor}")
print(f"Mediana: {mediana_valor}")
print(f"Moda: {moda_valor}")

# Evaluar el tipo de sesgo
if media_valor > mediana_valor > moda_valor:
    print("Sesgo positivo (a la derecha)")
elif media_valor < mediana_valor < moda_valor:
    print("Sesgo negativo (a la izquierda)")
elif media_valor == mediana_valor == moda_valor:
    print("Sin sesgo")
else:
    print("No hay sesgo")#7


# %%
#5
#Permitir introducir contraseña de entre 8 y 14 caracteres
contraseña = input("Ingrese su contraseña: ")
#Evaluamos la cantidad de caracteres
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# %%
#4
#Pedir al usuario su edad para saber su categoria
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad >=12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30 :
    print("Adulto/a")


# %%
#3
# Permitir solo números pares

numero = int(input("Ingrese un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# %%
#2
#Pedir al usuario su nota
nota = float(input("Ingrese su nota: "))
#Si la nota es mayor o igual a 6, mostrar un mensaje de aprobado
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# %%
#1
#Pedir al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))
#Si el usuario es mayor de 18 años mostrar "Es mayor de edad"
if edad > 18:
    print("Es mayor de edad")
else: 
    print("Es menor de edad")


