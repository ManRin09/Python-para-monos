"""
========================================
🐒 Python para Monos
Módulo 3 — Actividad 25: Agrupación de Datos
========================================

📚 TEORÍA:

La AGRUPACIÓN DE DATOS es un algoritmo que toma una lista de registros y los
consolida (agrupa) según un campo en común, sumando o acumulando los valores
numéricos de los registros que comparten ese campo.

EJEMPLO DEL MUNDO REAL:
Tienes una lista de ventas donde el mismo producto aparece múltiples veces
en diferentes transacciones. Necesitas saber el TOTAL vendido por producto.

    ventas = [
        {"producto": "Laptop", "cantidad": 2},
        {"producto": "Mouse", "cantidad": 5},
        {"producto": "Laptop", "cantidad": 1},
        {"producto": "Mouse", "cantidad": 3},
        {"producto": "Teclado", "cantidad": 4},
    ]

    # Resultado esperado después de agrupar por "producto":
    # Laptop: 3 (2 + 1)
    # Mouse: 8 (5 + 3)
    # Teclado: 4

ALGORITMO DE AGRUPACIÓN con diccionario acumulador:

    El truco es usar un DICCIONARIO como acumulador. Las claves son los valores
    únicos del campo por el que agrupas, y los valores son las sumas acumuladas.

    agrupado = {}
    for venta in ventas:
        clave = venta["producto"]
        cantidad = venta["cantidad"]

        if clave in agrupado:
            agrupado[clave] += cantidad          # Si ya existe, suma
        else:
            agrupado[clave] = cantidad           # Si es nuevo, inicializa

    # agrupado → {"Laptop": 3, "Mouse": 8, "Teclado": 4}

AGRUPAR MÚLTIPLES CAMPOS:
Si necesitas acumular más de un valor numérico:

    agrupado = {}
    for venta in ventas:
        clave = venta["categoria"]
        if clave not in agrupado:
            agrupado[clave] = {"cantidad": 0, "total": 0}
        agrupado[clave]["cantidad"] += venta["cantidad"]
        agrupado[clave]["total"] += venta["cantidad"] * venta["precio"]

CONVERTIR RESULTADO A LISTA DE DICCIONARIOS:
Después de agrupar, es útil convertir el diccionario a lista para seguir
procesando:

    resultado = []
    for clave, valores in agrupado.items():
        registro = {"categoria": clave}
        registro.update(valores)  # Agrega las claves del sub-diccionario
        resultado.append(registro)

📝 INSTRUCCIONES:

Crea un script que agrupe datos del archivo 'datos/ventas.csv':

1. Lee el CSV y limpia los datos (convierte cantidad a int, precio a float).

2. Crea una función 'agrupar_por_categoria(registros)' que:
   - Reciba la lista de registros limpios.
   - Agrupe por la columna "categoria".
   - Para cada categoría, acumule:
     * La cantidad total de artículos.
     * El valor total (cantidad * precio de cada artículo).
     * La cantidad de productos distintos en esa categoría.
   - Devuelva un diccionario con los resultados agrupados.

3. Crea una función 'mostrar_resumen(agrupado)' que:
   - Imprima una tabla formateada con las categorías y sus totales.
   - Use ljust/rjust para alinear las columnas.

4. En la sección principal:
   a) Lee y limpia los datos.
   b) Agrupa por categoría.
   c) Muestra el resumen.
   d) Identifica la categoría con mayor valor total.

✅ CRITERIOS DE ACEPTACIÓN:
- Se usa un diccionario como acumulador para agrupar.
- Se agrupa por un campo específico ("categoria").
- Se acumulan al menos 2 valores numéricos por grupo.
- Se crea una función genérica de agrupación.
- Se muestra el resultado en formato de tabla.
- Se identifica el grupo con mayor valor.
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
# ruta_csv = os.path.join(ruta_script, "..", "datos", "ventas.csv")
#
#
# def leer_y_limpiar(ruta):
#     """Lee el CSV y convierte los tipos de datos."""
#     registros = []
#     with open(ruta, "r", encoding="utf-8", newline="") as archivo:
#         lector = csv.DictReader(archivo)
#         for reg in lector:
#             limpio = {
#                 "nombre": reg["nombre"].strip(),
#                 "categoria": reg["categoria"].strip(),
#                 "cantidad": int(reg["cantidad"].strip()),
#                 "precio": float(reg["precio"].strip()),
#             }
#             registros.append(limpio)
#     return registros
#
#
# def agrupar_por_categoria(registros):
#     """Agrupa registros por categoría, acumulando cantidad y valor."""
#     agrupado = {}
#     for reg in registros:
#         cat = reg["categoria"]
#         valor = reg["cantidad"] * reg["precio"]
#
#         if cat not in agrupado:
#             agrupado[cat] = {
#                 "cantidad_total": 0,
#                 "valor_total": 0,
#                 "num_productos": 0
#             }
#
#         agrupado[cat]["cantidad_total"] += reg["cantidad"]
#         agrupado[cat]["valor_total"] += valor
#         agrupado[cat]["num_productos"] += 1
#
#     return agrupado
#
#
# def mostrar_resumen(agrupado):
#     """Muestra los datos agrupados en formato de tabla."""
#     AC = 18  # Ancho categoría
#     AP = 12  # Ancho productos
#     AQ = 12  # Ancho cantidad
#     AV = 18  # Ancho valor
#
#     print("CATEGORÍA".ljust(AC) + "PRODUCTOS".rjust(AP) + "CANTIDAD".rjust(AQ) + "VALOR TOTAL".rjust(AV))
#     print("=" * (AC + AP + AQ + AV))
#
#     for cat, datos in agrupado.items():
#         valor_fmt = f"${datos['valor_total']:,.2f}"
#         print(
#             cat.ljust(AC)
#             + str(datos["num_productos"]).rjust(AP)
#             + str(datos["cantidad_total"]).rjust(AQ)
#             + valor_fmt.rjust(AV)
#         )
#
#
# # --- Sección principal ---
# print("=== AGRUPACIÓN DE DATOS POR CATEGORÍA ===\n")
#
# # a) Leer y limpiar
# datos = leer_y_limpiar(ruta_csv)
# print(f"Registros leídos: {len(datos)}\n")
#
# # b) Agrupar
# resumen = agrupar_por_categoria(datos)
#
# # c) Mostrar
# mostrar_resumen(resumen)
#
# # d) Categoría con mayor valor
# cat_mayor = ""
# valor_mayor = 0
# for cat, datos in resumen.items():
#     if datos["valor_total"] > valor_mayor:
#         valor_mayor = datos["valor_total"]
#         cat_mayor = cat
#
# print(f"\n🏆 Categoría con mayor valor: {cat_mayor} (${valor_mayor:,.2f})")
