#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el  usuario. 

numero = int(input("Ingresa un número entero: "))

# Para convertir el número a cadena, invertirlo y después volver a convertirlo en entero
numero_invertido = int(str(abs(numero))[::-1])

# Si el número original es negativo, se vuelve a colocar el signo
if numero < 0:
    numero_invertido = -numero_invertido

# Mostrar número invertido
print(f"El número invertido es: {numero_invertido}")