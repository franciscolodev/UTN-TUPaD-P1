#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario

numero = int(input("Ingresa un número entero positivo: "))

# Verificar que el número sea positivo
if numero >= 0:
# Calculo de la suma de los números entre 0 y el número indicado
    suma = sum(range(numero + 1))  # genera los números de 0 al numero indicado
    
# Mostrar el resultado
    print(f"La suma de los números entre 0 y {numero} es: {suma}")
else:
    print("Por favor, ingresa un número entero positivo.")