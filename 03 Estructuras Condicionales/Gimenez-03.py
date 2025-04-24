{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "172fd692",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estación: Hemisferio inválido\n"
     ]
    }
   ],
   "source": [
    "#10\n",
    "#Preguntar al usuario en que hemisferio N/S\n",
    "hemisferio = input(\"¿En qué hemisferio estás? (N/S): \").upper()\n",
    "mes = int(input(\"¿Qué mes es? (1-12): \"))\n",
    "dia = int(input(\"¿Qué día es? (1-31): \"))\n",
    "\n",
    "# Determinar estación\n",
    "if hemisferio == \"N\":\n",
    "    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):\n",
    "        estacion = \"Invierno\"\n",
    "    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):\n",
    "        estacion = \"Primavera\"\n",
    "    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):\n",
    "        estacion = \"Verano\"\n",
    "    else:\n",
    "        estacion = \"Otoño\"\n",
    "elif hemisferio == \"S\":\n",
    "    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):\n",
    "        estacion = \"Verano\"\n",
    "    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):\n",
    "        estacion = \"Otoño\"\n",
    "    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):\n",
    "        estacion = \"Invierno\"\n",
    "    else:\n",
    "        estacion = \"Primavera\"\n",
    "else:\n",
    "    estacion = \"Hemisferio inválido\"\n",
    "    \n",
    "print(\"Estación:\", estacion)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "f7b4d19c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fuerte\n"
     ]
    }
   ],
   "source": [
    "#9\n",
    "#Pedir al usuario la magnitud de un terremoto\n",
    "magnitud = float(input(\"Ingrese magnitud: \"))\n",
    "if magnitud < 3:\n",
    "    print(\"Muy leve\")\n",
    "elif magnitud >= 3 and magnitud < 4:\n",
    "    print (\"Leve\")\n",
    "elif magnitud >= 4 and magnitud < 5:\n",
    "    print(\"Moderado\")\n",
    "elif magnitud >= 5 and magnitud < 6:\n",
    "    print(\"Fuerte\")\n",
    "elif magnitud >= 6 and magnitud < 7:\n",
    "    print(\"Muy fuerte\")\n",
    "elif magnitud >= 7 :\n",
    "    print(\"Extremo\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "43418340",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dario\n"
     ]
    }
   ],
   "source": [
    "#8\n",
    "#Pedir al usuario que ingrese su nombre y el numero 1,2 0 3 para seleccionar una opcion\n",
    "nombre = input(\"Ingrese su nombre: \")\n",
    "opcion = input(\"Ingrese el numero de la opcion que desea seleccionar: \")\n",
    "# Las opciones\n",
    "if opcion == \"1\":\n",
    "    print(nombre.upper())\n",
    "elif opcion == \"2\":\n",
    "    print(nombre.lower())\n",
    "elif opcion == \"3\":\n",
    "    print(nombre.title())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "19cab339",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "casar\n"
     ]
    }
   ],
   "source": [
    "#7\n",
    "# Pedir una frase o palabra al usuario\n",
    "palabra = input(\"Ingrese una frase o palabra: \")\n",
    "\n",
    "# Verifico si termina en vocal (minúscula o mayúscula)\n",
    "if palabra[-1].lower() in 'aeiou':\n",
    "    palabra += \"!\"\n",
    "print(palabra)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "14c0d893",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Media: 48.78\n",
      "Mediana: 47.5\n",
      "Moda: 10\n",
      "Sesgo positivo (a la derecha)\n"
     ]
    }
   ],
   "source": [
    "#6\n",
    "#Tomar la lista de numeros_aleatorios calcular su moda, mediana y media y los compare por sesgo positivo negativo o no hay sesgo\n",
    "import random\n",
    "from statistics import mean, median, mode\n",
    "\n",
    "# Generar la lista de números aleatorios\n",
    "numeros_aleatorios = [random.randint(1, 100) for i in range(50)]\n",
    "\n",
    "# Calcular media, mediana y moda\n",
    "media_valor = mean(numeros_aleatorios)\n",
    "mediana_valor = median(numeros_aleatorios)\n",
    "moda_valor = mode(numeros_aleatorios)\n",
    "\n",
    "# Mostrar los valores\n",
    "print(f\"Media: {media_valor}\")\n",
    "print(f\"Mediana: {mediana_valor}\")\n",
    "print(f\"Moda: {moda_valor}\")\n",
    "\n",
    "# Evaluar el tipo de sesgo\n",
    "if media_valor > mediana_valor > moda_valor:\n",
    "    print(\"Sesgo positivo (a la derecha)\")\n",
    "elif media_valor < mediana_valor < moda_valor:\n",
    "    print(\"Sesgo negativo (a la izquierda)\")\n",
    "elif media_valor == mediana_valor == moda_valor:\n",
    "    print(\"Sin sesgo\")\n",
    "else:\n",
    "    print(\"No hay sesgo\")#7\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "64742622",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ha ingresado una contraseña correcta\n"
     ]
    }
   ],
   "source": [
    "#5\n",
    "#Permitir introducir contraseña de entre 8 y 14 caracteres\n",
    "contraseña = input(\"Ingrese su contraseña: \")\n",
    "#Evaluamos la cantidad de caracteres\n",
    "if len(contraseña) >= 8 and len(contraseña) <= 14:\n",
    "    print(\"Ha ingresado una contraseña correcta\")\n",
    "else:\n",
    "    print(\"Por favor, ingrese una contraseña de entre 8 y 14 caracteres\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "13628fb1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Adulto/a\n"
     ]
    }
   ],
   "source": [
    "#4\n",
    "#Pedir al usuario su edad para saber su categoria\n",
    "edad = int(input(\"Ingrese su edad: \"))\n",
    "if edad < 12:\n",
    "    print(\"Niño/a\")\n",
    "elif edad >=12 and edad < 18:\n",
    "    print(\"Adolescente\")\n",
    "elif edad >= 18 and edad < 30:\n",
    "    print(\"Adulto/a joven\")\n",
    "elif edad >= 30 :\n",
    "    print(\"Adulto/a\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a0d44665",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ha ingresado un número par\n"
     ]
    }
   ],
   "source": [
    "#3\n",
    "# Permitir solo números pares\n",
    "\n",
    "numero = int(input(\"Ingrese un número par: \"))\n",
    "\n",
    "if numero % 2 == 0:\n",
    "    print(\"Ha ingresado un número par\")\n",
    "else:\n",
    "    print(\"Por favor, ingrese un número par\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "54cd32dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Desaprobado\n"
     ]
    }
   ],
   "source": [
    "#2\n",
    "#Pedir al usuario su nota\n",
    "nota = float(input(\"Ingrese su nota: \"))\n",
    "#Si la nota es mayor o igual a 6, mostrar un mensaje de aprobado\n",
    "if nota >= 6:\n",
    "    print(\"Aprobado\")\n",
    "else:\n",
    "    print(\"Desaprobado\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8212ca4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Es mayor de edad\n"
     ]
    }
   ],
   "source": [
    "#1\n",
    "#Pedir al usuario que ingrese su edad\n",
    "edad = int(input(\"Ingrese su edad: \"))\n",
    "#Si el usuario es mayor de 18 años mostrar \"Es mayor de edad\"\n",
    "if edad > 18:\n",
    "    print(\"Es mayor de edad\")\n",
    "else: \n",
    "    print(\"Es menor de edad\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
