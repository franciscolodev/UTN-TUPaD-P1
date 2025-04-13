#2)Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene

numero = int(input("Ingresa un número entero: "))

# Convertir el número a string y contar la cantidad de dígitos
cantidad_digitos = len(str(abs(numero)))  

# Mostrar la cantidad de dígitos
print(f"El número {numero} tiene {cantidad_digitos} dígitos.")