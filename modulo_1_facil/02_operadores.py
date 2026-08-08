"""
========================================
🐒 Python para Monos
Módulo 1 — Actividad 02: Operadores Matemáticos
========================================

📚 TEORÍA:

Los OPERADORES son símbolos que le dicen a Python que realice una operación
específica entre dos o más valores (operandos).

OPERADORES ARITMÉTICOS (los más comunes):

  Operador  |  Nombre          |  Ejemplo    |  Resultado
  ----------|------------------|-------------|----------
     +      |  Suma            |  10 + 3     |  13
     -      |  Resta           |  10 - 3     |  7
     *      |  Multiplicación  |  10 * 3     |  30
     /      |  División        |  10 / 3     |  3.3333...
     //     |  División entera |  10 // 3    |  3
     %      |  Módulo (resto)  |  10 % 3     |  1
     **     |  Potencia        |  10 ** 3    |  1000

PRECEDENCIA DE OPERADORES (orden en que se ejecutan):
1. Paréntesis ()           → Se evalúa primero lo que esté dentro.
2. Potencia **             → Luego las potencias.
3. Multiplicación, División, Módulo  *, /, //, %
4. Suma y Resta  +, -

Si dos operadores tienen la misma precedencia, se evalúan de izquierda a derecha.

Ejemplo:
    resultado = 2 + 3 * 4       →  14  (primero 3*4=12, luego 2+12=14)
    resultado = (2 + 3) * 4     →  20  (primero 2+3=5, luego 5*4=20)

TIPOS DE RESULTADO:
- int + int  →  int         (5 + 3 = 8)
- int + float  →  float     (5 + 3.0 = 8.0)
- int / int  →  SIEMPRE float  (10 / 2 = 5.0, no 5)
- int // int  →  int        (10 // 3 = 3)

La DIVISIÓN ENTERA (//) trunca los decimales, no redondea. Siempre baja al entero
más cercano por la izquierda:
    7 // 2  →  3   (no 3.5, no 4)
   -7 // 2  →  -4  (no -3, baja hacia la izquierda)

El MÓDULO (%) devuelve el residuo de la división:
    10 % 3  →  1   (porque 10 = 3*3 + 1)
    Es muy útil para saber si un número es par: numero % 2 == 0

📝 INSTRUCCIONES:

Crea un script que haga lo siguiente:
1. Declara dos variables numéricas: 'numero_a' con valor 17 y 'numero_b' con valor 5.
2. Realiza las 7 operaciones aritméticas entre esas dos variables y guarda
   cada resultado en una variable descriptiva (ej: suma, resta, etc.).
3. Imprime cada resultado con un mensaje descriptivo.
   Ejemplo de salida: "La suma de 17 + 5 = 22"
4. Crea una operación compuesta que use al menos 3 operadores y paréntesis.
   Imprímela mostrando la expresión y su resultado.
   Ejemplo: "Operación compuesta: (17 + 5) * 2 - 3 = ..."

✅ CRITERIOS DE ACEPTACIÓN:
- Se deben usar las 7 operaciones aritméticas: +, -, *, /, //, %, **
- Cada resultado debe guardarse en una variable con nombre descriptivo.
- Cada resultado debe imprimirse con un mensaje que incluya los operandos y el resultado.
- Debe haber al menos una operación compuesta con paréntesis.
- El script debe ejecutarse sin errores.
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# numero_a = 17
# numero_b = 5
#
# suma = numero_a + numero_b
# resta = numero_a - numero_b
# multiplicacion = numero_a * numero_b
# division = numero_a / numero_b
# division_entera = numero_a // numero_b
# modulo = numero_a % numero_b
# potencia = numero_a ** numero_b
#
# print(f"La suma de {numero_a} + {numero_b} = {suma}")
# print(f"La resta de {numero_a} - {numero_b} = {resta}")
# print(f"La multiplicación de {numero_a} * {numero_b} = {multiplicacion}")
# print(f"La división de {numero_a} / {numero_b} = {division}")
# print(f"La división entera de {numero_a} // {numero_b} = {division_entera}")
# print(f"El módulo de {numero_a} % {numero_b} = {modulo}")
# print(f"La potencia de {numero_a} ** {numero_b} = {potencia}")
#
# # Operación compuesta
# compuesta = (numero_a + numero_b) * 2 - numero_b ** 2
# print(f"\nOperación compuesta: ({numero_a} + {numero_b}) * 2 - {numero_b}² = {compuesta}")
