#TP3 - Francisco López

#1)Escribir un programa que solicite la edad del usuario y compruebe si es mayor de edad
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")


#2)Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


#3)Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par"
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


#4)Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las categorías pertenece:
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


#5)Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string
contraseña = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#6)Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Números aleatorios:", numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("Distribución sin un sesgo claro")


#7)Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
texto = input("Ingrese una frase o palabra: ")

if texto[-1].lower() in 'aeiou':
    texto += "!"  

print("Resultado:", texto)


#8)Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee
nombre = input("Ingrese su nombre: ")

print("Seleccione una opción:")
print("1. Nombre en MAYÚSCULAS")
print("2. Nombre en minúsculas")
print("3. Nombre con la primera letra mayúscula")
opcion = input("Ingrese 1, 2 o 3: ")

if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción inválida. Por favor, ingrese 1, 2 o 3.")


#9)Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las categorías según la escala de Richter e imprima el resultado por pantalla:
magnitud = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:  
    print("Extremo (puede causar graves daños a gran escala)")

#10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input("¿En qué hemisferio estás? (N para norte / S para sur): ").upper()
mes = int(input("¿Qué mes es? (en número, ej: enero = 1): "))
dia = int(input("¿Qué día es?: "))

def estacion_norte(mes, dia):
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        return "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        return "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        return "Verano"
    else:
        return "Otoño"

def estacion_sur(mes, dia):
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        return "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        return "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        return "Invierno"
    else:
        return "Primavera"

if hemisferio == "N":
    estacion = estacion_norte(mes, dia)
elif hemisferio == "S":
    estacion = estacion_sur(mes, dia)
else:
    estacion = "Hemisferio no válido"

print("Estás en:", estacion)

