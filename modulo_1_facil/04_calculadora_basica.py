"""
========================================
🐒 Python para Monos
Módulo 1 — Actividad 04: Calculadora Básica con input()
========================================

📚 TEORÍA:

Hasta ahora hemos "hardcodeado" los valores directamente en el código. En la
vida real, los programas necesitan recibir datos del USUARIO. Para eso existe
la función input().

CÓMO FUNCIONA input():
    dato = input("Escribe algo: ")

- Muestra el mensaje entre comillas en la consola.
- PAUSA el programa y espera a que el usuario escriba algo y presione Enter.
- Lo que el usuario escriba se guarda en la variable 'dato'.

⚠️ MUY IMPORTANTE: input() SIEMPRE devuelve un STRING (cadena de texto).
   Incluso si el usuario escribe un número, Python lo guarda como texto:

    numero = input("Escribe un número: ")  # El usuario escribe: 5
    print(type(numero))  →  <class 'str'>   # ¡Es texto, no número!

Para poder hacer operaciones matemáticas, necesitas CONVERTIR el texto a número:
    int()   → Convierte a número entero       int("5")    →  5
    float() → Convierte a número decimal       float("3.14") →  3.14

Si el usuario escribe algo que no es un número y tratas de convertir, Python
lanza un error (ValueError). Por ahora no te preocupes, eso lo veremos en la
actividad 14 (manejo de errores).

EJEMPLO COMPLETO:
    nombre = input("¿Cómo te llamas? ")
    edad_texto = input("¿Cuántos años tienes? ")
    edad = int(edad_texto)  # Convertimos texto a entero

    print(f"Hola {nombre}, en 10 años tendrás {edad + 10} años.")

ATAJO — Conversión en la misma línea:
    edad = int(input("¿Cuántos años tienes? "))

📝 INSTRUCCIONES:

Crea una calculadora básica que funcione así:
1. Pide al usuario que ingrese un primer número (puede ser decimal).
2. Pide al usuario que ingrese un segundo número (puede ser decimal).
3. Pide al usuario que elija una operación escribiendo un símbolo: +, -, *, /
4. Realiza la operación elegida y muestra el resultado.
5. Si el usuario elige división y el segundo número es 0, muestra:
   "Error: No se puede dividir entre cero."
6. Si el usuario escribe un símbolo de operación inválido, muestra:
   "Error: Operación no válida. Usa +, -, * o /"

Formato de salida esperado:
    "Resultado: [num1] [operación] [num2] = [resultado]"
    Ejemplo: "Resultado: 10.0 + 5.0 = 15.0"

✅ CRITERIOS DE ACEPTACIÓN:
- Se debe usar input() para recibir los dos números y la operación.
- Los números deben convertirse a float para permitir decimales.
- Se deben soportar las 4 operaciones: +, -, *, /
- Se debe validar la división entre cero.
- Se debe validar que la operación sea una de las 4 permitidas.
- El resultado debe mostrarse con un mensaje descriptivo.
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# print("=== Calculadora Básica ===")
# numero_1 = float(input("Ingresa el primer número: "))
# numero_2 = float(input("Ingresa el segundo número: "))
# operacion = input("Elige una operación (+, -, *, /): ")
#
# if operacion == "+":
#     resultado = numero_1 + numero_2
#     print(f"Resultado: {numero_1} + {numero_2} = {resultado}")
# elif operacion == "-":
#     resultado = numero_1 - numero_2
#     print(f"Resultado: {numero_1} - {numero_2} = {resultado}")
# elif operacion == "*":
#     resultado = numero_1 * numero_2
#     print(f"Resultado: {numero_1} * {numero_2} = {resultado}")
# elif operacion == "/":
#     if numero_2 == 0:
#         print("Error: No se puede dividir entre cero.")
#     else:
#         resultado = numero_1 / numero_2
#         print(f"Resultado: {numero_1} / {numero_2} = {resultado}")
# else:
#     print("Error: Operación no válida. Usa +, -, * o /")
