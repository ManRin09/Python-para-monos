"""
========================================
🐒 Python para Monos
Módulo 2 — Actividad 16: Lectura de Archivos de Texto
========================================

📚 TEORÍA:

Python puede LEER archivos que están guardados en tu computador. Esto es
fundamental porque en el mundo real, los datos no se escriben directamente
en el código; vienen de archivos externos (logs, reportes, configuraciones, etc.).

ABRIR UN ARCHIVO con open():
    archivo = open("ruta/al/archivo.txt", "r")
    # "r" = Read (lectura). Es el modo por defecto.

MODOS DE APERTURA:
    "r"  → Lectura (read). El archivo debe existir.
    "w"  → Escritura (write). Crea el archivo o BORRA su contenido si existe.
    "a"  → Agregar (append). Añade al final sin borrar.
    "r+" → Lectura y escritura.

MÉTODOS DE LECTURA:

    1. .read() — Lee TODO el contenido como un solo string:
        archivo = open("datos.txt", "r")
        contenido = archivo.read()
        print(contenido)
        archivo.close()

    2. .readline() — Lee UNA sola línea:
        archivo = open("datos.txt", "r")
        linea = archivo.readline()  # Primera línea
        print(linea)
        archivo.close()

    3. .readlines() — Lee TODAS las líneas y las devuelve como una LISTA:
        archivo = open("datos.txt", "r")
        lineas = archivo.readlines()
        # lineas = ["línea 1\\n", "línea 2\\n", "línea 3\\n"]
        archivo.close()

⚠️ SIEMPRE CERRAR EL ARCHIVO:
Cada vez que abres un archivo, debes cerrarlo con .close(). Si no lo haces,
el archivo queda "bloqueado" y puede causar problemas.

LA MEJOR PRÁCTICA — Bloque with:
El bloque 'with' abre el archivo y lo cierra AUTOMÁTICAMENTE al salir del bloque:

    with open("datos.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
    # Aquí el archivo ya está cerrado automáticamente ✅

LEER LÍNEA POR LÍNEA (la forma más eficiente):
    with open("datos.txt", "r") as archivo:
        for linea in archivo:
            print(linea.strip())  # .strip() elimina el \\n al final

    ¿Por qué .strip()? Cada línea del archivo termina con un salto de línea
    (\\n). Si no lo eliminas, print() agrega otro salto y queda doble espacio.

ENCODING (codificación):
Si el archivo tiene caracteres especiales (acentos, ñ), usa encoding:
    with open("datos.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

MANEJO DE ERRORES AL LEER:
    try:
        with open("archivo_inexistente.txt", "r") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print("El archivo no fue encontrado.")

📝 INSTRUCCIONES:

Crea un script que lea el archivo 'datos/notas.txt' (ya incluido en el
repositorio) y realice las siguientes operaciones:

1. Lee el archivo completo usando 'with open()' y muestra su contenido.

2. Lee el archivo LÍNEA POR LÍNEA usando un ciclo for e imprime cada línea
   sin el salto de línea extra (usa .strip()).

3. Cuenta cuántas líneas tiene el archivo en total.

4. Crea una función 'extraer_notas(ruta_archivo)' que:
   - Lea el archivo línea por línea.
   - De cada línea que contenga "Nota:", extraiga el número (usando split).
   - Devuelva una lista con todas las notas como números (int o float).

5. Con la lista de notas devuelta, calcula e imprime:
   - La cantidad de notas.
   - El promedio.
   - La nota más alta y la más baja.

NOTA: Usa una ruta relativa como '../datos/notas.txt' o la que corresponda
según desde dónde ejecutes el script.

✅ CRITERIOS DE ACEPTACIÓN:
- Se usa 'with open()' para abrir el archivo (no open/close manual).
- Se usa encoding="utf-8".
- Se lee línea por línea con un ciclo for.
- Se usa .strip() para limpiar los saltos de línea.
- Se crea una función que extrae datos numéricos del archivo.
- Se maneja el caso de FileNotFoundError con try/except.
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
# # Construir ruta al archivo de datos
# ruta_script = os.path.dirname(os.path.abspath(__file__))
# ruta_archivo = os.path.join(ruta_script, "..", "datos", "notas.txt")
#
#
# def extraer_notas(ruta):
#     """Lee el archivo y extrae las notas numéricas."""
#     notas = []
#     try:
#         with open(ruta, "r", encoding="utf-8") as archivo:
#             for linea in archivo:
#                 linea_limpia = linea.strip()
#                 if "Nota:" in linea_limpia:
#                     # Formato: "Estudiante: Nombre | Nota: 85"
#                     partes = linea_limpia.split("Nota:")
#                     if len(partes) > 1:
#                         nota_texto = partes[1].strip()
#                         notas.append(int(nota_texto))
#     except FileNotFoundError:
#         print(f"❌ Error: No se encontró el archivo '{ruta}'")
#     return notas
#
#
# # 1. Leer contenido completo
# print("=== CONTENIDO COMPLETO ===\n")
# try:
#     with open(ruta_archivo, "r", encoding="utf-8") as archivo:
#         contenido = archivo.read()
#         print(contenido)
# except FileNotFoundError:
#     print(f"❌ Error: No se encontró el archivo")
#
#
# # 2. Leer línea por línea
# print("\n=== LÍNEA POR LÍNEA ===\n")
# try:
#     contador_lineas = 0
#     with open(ruta_archivo, "r", encoding="utf-8") as archivo:
#         for linea in archivo:
#             contador_lineas += 1
#             print(f"Línea {contador_lineas}: {linea.strip()}")
# except FileNotFoundError:
#     print("❌ Archivo no encontrado")
#
#
# # 3. Total de líneas
# print(f"\n📄 Total de líneas: {contador_lineas}")
#
#
# # 4 y 5. Extraer notas y calcular estadísticas
# notas = extraer_notas(ruta_archivo)
#
# if len(notas) > 0:
#     print(f"\n=== ESTADÍSTICAS DE NOTAS ===")
#     print(f"📊 Notas extraídas: {notas}")
#     print(f"📋 Cantidad: {len(notas)}")
#
#     suma = 0
#     mayor = notas[0]
#     menor = notas[0]
#     for nota in notas:
#         suma += nota
#         if nota > mayor:
#             mayor = nota
#         if nota < menor:
#             menor = nota
#
#     promedio = suma / len(notas)
#     print(f"📈 Promedio: {promedio:.2f}")
#     print(f"🏆 Nota más alta: {mayor}")
#     print(f"📉 Nota más baja: {menor}")
