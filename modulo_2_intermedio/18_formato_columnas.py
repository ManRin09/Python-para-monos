"""
========================================
🐒 Python para Monos
Módulo 2 — Actividad 18: Formato de Columnas en Consola
========================================

📚 TEORÍA:

Cuando necesitas mostrar datos tabulares en la consola (como una tabla),
el simple print() no alinea bien las columnas porque cada texto tiene
diferente longitud. Para resolver esto, Python ofrece métodos de ALINEACIÓN.

MÉTODOS DE ALINEACIÓN DE STRINGS:

    .ljust(ancho)   → Alinea a la IZQUIERDA, rellena con espacios a la derecha.
    .rjust(ancho)   → Alinea a la DERECHA, rellena con espacios a la izquierda.
    .center(ancho)  → CENTRA el texto, rellena ambos lados con espacios.

    "Hola".ljust(15)    →  "Hola           "   (15 caracteres total)
    "Hola".rjust(15)    →  "           Hola"
    "Hola".center(15)   →  "     Hola      "

    También puedes especificar el carácter de relleno:
    "Hola".ljust(15, ".")   →  "Hola..........."
    "Hola".center(15, "-")  →  "-----Hola------"

¿CUÁNDO USAR CADA UNO?
    - ljust: Para texto (nombres, descripciones) → Alineación natural.
    - rjust: Para números (precios, cantidades) → Los números se leen mejor
             alineados a la derecha, como en una hoja de cálculo.
    - center: Para encabezados y títulos.

EJEMPLO — Tabla bien formateada:

    print("Producto".ljust(20) + "Cantidad".rjust(10) + "Precio".rjust(12))
    print("-" * 42)
    print("Laptop".ljust(20) + "3".rjust(10) + "$2,500.00".rjust(12))
    print("Mouse".ljust(20) + "10".rjust(10) + "$85.00".rjust(12))
    print("Teclado".ljust(20) + "5".rjust(10) + "$150.00".rjust(12))

    Resultado:
    Producto            Cantidad      Precio
    ------------------------------------------
    Laptop                     3  $2,500.00
    Mouse                     10     $85.00
    Teclado                    5    $150.00

ALTERNATIVA CON F-STRINGS (más compacta):
    Los f-strings también permiten alinear directamente:

    nombre = "Laptop"
    cantidad = 3
    precio = 2500.00

    print(f"{'Producto':<20}{'Cantidad':>10}{'Precio':>12}")
    #       :<20 = ljust(20)   :>10 = rjust(10)

    print(f"{nombre:<20}{cantidad:>10}${precio:>11,.2f}")

    Especificadores en f-strings:
    :<20   → Alinear izquierda, ancho 20  (equivale a ljust)
    :>10   → Alinear derecha, ancho 10    (equivale a rjust)
    :^15   → Centrar, ancho 15            (equivale a center)
    :>11,.2f → Derecha, ancho 11, miles, 2 decimales

CONSEJO: Usa constantes para los anchos para que sea fácil de ajustar:
    ANCHO_NOMBRE = 20
    ANCHO_CANT = 10
    ANCHO_PRECIO = 12

📝 INSTRUCCIONES:

Crea un script que muestre una tabla formateada en consola con datos de empleados:

1. Crea una lista de diccionarios con al menos 6 empleados, cada uno con:
   "nombre", "departamento", "horas_trabajadas" (int) y "tarifa_hora" (float).

2. Define constantes para los anchos de columna:
   ANCHO_NOMBRE = 22, ANCHO_DEPTO = 18, ANCHO_HORAS = 8, ANCHO_PAGO = 14

3. Imprime un encabezado de tabla usando ljust/rjust con los anchos definidos:
   NOMBRE                DEPARTAMENTO        HORAS       PAGO TOTAL

4. Imprime una línea separadora de guiones.

5. Para cada empleado, calcula el pago (horas * tarifa) e imprime una fila
   usando ljust para texto y rjust para números.

6. Al final, imprime una línea separadora y el TOTAL de pagos, alineado a
   la derecha en la columna de "PAGO TOTAL".

✅ CRITERIOS DE ACEPTACIÓN:
- Se usan .ljust() y .rjust() (o sus equivalentes en f-strings) para alinear.
- Los textos van alineados a la izquierda (ljust).
- Los números van alineados a la derecha (rjust).
- Los montos usan formato con separador de miles y 2 decimales.
- Hay un encabezado de columnas y líneas separadoras.
- Se muestra un total al final, alineado correctamente.
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# # 1. Datos
# empleados = [
#     {"nombre": "Ana López", "departamento": "Ingeniería", "horas_trabajadas": 160, "tarifa_hora": 45000.0},
#     {"nombre": "Carlos Méndez", "departamento": "Diseño", "horas_trabajadas": 140, "tarifa_hora": 38000.0},
#     {"nombre": "María García", "departamento": "Ingeniería", "horas_trabajadas": 168, "tarifa_hora": 52000.0},
#     {"nombre": "Juan Pérez", "departamento": "Soporte", "horas_trabajadas": 150, "tarifa_hora": 30000.0},
#     {"nombre": "Sofía Herrera", "departamento": "Diseño", "horas_trabajadas": 155, "tarifa_hora": 40000.0},
#     {"nombre": "Pedro Castillo", "departamento": "Soporte", "horas_trabajadas": 145, "tarifa_hora": 32000.0},
# ]
#
# # 2. Constantes de ancho
# AN = 22   # Ancho nombre
# AD = 18   # Ancho departamento
# AH = 8    # Ancho horas
# AP = 16   # Ancho pago
# ANCHO_TOTAL = AN + AD + AH + AP
#
# # 3. Encabezado
# print("NOMBRE".ljust(AN) + "DEPARTAMENTO".ljust(AD) + "HORAS".rjust(AH) + "PAGO TOTAL".rjust(AP))
#
# # 4. Separador
# print("=" * ANCHO_TOTAL)
#
# # 5. Filas de datos
# total_pagos = 0
# for emp in empleados:
#     pago = emp["horas_trabajadas"] * emp["tarifa_hora"]
#     total_pagos += pago
#     pago_formateado = f"${pago:,.2f}"
#     print(
#         emp["nombre"].ljust(AN)
#         + emp["departamento"].ljust(AD)
#         + str(emp["horas_trabajadas"]).rjust(AH)
#         + pago_formateado.rjust(AP)
#     )
#
# # 6. Total
# print("=" * ANCHO_TOTAL)
# total_formateado = f"${total_pagos:,.2f}"
# print("TOTAL".ljust(AN + AD + AH) + total_formateado.rjust(AP))
