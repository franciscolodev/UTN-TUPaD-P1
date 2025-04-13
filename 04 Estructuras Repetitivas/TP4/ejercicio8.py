#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el  programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos...

cantidad_numeros = 100

# Inicia los contadores
pares = 0
impares = 0
negativos = 0
positivos = 0

# Solicita los números al usuario
for i in range(cantidad_numeros):
    numero = int(input(f"Ingresa el número {i + 1}: "))
    
    # Cuenta los pares e impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Cuenta los negativos y positivos
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1

# Mostrar resultados
print(f"\nResultados:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números negativos: {negativos}")
print(f"Números positivos: {positivos}")