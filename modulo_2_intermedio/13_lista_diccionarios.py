"""
========================================
🐒 Python para Monos
Módulo 2 — Actividad 13: Lista de Diccionarios
========================================

📚 TEORÍA:

En el mundo real, los datos rara vez son simples. Frecuentemente necesitas
manejar COLECCIONES de registros, donde cada registro tiene múltiples campos.
La estructura perfecta para esto es una LISTA DE DICCIONARIOS.

Cada diccionario representa un "registro" o "fila" de datos, y la lista
los agrupa todos juntos.

EJEMPLO:
    empleados = [
        {"nombre": "Ana", "cargo": "Desarrolladora", "salario": 3500000},
        {"nombre": "Carlos", "cargo": "Diseñador", "salario": 2800000},
        {"nombre": "María", "cargo": "Gerente", "salario": 5200000},
    ]

ACCEDER A UN REGISTRO:
    empleados[0]             →  {"nombre": "Ana", "cargo": "Desarrolladora", ...}
    empleados[0]["nombre"]   →  "Ana"
    empleados[1]["salario"]  →  2800000

ITERAR SOBRE LA LISTA:
    for empleado in empleados:
        print(f"{empleado['nombre']} - {empleado['cargo']}")

    Salida:
    Ana - Desarrolladora
    Carlos - Diseñador
    María - Gerente

AGREGAR UN NUEVO REGISTRO:
    nuevo = {"nombre": "Pedro", "cargo": "Analista", "salario": 3000000}
    empleados.append(nuevo)

FILTRAR REGISTROS:
    # Encontrar empleados con salario mayor a 3 millones
    bien_pagados = []
    for empleado in empleados:
        if empleado["salario"] > 3000000:
            bien_pagados.append(empleado)

BUSCAR UN REGISTRO ESPECÍFICO:
    def buscar_por_nombre(lista, nombre_buscado):
        for registro in lista:
            if registro["nombre"] == nombre_buscado:
                return registro
        return None  # No encontrado

    resultado = buscar_por_nombre(empleados, "Ana")
    if resultado:
        print(f"Encontrado: {resultado}")
    else:
        print("No encontrado")

MODIFICAR UN REGISTRO:
    for empleado in empleados:
        if empleado["nombre"] == "Carlos":
            empleado["salario"] = 3200000  # Aumento de salario

ESTE PATRÓN ES FUNDAMENTAL:
Esta estructura (lista de diccionarios) es la base de cómo se manejan datos
en programación. Los archivos CSV, las bases de datos y las APIs JSON producen
datos que se representan exactamente así en Python.

📝 INSTRUCCIONES:

Crea un script que administre un inventario de libros usando una lista de
diccionarios:

1. Crea una lista llamada 'biblioteca' con al menos 5 libros. Cada libro debe
   ser un diccionario con las claves: "titulo", "autor", "anio", "paginas", "leido"
   (leido es un bool: True/False).

2. Imprime un encabezado "=== BIBLIOTECA ===" y luego TODOS los libros con un
   formato bonito usando un ciclo for:
   "📖 [titulo] — [autor] ([anio]) | [paginas] págs. | [Leído ✅ / Pendiente ⏳]"

3. Crea una función 'filtrar_leidos(lista_libros)' que reciba la lista y
   devuelva una NUEVA lista solo con los libros que tienen leido=True.

4. Crea una función 'buscar_por_autor(lista_libros, autor)' que devuelva una
   lista con todos los libros de un autor específico.

5. Calcula e imprime el PROMEDIO de páginas de todos los libros.

6. Encuentra e imprime cuál es el libro con más páginas.

✅ CRITERIOS DE ACEPTACIÓN:
- La lista contiene al menos 5 diccionarios, cada uno con 5 claves.
- Se itera la lista completa para imprimir todos los libros formateados.
- Se crea una función que filtra libros leídos y devuelve una nueva lista.
- Se crea una función que busca por autor y devuelve resultados.
- Se calcula el promedio de páginas con un acumulador (no sum()).
- Se encuentra el libro con más páginas usando comparación iterativa.
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# # 1. Crear la biblioteca
# biblioteca = [
#     {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez", "anio": 1967, "paginas": 417, "leido": True},
#     {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "anio": 1943, "paginas": 96, "leido": True},
#     {"titulo": "1984", "autor": "George Orwell", "anio": 1949, "paginas": 328, "leido": False},
#     {"titulo": "Don Quijote", "autor": "Miguel de Cervantes", "anio": 1605, "paginas": 863, "leido": False},
#     {"titulo": "El Amor en los Tiempos del Cólera", "autor": "Gabriel García Márquez", "anio": 1985, "paginas": 348, "leido": True},
# ]
#
#
# # 2. Imprimir todos los libros
# print("=== BIBLIOTECA ===\n")
# for libro in biblioteca:
#     estado = "Leído ✅" if libro["leido"] else "Pendiente ⏳"
#     print(f"📖 {libro['titulo']} — {libro['autor']} ({libro['anio']}) | {libro['paginas']} págs. | {estado}")
#
#
# # 3. Función filtrar leídos
# def filtrar_leidos(lista_libros):
#     leidos = []
#     for libro in lista_libros:
#         if libro["leido"]:
#             leidos.append(libro)
#     return leidos
#
#
# # 4. Función buscar por autor
# def buscar_por_autor(lista_libros, autor):
#     resultados = []
#     for libro in lista_libros:
#         if libro["autor"].lower() == autor.lower():
#             resultados.append(libro)
#     return resultados
#
#
# # Probar funciones
# print("\n=== LIBROS LEÍDOS ===")
# leidos = filtrar_leidos(biblioteca)
# for libro in leidos:
#     print(f"  ✅ {libro['titulo']}")
#
# print("\n=== BÚSQUEDA POR AUTOR ===")
# autor_buscar = "Gabriel García Márquez"
# resultados = buscar_por_autor(biblioteca, autor_buscar)
# print(f"Libros de {autor_buscar}:")
# for libro in resultados:
#     print(f"  📖 {libro['titulo']} ({libro['anio']})")
#
#
# # 5. Promedio de páginas
# total_paginas = 0
# for libro in biblioteca:
#     total_paginas += libro["paginas"]
# promedio = total_paginas / len(biblioteca)
# print(f"\n📊 Promedio de páginas: {promedio:.1f}")
#
#
# # 6. Libro con más páginas
# libro_mayor = biblioteca[0]
# for libro in biblioteca:
#     if libro["paginas"] > libro_mayor["paginas"]:
#         libro_mayor = libro
# print(f"📚 Libro con más páginas: '{libro_mayor['titulo']}' ({libro_mayor['paginas']} págs.)")
