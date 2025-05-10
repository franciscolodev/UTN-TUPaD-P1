# TP5 Listas - Francisco López 
#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
multiplos_4 = list (range(4, 101, 4)) # Crea la lista
print("Multiplos de 4, del 1 al 100:", multiplos_4) #Imprime en pantala de la lista de multiplos de 4


#2) Crear una lista con cinco elementos y mostrar el penúltimo
gustos = ["programacion", "música", "deportes", "peliculas", "viajes"]
print("El penultimo gusto es:", gustos[-2])


#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla
lista_vacia = []
lista_vacia.append("programacion") #Agrega la palabra programacion
lista_vacia.append("peliculas") #Agrega la palabra peliculas
lista_vacia.append("música") #Agrega la palabra música
print("Lista resultante:", lista_vacia)


#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla.
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro" #Reemplaza el segundo valor (gato)
animales[-1] = "oso" #Reemplaza el cuarto (pez)
print("Lista modificada:", animales)


#5) Respuesta:
# El programa crea una lista con varios numeros y luego elimina el valor más alto de la lista (max=22)

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
numeros = list(range(10, 31, 5))
print("Los dos primeros números son:", numeros[0:2]) #Imprime los dos primeros números de la lista


#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
autos = ["Toyota", "Ford", "Chevrolet", "Honda"]
autos[1:3] = ["Nissan", "Kia"]  # Reemplaza los valores en los índices 1 y 2
print("Lista de autos modificada:", autos) 


#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.
dobles = []
dobles.append(5*2) #Agrega el doble de 5
dobles.append(10*2) #El doble de 10
dobles.append(15*2) #El doble de 15
print("Lista de dobles:", dobles)


#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo") #a
compras[1][1] = "tallarines" #b
compras[0].remove("pan") #c
print("Lista de compras actualizada:", compras) #d


#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 15, true, 25.5, 57.9, 30.6 y False. Imprimir la lista resultante por pantalla.
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("Lista anidada:", lista_anidada)