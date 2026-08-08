"""
========================================
🐒 Python para Monos
Módulo 3 — Actividad 21: Lectura CSV Básica (Manual)
========================================

📚 TEORÍA:

Un archivo CSV (Comma-Separated Values = Valores Separados por Comas) es uno
de los formatos más usados para almacenar datos tabulares en texto plano.
Cada línea es un registro y los campos se separan por comas.

EJEMPLO de archivo CSV (ventas.csv):
    nombre,categoria,cantidad,precio
    Laptop Dell,Tecnologia,3,2500000
    Mouse Logitech,Tecnologia,10,85000
    Silla Ergonomica,Oficina,5,450000

La PRIMERA LÍNEA generalmente contiene los ENCABEZADOS (nombres de columnas).
Las siguientes líneas contienen los DATOS.

PARSEO MANUAL (sin usar la librería csv):
Parsear significa "analizar y descomponer" un texto para extraer datos
estructurados. Podemos hacerlo manualmente con los métodos que ya conocemos:

    1. Abrir el archivo con open()
    2. Leer línea por línea
    3. Usar .strip() para limpiar saltos de línea
    4. Usar .split(',') para separar los campos

EJEMPLO COMPLETO:
    with open("datos.csv", "r", encoding="utf-8") as archivo:
        encabezados = archivo.readline().strip().split(",")
        print(f"Columnas: {encabezados}")

        for linea in archivo:
            campos = linea.strip().split(",")
            print(campos)

    # encabezados → ["nombre", "categoria", "cantidad", "precio"]
    # campos      → ["Laptop Dell", "Tecnologia", "3", "2500000"]

⚠️ IMPORTANTE:
- Todos los valores extraídos con split() son STRINGS, incluso los números.
  Si necesitas hacer matemáticas, debes convertirlos: int("3") o float("2500000")

- El parseo manual FALLA si un campo contiene una coma dentro del texto:
  'Laptop Dell, 14"' se partiría incorrectamente.
  Para esos casos, usaremos la librería csv en la siguiente actividad.

CONVERTIR A LISTA DE DICCIONARIOS:
El patrón más útil es convertir las filas a diccionarios usando los encabezados:

    registros = []
    with open("datos.csv", "r", encoding="utf-8") as archivo:
        encabezados = archivo.readline().strip().split(",")
        for linea in archivo:
            valores = linea.strip().split(",")
            registro = {}
            for i in range(len(encabezados)):
                registro[encabezados[i]] = valores[i]
            registros.append(registro)

    # registros[0] → {"nombre": "Laptop Dell", "categoria": "Tecnologia", ...}

📝 INSTRUCCIONES:

Crea un script que lea el archivo 'datos/ventas.csv' de forma manual:

1. Abre el archivo usando 'with open()' con encoding="utf-8".

2. Lee la primera línea como encabezados, límpiala y sepárala con split(",").
   Imprime las columnas encontradas.

3. Lee el resto de líneas una por una, sepáralas con split(",") y guárdalas
   como una lista de listas.
   Imprime cada fila con un formato legible.

4. Crea una función 'csv_a_diccionarios(ruta_archivo)' que:
   - Abra el CSV.
   - Lea los encabezados.
   - Convierta cada fila en un diccionario (clave = encabezado, valor = dato).
   - Devuelva una lista de diccionarios.

5. Usa la función para cargar los datos e imprime cada registro.

6. Cuenta e imprime cuántos registros se leyeron.

✅ CRITERIOS DE ACEPTACIÓN:
- Se usa open() con encoding="utf-8" (no la librería csv).
- Se usa .strip() y .split(",") para parsear las líneas.
- Los encabezados se extraen de la primera línea.
- Se crea una función que devuelve una lista de diccionarios.
- Se maneja FileNotFoundError con try/except.
- Se imprime el total de registros leídos.
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# import os
#
# ruta_script = os.path.dirname(os.path.abspath(__file__))
# ruta_csv = os.path.join(ruta_script, "..", "datos", "ventas.csv")
#
#
# def csv_a_diccionarios(ruta_archivo):
#     """Lee un CSV manualmente y devuelve una lista de diccionarios."""
#     registros = []
#     try:
#         with open(ruta_archivo, "r", encoding="utf-8") as archivo:
#             # Leer encabezados
#             primera_linea = archivo.readline().strip()
#             encabezados = primera_linea.split(",")
#
#             # Leer datos
#             for linea in archivo:
#                 linea_limpia = linea.strip()
#                 if linea_limpia == "":
#                     continue  # Saltar líneas vacías
#                 valores = linea_limpia.split(",")
#                 registro = {}
#                 for i in range(len(encabezados)):
#                     registro[encabezados[i]] = valores[i]
#                 registros.append(registro)
#
#     except FileNotFoundError:
#         print(f"❌ Error: No se encontró el archivo '{ruta_archivo}'")
#
#     return registros
#
#
# # --- Sección principal ---
#
# # 1-3. Lectura manual básica
# print("=== LECTURA MANUAL DEL CSV ===\n")
# try:
#     with open(ruta_csv, "r", encoding="utf-8") as archivo:
#         encabezados = archivo.readline().strip().split(",")
#         print(f"📋 Columnas encontradas: {encabezados}\n")
#
#         filas = []
#         for linea in archivo:
#             campos = linea.strip().split(",")
#             filas.append(campos)
#             print(f"  Fila: {campos}")
#
#         print(f"\n📊 Total de filas de datos: {len(filas)}")
# except FileNotFoundError:
#     print("❌ Archivo no encontrado")
#
# # 4-6. Usando la función csv_a_diccionarios
# print("\n\n=== CONVERSIÓN A DICCIONARIOS ===\n")
# datos = csv_a_diccionarios(ruta_csv)
#
# for i, registro in enumerate(datos, start=1):
#     print(f"Registro #{i}:")
#     for clave, valor in registro.items():
#         print(f"  {clave}: {valor}")
#     print()
#
# print(f"📊 Total de registros leídos: {len(datos)}")
