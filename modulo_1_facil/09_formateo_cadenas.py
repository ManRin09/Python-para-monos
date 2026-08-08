"""
========================================
🐒 Python para Monos
Módulo 1 — Actividad 09: Formateo de Cadenas (f-strings)
========================================

📚 TEORÍA:

El FORMATEO DE CADENAS permite insertar valores de variables dentro de un texto
de forma elegante y legible. Python ofrece varias formas de hacerlo, pero la
más moderna y recomendada son los F-STRINGS (disponibles desde Python 3.6).

MÉTODO 1 — CONCATENACIÓN (la forma antigua y torpe):
    nombre = "Carlos"
    edad = 28
    print("Hola, me llamo " + nombre + " y tengo " + str(edad) + " años.")
    # Funciona, pero es incómodo y hay que convertir números a str().

MÉTODO 2 — .format() (la forma intermedia):
    print("Hola, me llamo {} y tengo {} años.".format(nombre, edad))
    # Las {} se reemplazan por los argumentos en orden.
    # También puedes usar índices: "Hola {0}, tienes {1}".format(nombre, edad)
    # O nombres: "Hola {n}".format(n=nombre)

MÉTODO 3 — F-STRINGS (la forma moderna y recomendada ⭐):
    print(f"Hola, me llamo {nombre} y tengo {edad} años.")
    # Simplemente pones una 'f' antes de las comillas y metes las variables
    # directamente entre llaves {}. ¡Limpio, simple y poderoso!

    Puedes poner CUALQUIER expresión válida de Python dentro de las llaves:
    print(f"En 5 años tendré {edad + 5} años.")
    print(f"Mi nombre en mayúsculas: {nombre.upper()}")
    print(f"2 elevado a 10 es: {2 ** 10}")

FORMATO DE NÚMEROS EN F-STRINGS:

  Especificador  |  Descripción               |  Ejemplo               |  Resultado
  :.2f           |  2 decimales               |  f"{3.14159:.2f}"      |  "3.14"
  :.0f           |  Sin decimales             |  f"{3.14159:.0f}"      |  "3"
  :,             |  Separador de miles        |  f"{1000000:,}"        |  "1,000,000"
  :,.2f          |  Miles + 2 decimales       |  f"{1234567.891:,.2f}" |  "1,234,567.89"
  :%             |  Formato porcentaje        |  f"{0.856:.1%}"        |  "85.6%"
  :>10           |  Alineado a la derecha (10)|  f"{'hola':>10}"       |  "      hola"
  :<10           |  Alineado a la izquierda   |  f"{'hola':<10}"       |  "hola      "
  :^10           |  Centrado                  |  f"{'hola':^10}"       |  "   hola   "
  :0>5           |  Rellenar con ceros        |  f"{42:0>5}"           |  "00042"

MULTILÍNEA CON F-STRINGS:
    mensaje = (
        f"Nombre: {nombre}\n"
        f"Edad: {edad}\n"
        f"Estatura: {1.75:.1f}m"
    )
    print(mensaje)

📝 INSTRUCCIONES:

Crea un script que genere un "recibo" de texto formateado con f-strings:

1. Declara las siguientes variables:
   - cliente = "María García"
   - articulo = "Monitor LED 24 pulgadas"
   - cantidad = 3
   - precio_unitario = 459999.50
   - descuento = 0.15  (15%)

2. Calcula:
   - subtotal = cantidad * precio_unitario
   - monto_descuento = subtotal * descuento
   - total = subtotal - monto_descuento

3. Imprime un recibo con el siguiente formato EXACTO (usa f-strings para todo):

   ========================================
   RECIBO DE COMPRA
   ========================================
   Cliente:        María García
   Artículo:       Monitor LED 24 pulgadas
   Cantidad:       3
   Precio unit.:   $459,999.50
   ----------------------------------------
   Subtotal:       $1,379,998.50
   Descuento (15%): -$206,999.78
   ========================================
   TOTAL:          $1,172,998.73
   ========================================

   Nota: Los precios deben tener separador de miles y 2 decimales.

✅ CRITERIOS DE ACEPTACIÓN:
- Se deben usar f-strings (no concatenación ni .format()).
- Los precios deben mostrarse con formato: separador de miles y 2 decimales (:,.2f).
- El descuento debe mostrarse como porcentaje en el encabezado.
- Los textos deben estar alineados visualmente (puedes usar espacios o :</>).
- Los cálculos deben ser correctos.
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# cliente = "María García"
# articulo = "Monitor LED 24 pulgadas"
# cantidad = 3
# precio_unitario = 459999.50
# descuento = 0.15
#
# subtotal = cantidad * precio_unitario
# monto_descuento = subtotal * descuento
# total = subtotal - monto_descuento
#
# print("=" * 40)
# print("RECIBO DE COMPRA")
# print("=" * 40)
# print(f"{'Cliente:':<16}{cliente}")
# print(f"{'Artículo:':<16}{articulo}")
# print(f"{'Cantidad:':<16}{cantidad}")
# print(f"{'Precio unit.:':<16}${precio_unitario:,.2f}")
# print("-" * 40)
# print(f"{'Subtotal:':<16}${subtotal:,.2f}")
# print(f"{'Descuento (' + str(int(descuento * 100)) + '%):':<16}-${monto_descuento:,.2f}")
# print("=" * 40)
# print(f"{'TOTAL:':<16}${total:,.2f}")
# print("=" * 40)
