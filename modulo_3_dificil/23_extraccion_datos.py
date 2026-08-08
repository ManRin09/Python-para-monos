"""
========================================
🐒 Python para Monos
Módulo 3 — Actividad 23: Extracción de Datos
========================================

📚 TEORÍA:

EXTRACCIÓN DE DATOS es el proceso de leer una fuente de datos (como un CSV)
y quedarse SOLO con las columnas o campos que te interesan, descartando el
resto. Es el primer paso del proceso ETL (Extract, Transform, Load) que se
usa profesionalmente en ciencia de datos e ingeniería de datos.

¿POR QUÉ EXTRAER COLUMNAS ESPECÍFICAS?
- Los archivos de datos a menudo tienen muchas más columnas de las que necesitas.
- Reducir los datos a solo lo necesario hace que el procesamiento sea más
  rápido y el código más limpio.
- Preparas los datos para un paso posterior (cálculos, reportes, etc.).

EJEMPLO — Extraer columnas específicas:
Supón que tienes un CSV con 10 columnas pero solo necesitas "nombre" y "precio":

    import csv

    datos_filtrados = []
    with open("datos.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for registro in lector:
            nuevo = {
                "nombre": registro["nombre"],
                "precio": registro["precio"]
            }
            datos_filtrados.append(nuevo)

FUNCIÓN GENÉRICA DE EXTRACCIÓN:
Puedes crear una función que reciba las columnas que quieres extraer:

    def extraer_columnas(registros, columnas):
        \"\"\"Extrae solo las columnas especificadas de cada registro.\"\"\"
        resultado = []
        for registro in registros:
            nuevo = {}
            for col in columnas:
                nuevo[col] = registro.get(col, "")
            resultado.append(nuevo)
        return resultado

    # Uso:
    filtrados = extraer_columnas(datos, ["nombre", "precio"])

GUARDAR DATOS EXTRAÍDOS EN UN NUEVO CSV:
Después de extraer, es común guardar el resultado en un archivo nuevo:

    import csv

    def guardar_csv(registros, ruta, columnas):
        with open(ruta, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(registros)

📝 INSTRUCCIONES:

Crea un script que lea 'datos/ventas.csv' y extraiga solo columnas específicas:

1. Crea una función 'leer_csv(ruta)' que devuelva una lista de diccionarios
   usando csv.DictReader.

2. Crea una función 'extraer_columnas(registros, columnas)' que:
   - Reciba una lista de diccionarios y una lista de nombres de columnas.
   - Devuelva una NUEVA lista de diccionarios con SOLO esas columnas.
   - Si una columna no existe en un registro, use "" como valor por defecto.

3. Crea una función 'guardar_csv(registros, ruta, columnas)' que:
   - Reciba registros, ruta de salida y lista de columnas.
   - Escriba los registros en un nuevo CSV.

4. En la sección principal:
   a) Lee 'datos/ventas.csv' completo.
   b) Extrae solo las columnas "nombre" y "precio".
   c) Imprime los datos extraídos en consola.
   d) Guarda los datos extraídos en 'datos/ventas_filtrado.csv'.
   e) Lee el archivo filtrado y muéstralo para verificar.

✅ CRITERIOS DE ACEPTACIÓN:
- Se usa csv.DictReader para la lectura.
- Se crea una función genérica de extracción que acepta cualquier lista de columnas.
- Se crea una función de guardado con csv.DictWriter.
- Se genera un nuevo archivo CSV con solo las columnas extraídas.
- Se verifica el archivo generado leyéndolo nuevamente.
- Cada función es independiente y reutilizable.
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
# ruta_entrada = os.path.join(ruta_script, "..", "datos", "ventas.csv")
# ruta_salida = os.path.join(ruta_script, "..", "datos", "ventas_filtrado.csv")
#
#
# def leer_csv(ruta):
#     """Lee un archivo CSV y devuelve una lista de diccionarios."""
#     registros = []
#     try:
#         with open(ruta, "r", encoding="utf-8", newline="") as archivo:
#             lector = csv.DictReader(archivo)
#             for registro in lector:
#                 registros.append(dict(registro))
#     except FileNotFoundError:
#         print(f"❌ Error: Archivo '{ruta}' no encontrado.")
#     return registros
#
#
# def extraer_columnas(registros, columnas):
#     """Extrae solo las columnas especificadas de cada registro."""
#     resultado = []
#     for registro in registros:
#         nuevo = {}
#         for col in columnas:
#             nuevo[col] = registro.get(col, "")
#         resultado.append(nuevo)
#     return resultado
#
#
# def guardar_csv(registros, ruta, columnas):
#     """Guarda una lista de diccionarios en un archivo CSV."""
#     with open(ruta, "w", encoding="utf-8", newline="") as archivo:
#         escritor = csv.DictWriter(archivo, fieldnames=columnas)
#         escritor.writeheader()
#         escritor.writerows(registros)
#     print(f"✅ Archivo guardado en: {ruta}")
#
#
# # --- Sección principal ---
#
# # a) Leer CSV completo
# print("=== DATOS COMPLETOS ===\n")
# datos_completos = leer_csv(ruta_entrada)
# for reg in datos_completos:
#     print(f"  {reg}")
#
# # b) Extraer solo nombre y precio
# columnas_deseadas = ["nombre", "precio"]
# datos_filtrados = extraer_columnas(datos_completos, columnas_deseadas)
#
# # c) Imprimir datos extraídos
# print(f"\n=== DATOS FILTRADOS (solo {columnas_deseadas}) ===\n")
# for reg in datos_filtrados:
#     print(f"  {reg['nombre']}: ${reg['precio']}")
#
# # d) Guardar en nuevo CSV
# print()
# guardar_csv(datos_filtrados, ruta_salida, columnas_deseadas)
#
# # e) Verificar archivo generado
# print(f"\n=== VERIFICACIÓN DEL ARCHIVO GENERADO ===\n")
# verificacion = leer_csv(ruta_salida)
# for reg in verificacion:
#     print(f"  ✅ {reg}")
#
# print(f"\n📊 Registros originales: {len(datos_completos)} | Filtrados: {len(datos_filtrados)}")
