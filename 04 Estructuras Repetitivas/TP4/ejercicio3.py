#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores

# Solicitar los dos valores 
inicio = int(input("Ingresa el primer número entero: "))
fin = int(input("Ingresa el segundo número entero: "))

# Para que el valor de "inicio" sea menor que "fin"
if inicio > fin:
    inicio, fin = fin, inicio  # Intercambia los valores si es necesario

# Calcular la suma de los números entre "inicio" y "fin", excluyendo ambos
suma = sum(range(inicio + 1, fin))

# Mostrar resultado
print(f"La suma de los números entre {inicio} y {fin}, excluyéndolos, es: {suma}")