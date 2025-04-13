#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

# Esta linea genera un número aleatorio entre 0 y 9
numero_aleatorio = random.randint(0, 9)

# Inicializa el contador de intentos y la variable para verificar si acertó
intentos = 0
adivinado = False  # Variable que controla si se ha adivinado el número

# Arranca el juego
print("Adivina el número entre 0 y 9")

# Este bucle segiurá pidiendo intentos hasta que el número sea adivinado
while not adivinado:
    intento = int(input("Ingresa tu intento: "))
    intentos += 1  # Aumentar el contador de intentos
    
    # Verificar el número ingresado 
    if intento == numero_aleatorio:
        adivinado = True  # Cambiar la variable a True cuando se adivine el número
        print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
    else:
        print("Intenta nuevamente.")