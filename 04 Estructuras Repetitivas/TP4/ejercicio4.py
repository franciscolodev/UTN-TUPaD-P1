#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

# Inicia la variable que almacenará la suma
suma_total = 0

# Solicita el primer número
numero = int(input("Ingresa un número entero: "))

# Bucle que pide números hasta que se ingrese 0
while numero != 0:
    suma_total += numero  # Suma el número ingresado
    numero = int(input("Ingresa un número entero: "))  # Solicita el siguiente número

# Muestra total acumulado
print(f"El total acumulado es: {suma_total}")