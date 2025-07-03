#TP: Estructuras de datos complejas - Francisco López - Programación I (UTN)

#1. Añadir frutas al diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#2. Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#3. Lista de frutas sin precios
frutas = list(precios_frutas.keys())
print("Frutas:", frutas)

#4. Agenda de contactos
agenda = {}
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = numero

busqueda = input("Ingresá el nombre del contacto a buscar: ")
if busqueda in agenda:
    print(f"El número de {busqueda} es {agenda[busqueda]}")
else:
    print("Contacto no encontrado.")

#5. Frase y conteo de palabras
frase = input("Ingresá una frase: ")
palabras = frase.split()

palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1
print("Conteo de palabras:", conteo)

#6. Alumnos y promedio
alumnos = {}
for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Ingresá nota {i+1} para {nombre}: ")) for i in range(3))
    alumnos[nombre] = notas

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: Promedio = {promedio:.2f}")

#7. Sets de estudiantes
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

#8. Inventario de productos
stock = {}
producto = input("Ingresá el nombre del producto a consultar: ")

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto no encontrado. ¿Cuántas unidades querés agregar?: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

#9. Agenda con tuplas
agenda_eventos = {
    ('Lunes', '10:00'): 'Reunión de equipo',
    ('Martes', '14:00'): 'Clase de Python'
}

dia = input("Ingresá el día: ")
hora = input("Ingresá la hora: ")
actividad = agenda_eventos.get((dia, hora), "No hay actividad programada.")
print(f"Actividad para {dia} a las {hora}: {actividad}")

#10. Invertir diccionario país-capital
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago'
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Diccionario invertido:", capitales_paises)