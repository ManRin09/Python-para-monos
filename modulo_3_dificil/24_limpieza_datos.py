"""
========================================
🐒 Python para Monos
Módulo 3 — Actividad 24: Limpieza de Datos
========================================

📚 TEORÍA:

Cuando lees datos de un archivo CSV (o cualquier fuente externa), TODOS los
valores llegan como STRINGS. Si un campo dice "2500000", Python lo ve como
el texto "2500000", NO como el número 2500000. No puedes hacer matemáticas
con texto.

LA LIMPIEZA DE DATOS (Data Cleaning) consiste en:
1. Convertir tipos de datos (str → int, str → float).
2. Manejar valores vacíos o nulos.
3. Eliminar espacios sobrantes.
4. Estandarizar formatos (ej: fechas, nombres).

CONVERSIÓN DE TIPOS:

    # String a entero
    cantidad = int("5")          →  5
    cantidad = int("cinco")      →  ❌ ValueError

    # String a flotante
    precio = float("2500.50")    →  2500.5
    precio = float("2,500.50")   →  ❌ ValueError (las comas fallan)

    # Para manejar comas como separador de miles:
    precio = float("2,500.50".replace(",", ""))  →  2500.5

CONVERSIÓN SEGURA (siempre usar try/except):

    def a_float(valor):
        try:
            limpio = str(valor).strip().replace(",", "")
            return float(limpio)
        except (ValueError, TypeError):
            return 0.0

    def a_int(valor):
        try:
            return int(float(str(valor).strip()))
        except (ValueError, TypeError):
            return 0

MANEJAR VALORES VACÍOS:
    Cuando un campo está vacío en el CSV, llega como "" (string vacío):

    def limpiar_campo(valor, tipo="str", default=None):
        \"\"\"Limpia un campo según su tipo esperado.\"\"\"
        if valor is None or str(valor).strip() == "":
            return default

        valor_limpio = str(valor).strip()

        if tipo == "float":
            return a_float(valor_limpio)
        elif tipo == "int":
            return a_int(valor_limpio)
        else:
            return valor_limpio

PIPELINE DE LIMPIEZA COMPLETO:
El patrón es: leer datos crudos → limpiar cada registro → devolver datos limpios:

    def limpiar_registros(registros_crudos):
        limpios = []
        errores = []
        for i, reg in enumerate(registros_crudos):
            try:
                limpio = {
                    "nombre": reg["nombre"].strip().title(),
                    "cantidad": int(reg["cantidad"]),
                    "precio": float(reg["precio"]),
                }
                limpios.append(limpio)
            except (ValueError, KeyError) as e:
                errores.append(f"Fila {i+1}: {e}")
        return limpios, errores

📝 INSTRUCCIONES:

Crea un script que limpie datos extraídos de 'datos/ventas.csv':

1. Lee el CSV usando csv.DictReader.

2. Crea las siguientes funciones de limpieza:
   a) 'a_float(valor)' → Convierte a float de forma segura. Retorna 0.0 si falla.
   b) 'a_int(valor)' → Convierte a int de forma segura. Retorna 0 si falla.
   c) 'limpiar_texto(valor)' → Strip + Title. Retorna "" si es None o vacío.

3. Crea una función 'limpiar_registro_venta(registro)' que:
   - Reciba un diccionario crudo (con todos los valores como strings).
   - Devuelva un nuevo diccionario con los tipos correctos:
     "nombre" → string limpio (Title Case)
     "categoria" → string limpio (Title Case)
     "cantidad" → int
     "precio" → float

4. Crea una función 'limpiar_todos(registros_crudos)' que:
   - Recorra todos los registros.
   - Limpie cada uno con limpiar_registro_venta().
   - Devuelva la lista de registros limpios.
   - Lleve un conteo de cuántos se limpiaron exitosamente y cuántos fallaron.

5. Muestra los registros antes y después de la limpieza para ver la diferencia.

6. Con los datos limpios, calcula el valor total del inventario:
   (cantidad * precio) para cada producto y la suma de todos.

✅ CRITERIOS DE ACEPTACIÓN:
- Se crean funciones de conversión segura (a_float, a_int, limpiar_texto).
- Las funciones usan try/except para manejar errores de conversión.
- Se demuestra la transformación de str → int y str → float.
- Los datos limpios tienen los tipos correctos (verificable con type()).
- Se calcula el valor del inventario con los datos ya convertidos.
- Se muestra un "antes y después" de la limpieza.
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
# # --- Funciones de limpieza ---
#
# def a_float(valor):
#     """Convierte un valor a float de forma segura."""
#     try:
#         limpio = str(valor).strip().replace(",", "")
#         return float(limpio)
#     except (ValueError, TypeError):
#         return 0.0
#
#
# def a_int(valor):
#     """Convierte un valor a int de forma segura."""
#     try:
#         return int(float(str(valor).strip()))
#     except (ValueError, TypeError):
#         return 0
#
#
# def limpiar_texto(valor):
#     """Limpia un texto: strip + title. Retorna '' si es vacío."""
#     if valor is None or str(valor).strip() == "":
#         return ""
#     return str(valor).strip().title()
#
#
# def limpiar_registro_venta(registro):
#     """Limpia un registro de venta individual."""
#     return {
#         "nombre": limpiar_texto(registro.get("nombre", "")),
#         "categoria": limpiar_texto(registro.get("categoria", "")),
#         "cantidad": a_int(registro.get("cantidad", "0")),
#         "precio": a_float(registro.get("precio", "0")),
#     }
#
#
# def limpiar_todos(registros_crudos):
#     """Limpia todos los registros y cuenta éxitos/fallos."""
#     limpios = []
#     exitosos = 0
#     fallidos = 0
#
#     for reg in registros_crudos:
#         try:
#             limpio = limpiar_registro_venta(reg)
#             limpios.append(limpio)
#             exitosos += 1
#         except Exception as e:
#             print(f"  ⚠️ Error limpiando registro: {e}")
#             fallidos += 1
#
#     print(f"\n📊 Resultados: {exitosos} exitosos, {fallidos} fallidos")
#     return limpios
#
#
# # --- Sección principal ---
#
# # Leer datos crudos
# datos_crudos = []
# with open(ruta_csv, "r", encoding="utf-8", newline="") as archivo:
#     lector = csv.DictReader(archivo)
#     for registro in lector:
#         datos_crudos.append(dict(registro))
#
# # Mostrar ANTES de limpiar
# print("=== ANTES DE LIMPIAR (datos crudos) ===\n")
# for reg in datos_crudos[:3]:
#     print(f"  {reg}")
#     for clave, valor in reg.items():
#         print(f"    {clave}: '{valor}' → tipo: {type(valor).__name__}")
#     print()
#
# # Limpiar
# print("=== LIMPIANDO... ===")
# datos_limpios = limpiar_todos(datos_crudos)
#
# # Mostrar DESPUÉS de limpiar
# print("\n=== DESPUÉS DE LIMPIAR ===\n")
# for reg in datos_limpios[:3]:
#     print(f"  {reg}")
#     for clave, valor in reg.items():
#         print(f"    {clave}: {valor} → tipo: {type(valor).__name__}")
#     print()
#
# # Calcular valor del inventario
# print("=== VALOR DEL INVENTARIO ===\n")
# valor_total = 0
# for reg in datos_limpios:
#     valor_item = reg["cantidad"] * reg["precio"]
#     valor_total += valor_item
#     print(f"  {reg['nombre']:<25} {reg['cantidad']:>3} x ${reg['precio']:>12,.2f} = ${valor_item:>14,.2f}")
#
# print(f"\n{'VALOR TOTAL INVENTARIO:':<30} ${valor_total:>14,.2f}")
