"""
========================================
🐒 Python para Monos
Módulo 3 — Actividad 22: Módulo CSV
========================================

📚 TEORÍA:

En la actividad anterior parseamos CSV manualmente con split(",""). Funciona,
pero tiene limitaciones: falla si un campo contiene comas, comillas o saltos
de línea dentro del texto.

Python incluye el módulo estándar 'csv' que maneja todos estos casos
correctamente. No necesitas instalarlo, ya viene con Python.

IMPORTAR:
    import csv

LECTURA CON csv.reader():
Devuelve cada fila como una LISTA de strings:

    import csv

    with open("datos.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            print(fila)
    # fila → ["Laptop Dell", "Tecnologia", "3", "2500000"]

Puedes separar los encabezados del resto:
    with open("datos.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        encabezados = next(lector)  # next() obtiene la primera fila
        print(f"Columnas: {encabezados}")
        for fila in lector:  # El resto son datos
            print(fila)

LECTURA CON csv.DictReader() ⭐ (LA MÁS ÚTIL):
Devuelve cada fila como un DICCIONARIO, usando la primera fila como claves:

    with open("datos.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for registro in lector:
            print(registro["nombre"], registro["precio"])

    # registro → {"nombre": "Laptop Dell", "categoria": "Tecnologia", ...}

    ¡Es mucho más legible! En lugar de fila[0], usas registro["nombre"].

ESCRITURA CON csv.writer():
    import csv

    datos = [
        ["nombre", "edad", "ciudad"],
        ["Ana", "28", "Bogotá"],
        ["Carlos", "35", "Medellín"],
    ]

    with open("salida.csv", "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        for fila in datos:
            escritor.writerow(fila)

    ⚠️ newline="" es necesario en Windows para evitar líneas en blanco extra.

ESCRITURA CON csv.DictWriter():
    import csv

    datos = [
        {"nombre": "Ana", "edad": 28},
        {"nombre": "Carlos", "edad": 35},
    ]

    with open("salida.csv", "w", encoding="utf-8", newline="") as archivo:
        campos = ["nombre", "edad"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()  # Escribe la fila de encabezados
        escritor.writerows(datos)  # Escribe todas las filas

DELIMITADOR PERSONALIZADO:
Algunos archivos usan ; en lugar de , (común en países donde la coma es
separador decimal):
    lector = csv.reader(archivo, delimiter=";")

📝 INSTRUCCIONES:

Crea un script que use el módulo csv para leer y escribir archivos:

1. Usa csv.reader() para leer 'datos/ventas.csv':
   - Extrae los encabezados con next().
   - Imprime cada fila como lista.

2. Usa csv.DictReader() para leer el mismo archivo:
   - Imprime cada registro como diccionario.
   - Accede a campos por nombre (ej: registro["nombre"]).

3. Crea una función 'leer_csv_como_diccionarios(ruta)' que:
   - Use csv.DictReader().
   - Devuelva una lista de diccionarios (los registros).
   - Maneje FileNotFoundError.

4. Crea una lista de 4 diccionarios con datos de ciudades:
   {"ciudad", "pais", "poblacion"} y escríbelos en un NUEVO archivo
   'datos/ciudades.csv' usando csv.DictWriter().

5. Lee el archivo que acabas de crear para verificar que se escribió bien.

✅ CRITERIOS DE ACEPTACIÓN:
- Se importa y usa el módulo csv (import csv).
- Se demuestra csv.reader() con next() para encabezados.
- Se demuestra csv.DictReader() para lectura con diccionarios.
- Se crea una función reutilizable de lectura.
- Se usa csv.DictWriter() para crear un nuevo CSV.
- Se usa newline="" y encoding="utf-8" al abrir archivos.
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# import csv
# import os
#
# ruta_script = os.path.dirname(os.path.abspath(__file__))
# ruta_ventas = os.path.join(ruta_script, "..", "datos", "ventas.csv")
# ruta_ciudades = os.path.join(ruta_script, "..", "datos", "ciudades.csv")
#
#
# def leer_csv_como_diccionarios(ruta):
#     """Lee un CSV y devuelve una lista de diccionarios."""
#     registros = []
#     try:
#         with open(ruta, "r", encoding="utf-8", newline="") as archivo:
#             lector = csv.DictReader(archivo)
#             for registro in lector:
#                 registros.append(dict(registro))
#     except FileNotFoundError:
#         print(f"❌ Error: No se encontró '{ruta}'")
#     return registros
#
#
# # 1. Lectura con csv.reader()
# print("=== LECTURA CON csv.reader() ===\n")
# try:
#     with open(ruta_ventas, "r", encoding="utf-8", newline="") as archivo:
#         lector = csv.reader(archivo)
#         encabezados = next(lector)
#         print(f"Encabezados: {encabezados}\n")
#         for fila in lector:
#             print(f"  {fila}")
# except FileNotFoundError:
#     print("❌ Archivo no encontrado")
#
#
# # 2. Lectura con csv.DictReader()
# print("\n\n=== LECTURA CON csv.DictReader() ===\n")
# try:
#     with open(ruta_ventas, "r", encoding="utf-8", newline="") as archivo:
#         lector = csv.DictReader(archivo)
#         for registro in lector:
#             print(f"  {registro['nombre']} | Categoría: {registro['categoria']} | Precio: ${registro['precio']}")
# except FileNotFoundError:
#     print("❌ Archivo no encontrado")
#
#
# # 3. Usando la función reutilizable
# print("\n\n=== FUNCIÓN REUTILIZABLE ===\n")
# datos = leer_csv_como_diccionarios(ruta_ventas)
# print(f"Total registros cargados: {len(datos)}")
# for d in datos[:3]:  # Mostrar solo los primeros 3
#     print(f"  → {d}")
#
#
# # 4. Escritura con csv.DictWriter()
# print("\n\n=== ESCRITURA CON csv.DictWriter() ===\n")
# ciudades = [
#     {"ciudad": "Bogotá", "pais": "Colombia", "poblacion": 7181469},
#     {"ciudad": "Ciudad de México", "pais": "México", "poblacion": 9209944},
#     {"ciudad": "Buenos Aires", "pais": "Argentina", "poblacion": 3075646},
#     {"ciudad": "Lima", "pais": "Perú", "poblacion": 9751717},
# ]
#
# campos = ["ciudad", "pais", "poblacion"]
# with open(ruta_ciudades, "w", encoding="utf-8", newline="") as archivo:
#     escritor = csv.DictWriter(archivo, fieldnames=campos)
#     escritor.writeheader()
#     escritor.writerows(ciudades)
#
# print(f"✅ Archivo '{ruta_ciudades}' creado exitosamente.")
#
#
# # 5. Verificar el archivo creado
# print("\n=== VERIFICACIÓN ===\n")
# ciudades_leidas = leer_csv_como_diccionarios(ruta_ciudades)
# for ciudad in ciudades_leidas:
#     print(f"  🌎 {ciudad['ciudad']}, {ciudad['pais']} — Población: {int(ciudad['poblacion']):,}")
