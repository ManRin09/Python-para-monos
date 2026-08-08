"""
========================================
🐒 Python para Monos
Módulo 2 — Actividad 17: Escritura de Archivos de Texto
========================================

📚 TEORÍA:

Así como podemos LEER archivos, también podemos CREAR y ESCRIBIR archivos
nuevos desde Python. Esto es esencial para guardar resultados, generar
reportes, logs de ejecución, etc.

MODOS DE ESCRITURA:

    "w" (write) — ESCRIBE desde cero.
        - Si el archivo NO existe, lo CREA.
        - Si el archivo YA existe, BORRA todo su contenido y escribe encima.
        ⚠️ ¡Cuidado! Puedes perder datos si usas "w" sin querer.

    "a" (append) — AGREGA al final.
        - Si el archivo NO existe, lo CREA.
        - Si el archivo YA existe, AGREGA al final sin borrar nada.

ESCRIBIR CON write():
    with open("salida.txt", "w", encoding="utf-8") as archivo:
        archivo.write("Primera línea\\n")
        archivo.write("Segunda línea\\n")
        archivo.write("Tercera línea\\n")

    ⚠️ write() NO agrega saltos de línea automáticamente. Debes poner \\n tú.

ESCRIBIR MÚLTIPLES LÍNEAS con writelines():
    lineas = ["Línea 1\\n", "Línea 2\\n", "Línea 3\\n"]
    with open("salida.txt", "w", encoding="utf-8") as archivo:
        archivo.writelines(lineas)

    ⚠️ writelines() tampoco agrega \\n. Cada string debe incluirlo.

AGREGAR AL FINAL con modo "a":
    with open("log.txt", "a", encoding="utf-8") as archivo:
        archivo.write("Nueva entrada en el log\\n")
    # El contenido anterior se conserva, la nueva línea se agrega al final.

EJEMPLO PRÁCTICO — Guardar resultados:
    resultados = [85, 92, 78, 95, 88]
    with open("resultados.txt", "w", encoding="utf-8") as archivo:
        archivo.write("=== RESULTADOS ===\\n")
        for i, resultado in enumerate(resultados, start=1):
            archivo.write(f"Prueba {i}: {resultado} puntos\\n")
        promedio = sum(resultados) / len(resultados)
        archivo.write(f"\\nPromedio: {promedio:.2f}\\n")

COMBINACIÓN LEER + ESCRIBIR:
Un patrón común es leer un archivo, procesar los datos, y escribir los
resultados en un archivo nuevo:

    # Leer datos
    with open("entrada.txt", "r") as entrada:
        datos = entrada.readlines()

    # Procesar y escribir
    with open("salida.txt", "w") as salida:
        for linea in datos:
            salida.write(linea.upper())  # Guarda todo en mayúsculas

📝 INSTRUCCIONES:

Crea un script que genere un reporte de texto a partir de datos procesados:

1. Crea una lista de diccionarios con al menos 5 estudiantes, cada uno con:
   "nombre" y "notas" (lista de 3 notas numéricas).

2. Crea una función 'calcular_promedio(notas)' que devuelva el promedio.

3. Crea una función 'generar_reporte_txt(estudiantes, ruta_salida)' que:
   a) Abra (o cree) un archivo en la ruta indicada en modo escritura ("w").
   b) Escriba un encabezado: "=== REPORTE DE CALIFICACIONES ===\\n"
   c) Para cada estudiante, escriba una línea con:
      "Nombre: [nombre] | Notas: [n1, n2, n3] | Promedio: [promedio]\\n"
   d) Al final, escriba una línea separadora y el promedio general.
   e) Cierre el archivo automáticamente con 'with'.

4. Llama a la función para generar el archivo 'datos/reporte_notas.txt'.

5. Después de generarlo, lee el archivo recién creado y muéstralo en consola
   para verificar que se guardó correctamente.

✅ CRITERIOS DE ACEPTACIÓN:
- Se usa 'with open(ruta, "w", encoding="utf-8")' para escribir.
- Se usa write() para escribir cada línea (con \\n al final).
- Se genera un archivo .txt nuevo con el reporte.
- El archivo contiene encabezado, datos de cada estudiante y promedio general.
- Después de escribir, se lee el archivo y se muestra en consola.
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
# ruta_salida = os.path.join(ruta_script, "..", "datos", "reporte_notas.txt")
#
# # 1. Datos de estudiantes
# estudiantes = [
#     {"nombre": "Ana López", "notas": [85, 92, 78]},
#     {"nombre": "Carlos Méndez", "notas": [60, 55, 70]},
#     {"nombre": "María García", "notas": [95, 98, 92]},
#     {"nombre": "Juan Pérez", "notas": [70, 65, 80]},
#     {"nombre": "Sofía Herrera", "notas": [88, 91, 85]},
# ]
#
#
# # 2. Función promedio
# def calcular_promedio(notas):
#     suma = 0
#     for nota in notas:
#         suma += nota
#     return suma / len(notas)
#
#
# # 3. Función generar reporte
# def generar_reporte_txt(lista_estudiantes, ruta):
#     suma_promedios = 0
#
#     with open(ruta, "w", encoding="utf-8") as archivo:
#         archivo.write("=" * 55 + "\n")
#         archivo.write("  REPORTE DE CALIFICACIONES\n")
#         archivo.write("=" * 55 + "\n\n")
#
#         for est in lista_estudiantes:
#             promedio = calcular_promedio(est["notas"])
#             suma_promedios += promedio
#             archivo.write(f"Nombre: {est['nombre']} | Notas: {est['notas']} | Promedio: {promedio:.2f}\n")
#
#         promedio_general = suma_promedios / len(lista_estudiantes)
#         archivo.write("\n" + "-" * 55 + "\n")
#         archivo.write(f"Promedio general del grupo: {promedio_general:.2f}\n")
#         archivo.write("=" * 55 + "\n")
#
#     print(f"✅ Reporte generado exitosamente en: {ruta}")
#
#
# # 4. Generar el reporte
# generar_reporte_txt(estudiantes, ruta_salida)
#
# # 5. Leer y mostrar el archivo generado
# print("\n=== CONTENIDO DEL ARCHIVO GENERADO ===\n")
# with open(ruta_salida, "r", encoding="utf-8") as archivo:
#     print(archivo.read())
