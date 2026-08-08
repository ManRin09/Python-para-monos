"""
========================================
🐒 Python para Monos
Módulo 1 — Actividad 06: Ciclo for
========================================

📚 TEORÍA:

El ciclo FOR es la herramienta de iteración más usada en Python. A diferencia
del while, el for recorre una SECUENCIA de elementos de forma automática, sin
necesidad de manejar un contador manualmente.

ESTRUCTURA BÁSICA:
    for variable in secuencia:
        # Este bloque se ejecuta una vez por cada elemento de la secuencia
        # 'variable' toma el valor del elemento actual en cada iteración

ITERAR SOBRE UNA LISTA:
    frutas = ["manzana", "banana", "cereza"]
    for fruta in frutas:
        print(fruta)

    Salida:
    manzana
    banana
    cereza

LA FUNCIÓN range():
Genera una secuencia de números. Es perfecta para cuando necesitas un contador:

    range(fin)              → Números desde 0 hasta fin-1
    range(inicio, fin)      → Números desde inicio hasta fin-1
    range(inicio, fin, paso) → Números con un incremento específico

    Ejemplos:
    range(5)        →  0, 1, 2, 3, 4
    range(2, 8)     →  2, 3, 4, 5, 6, 7
    range(0, 10, 2) →  0, 2, 4, 6, 8
    range(10, 0, -1) → 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

    for i in range(5):
        print(f"Iteración {i}")

ACUMULADORES:
Un patrón muy común es usar una variable que "acumula" valores en cada iteración:

    numeros = [10, 20, 30, 40, 50]
    total = 0  # Acumulador, inicia en 0
    for numero in numeros:
        total += numero  # Equivalente a: total = total + numero
    print(f"La suma total es: {total}")  →  150

ITERAR CON ÍNDICE usando enumerate():
Si necesitas tanto el índice como el valor:
    colores = ["rojo", "verde", "azul"]
    for indice, color in enumerate(colores):
        print(f"{indice}: {color}")

    Salida:
    0: rojo
    1: verde
    2: azul

ITERAR SOBRE UN STRING:
Los strings son secuencias de caracteres:
    for letra in "Python":
        print(letra)
    # Imprime: P, y, t, h, o, n (cada uno en una línea)

📝 INSTRUCCIONES:

Crea un script que haga lo siguiente:

PARTE 1 — Tabla de multiplicar:
1. Pide al usuario un número entero.
2. Usa un ciclo for con range() para imprimir su tabla de multiplicar del 1 al 10.
   Formato: "[numero] x [i] = [resultado]"

PARTE 2 — Suma acumulada:
3. Dada la siguiente lista de precios: [1500, 2300, 800, 4500, 1200, 3700]
4. Usa un ciclo for para recorrer la lista y calcular:
   - La suma total de todos los precios.
   - El precio más alto.
   - El precio más bajo.
5. Imprime los tres resultados.

✅ CRITERIOS DE ACEPTACIÓN:
- PARTE 1: Se usa for con range(1, 11) para la tabla de multiplicar.
- PARTE 1: Se imprime la tabla completa del 1 al 10.
- PARTE 2: Se usa un ciclo for para recorrer la lista (no funciones como sum()).
- PARTE 2: Se calcula la suma, el máximo y el mínimo usando acumuladores.
- Los resultados se imprimen con mensajes descriptivos.
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# # PARTE 1 — Tabla de multiplicar
# print("=== TABLA DE MULTIPLICAR ===")
# numero = int(input("Ingresa un número para ver su tabla: "))
#
# for i in range(1, 11):
#     resultado = numero * i
#     print(f"{numero} x {i} = {resultado}")
#
# # PARTE 2 — Suma acumulada
# print("\n=== SUMA ACUMULADA ===")
# precios = [1500, 2300, 800, 4500, 1200, 3700]
#
# suma_total = 0
# precio_mayor = precios[0]
# precio_menor = precios[0]
#
# for precio in precios:
#     suma_total += precio
#     if precio > precio_mayor:
#         precio_mayor = precio
#     if precio < precio_menor:
#         precio_menor = precio
#
# print(f"Lista de precios: {precios}")
# print(f"Suma total: ${suma_total}")
# print(f"Precio más alto: ${precio_mayor}")
# print(f"Precio más bajo: ${precio_menor}")
