📚 Proyecto de Estructuras de Datos y Programación en Python
Este proyecto incluye una serie de ejercicios prácticos diseñados para reforzar el conocimiento de estructuras de datos (diccionarios, listas, pilas, colas, listas enlazadas) y conceptos de programación orientada a objetos con Python.

🧠 Contenidos
1. Manejo de Diccionarios
Se trabaja con el diccionario precios_frutas, realizando:

Agregado de elementos.

Actualización de precios.

Extracción de las claves (nombres de frutas).

2. Clases y Objetos
Se crean dos clases:

👤 Persona
Atributos: nombre, pais, edad.

Método: saludar() que imprime un saludo personalizado.

⚪ Circulo
Atributo: radio.

Métodos:

calcular_area(): Calcula el área del círculo.

calcular_perimetro(): Calcula el perímetro del círculo.

3. Verificación de Paréntesis Balanceados
Se implementa una función estaBalanceado(cadena) que:

Utiliza una pila (stack) para validar si los paréntesis están correctamente balanceados.

Compatible con (), {}, [].

4. Simulación de Cola en un Banco
Clase Turnero:

Implementa una cola con deque.

Métodos:

encolar()

desencolar()

siguiente()

esta_vacia()

5. Lista Enlazada Simple
Clase ListaEnlazada con nodos insertados al inicio:

Método insertar(dato): Inserta un nodo al inicio.

Método mostrar(): Recorre e imprime los datos.

Método invertir_lista(): Invierte el orden de los nodos usando una pila.

🧪 Ejecución
Podés ejecutar este proyecto desde cualquier entorno Python compatible. Solo necesitás tener instalado Python 3.x y ejecutar el archivo .py con:
Gimenez_datos_complejos.py

🛠 Requisitos
Python 3.x

Módulos usados:

math

collections.deque (para la cola)

📌 Notas
El código está estructurado y comentado para facilitar su lectura.

Se utiliza tipado estático (list[str], -> None) como buena práctica.

Desarrollado por Gimenez Jode Dario