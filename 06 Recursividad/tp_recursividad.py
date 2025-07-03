#TP Recursividad - Francisco López - Programación I (UTN)

#1. Función para calcular e imprimir el factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

#2. Función para calcular valor de la serie de Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

#3. Función para calcular la potencia con recursividad
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

#4. Función para convertir a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

#5. Palíndromo: Función que devuelva True o False
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

#6. Suma de dígitos
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

#7. Pirámide de bloques
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

#8. Contar dígitos en número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    coincidencia = 1 if numero % 10 == digito else 0
    return coincidencia + contar_digito(numero // 10, digito)

#Ejecución 
if __name__ == "__main__":
    print("1) Factorial:")
    n = int(input("Ingrese un número: "))
    for i in range(1, n + 1):
        print(f"{i}! = {factorial(i)}")

    print("\n2) Fibonacci:")
    n = int(input("Cantidad de términos de Fibonacci: "))
    for i in range(n):
        print(fibonacci(i), end=" ")

    print("\n\n3) Potencia:")
    base = int(input("Base: "))
    exp = int(input("Exponente: "))
    print(f"{base}^{exp} = {potencia(base, exp)}")

    print("\n4) Decimal a binario:")
    n = int(input("Número decimal: "))
    binario = decimal_a_binario(n)
    print(f"Binario: {binario if binario else '0'}")

    print("\n5) Palíndromo:")
    palabra = input("Ingrese una palabra: ").lower()
    print("Es palíndromo:", es_palindromo(palabra))

    print("\n6) Suma de dígitos:")
    n = int(input("Número entero positivo: "))
    print("Suma de dígitos:", suma_digitos(n))

    print("\n7) Pirámide de bloques:")
    n = int(input("Bloques en el nivel más bajo: "))
    print("Total de bloques:", contar_bloques(n))

    print("\n8) Contar dígito:")
    numero = int(input("Número: "))
    digito = int(input("Dígito a contar: "))
    print(f"Aparece {contar_digito(numero, digito)} vez/veces")
