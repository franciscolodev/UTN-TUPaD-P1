#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la  media de esos valores. 

cantidad_numeros = 100

# Inicia la variable para almacenar la suma de los números
suma = 0

# Solicitar los números al usuario
for i in range(cantidad_numeros):
    numero = int(input(f"Ingresa el número {i + 1}: "))
    suma += numero  # Acumular la suma de los números

# Para calcular la media
media = suma / cantidad_numeros

# Mostrar resultado
print(f"\nLa media de los {cantidad_numeros} números es: {media}")