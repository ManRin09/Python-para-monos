"""
========================================
🐒 Python para Monos
Módulo 2 — Actividad 19: Cálculos Iterativos
========================================

📚 TEORÍA:

En programación, un CÁLCULO ITERATIVO es cuando recorres una colección de
datos (generalmente una lista) para calcular un resultado paso a paso. Cada
iteración del ciclo procesa un dato y actualiza los acumuladores.

Este patrón es la base del procesamiento de datos: desde calcular el total
de un carrito de compras hasta generar estadísticas financieras.

PATRÓN BÁSICO — Acumulador:
    datos = [100, 200, 300, 400, 500]
    total = 0
    for dato in datos:
        total += dato
    print(f"Total: {total}")  →  1500

PATRÓN — Subtotal + Porcentaje + Total:
Este es un patrón muy común en el mundo real:

    precios = [1500, 2300, 800]

    # Paso 1: Calcular el subtotal (suma de todos los precios)
    subtotal = 0
    for precio in precios:
        subtotal += precio
    # subtotal = 4600

    # Paso 2: Calcular un porcentaje (ej: impuesto del 19%)
    porcentaje = 0.19
    impuesto = subtotal * porcentaje
    # impuesto = 874.0

    # Paso 3: Calcular el total
    total = subtotal + impuesto
    # total = 5474.0

PATRÓN — Cálculos por elemento:
A veces necesitas calcular algo PARA CADA ELEMENTO, no solo un total:

    items = [
        {"nombre": "Item A", "cantidad": 3, "precio": 1000},
        {"nombre": "Item B", "cantidad": 5, "precio": 500},
    ]

    subtotal_general = 0
    for item in items:
        subtotal_item = item["cantidad"] * item["precio"]
        subtotal_general += subtotal_item
        print(f"{item['nombre']}: {item['cantidad']} x ${item['precio']} = ${subtotal_item}")

    print(f"Subtotal general: ${subtotal_general}")

MÚLTIPLES ACUMULADORES:
Puedes llevar varios acumuladores simultáneamente:

    numeros = [15, -3, 22, -8, 10, -1, 30]
    suma_positivos = 0
    suma_negativos = 0
    cuenta_positivos = 0
    cuenta_negativos = 0

    for n in numeros:
        if n >= 0:
            suma_positivos += n
            cuenta_positivos += 1
        else:
            suma_negativos += n
            cuenta_negativos += 1

📝 INSTRUCCIONES:

Crea un script que procese una lista de elementos con precio y cantidad:

1. Crea la siguiente lista de diccionarios (representan artículos):
   [
       {"nombre": "Cuaderno", "cantidad": 4, "precio_unitario": 8500},
       {"nombre": "Lápiz", "cantidad": 12, "precio_unitario": 1200},
       {"nombre": "Borrador", "cantidad": 6, "precio_unitario": 800},
       {"nombre": "Regla", "cantidad": 3, "precio_unitario": 2500},
       {"nombre": "Marcador", "cantidad": 8, "precio_unitario": 3200},
       {"nombre": "Carpeta", "cantidad": 2, "precio_unitario": 12000},
   ]

2. Crea una función 'calcular_subtotal_item(cantidad, precio_unitario)' que
   devuelva cantidad * precio_unitario.

3. Recorre la lista e imprime para cada artículo:
   "[nombre] | [cantidad] x $[precio] = $[subtotal_item]"

4. Calcula e imprime:
   a) SUBTOTAL: La suma de todos los subtotales de cada artículo.
   b) DESCUENTO (10%): El monto del descuento sobre el subtotal.
   c) SUBTOTAL CON DESCUENTO: Subtotal - descuento.
   d) IMPUESTO (19%): Porcentaje sobre el subtotal con descuento.
   e) TOTAL: Subtotal con descuento + impuesto.

5. Muestra un resumen formateado con los montos alineados a la derecha.

✅ CRITERIOS DE ACEPTACIÓN:
- Se usa un ciclo for para recorrer la lista de artículos.
- Se usa un acumulador para calcular el subtotal general.
- Se calcula el descuento como un porcentaje del subtotal.
- Se calcula el impuesto sobre el subtotal con descuento.
- Todos los montos se muestran con separador de miles y 2 decimales.
- Se crea al menos una función (calcular_subtotal_item).
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# articulos = [
#     {"nombre": "Cuaderno", "cantidad": 4, "precio_unitario": 8500},
#     {"nombre": "Lápiz", "cantidad": 12, "precio_unitario": 1200},
#     {"nombre": "Borrador", "cantidad": 6, "precio_unitario": 800},
#     {"nombre": "Regla", "cantidad": 3, "precio_unitario": 2500},
#     {"nombre": "Marcador", "cantidad": 8, "precio_unitario": 3200},
#     {"nombre": "Carpeta", "cantidad": 2, "precio_unitario": 12000},
# ]
#
# PORCENTAJE_DESCUENTO = 0.10
# PORCENTAJE_IMPUESTO = 0.19
#
#
# def calcular_subtotal_item(cantidad, precio_unitario):
#     """Calcula el subtotal de un artículo."""
#     return cantidad * precio_unitario
#
#
# # 3. Recorrer e imprimir cada artículo
# print("=== DETALLE DE ARTÍCULOS ===\n")
# subtotal_general = 0
#
# for art in articulos:
#     sub_item = calcular_subtotal_item(art["cantidad"], art["precio_unitario"])
#     subtotal_general += sub_item
#     print(f"  {art['nombre']:<12} | {art['cantidad']:>3} x ${art['precio_unitario']:>10,.2f} = ${sub_item:>12,.2f}")
#
# # 4. Cálculos
# descuento = subtotal_general * PORCENTAJE_DESCUENTO
# subtotal_con_descuento = subtotal_general - descuento
# impuesto = subtotal_con_descuento * PORCENTAJE_IMPUESTO
# total = subtotal_con_descuento + impuesto
#
# # 5. Resumen
# ANCHO = 42
# print("\n" + "=" * ANCHO)
# print(f"{'SUBTOTAL:':<25}${subtotal_general:>14,.2f}")
# print(f"{'DESCUENTO (10%):':<25}-${descuento:>13,.2f}")
# print(f"{'SUBTOTAL C/DESC:':<25}${subtotal_con_descuento:>14,.2f}")
# print(f"{'IMPUESTO (19%):':<25}${impuesto:>14,.2f}")
# print("=" * ANCHO)
# print(f"{'TOTAL:':<25}${total:>14,.2f}")
# print("=" * ANCHO)
