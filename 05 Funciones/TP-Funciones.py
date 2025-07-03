#TP Funciones - Francisco López - Tecnicatura Universitaria en Programación (UTN)
import math

#1. Función que imprime "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")

#2. Función que saluda al usuario
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

#3. Función que muestra la información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4. Funciones para calcular área y perímetro de un círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

#5. Función para convertir de segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

#6. Función para imprimir la tabla de multiplicar de un número
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

#7. Función que devuelve la suma, resta, multiplicación y división entre dos números
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida"
    return suma, resta, multiplicacion, division

#8. Función para calcular el Índice de Masa Corporal (IMC)
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

#9. Función que convierte Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#10. Función para calcular el promedio entre tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3


# MAIN
if __name__ == "__main__":
    #Ejercicio 1
    imprimir_hola_mundo()
    
    #Ejercicio 2
    nombre = input("Ingrese su nombre: ")
    print(saludar_usuario(nombre))

    #Ejercicio 3
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    residencia = input("Lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

    #Ejercicio 4
    radio = float(input("Ingrese el radio del círculo: "))
    print(f"Área: {calcular_area_circulo(radio):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

    #Ejercicio 5
    segundos = int(input("Ingrese una cantidad de segundos: "))
    print(f"Equivale a {segundos_a_horas(segundos):.2f} horas")

    #Ejercicio 6
    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)

    #Ejercicio 7
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    suma, resta, mult, div = operaciones_basicas(a, b)
    print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {mult}, División: {div}")

    #Ejercicio 8
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    print(f"Su IMC es: {calcular_imc(peso, altura):.2f}")

    #Ejercicio 9
    celsius = float(input("Ingrese temperatura en grados Celsius: "))
    print(f"Temperatura en Fahrenheit: {celsius_a_fahrenheit(celsius):.2f}")

    #Ejercicio 10
    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))
    n3 = float(input("Ingrese el tercer número: "))
    print(f"Promedio: {calcular_promedio(n1, n2, n3):.2f}")