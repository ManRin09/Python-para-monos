"""
========================================
🐒 Python para Monos
Módulo 1 — Actividad 05: Ciclo while
========================================

📚 TEORÍA:

El ciclo WHILE (mientras) repite un bloque de código MIENTRAS una condición
sea verdadera (True). Es ideal cuando NO SABES de antemano cuántas veces
necesitas repetir algo.

ESTRUCTURA:
    while condicion:
        # Este bloque se repite mientras condicion sea True
        # IMPORTANTE: algo debe cambiar para que la condición se vuelva False
        # De lo contrario tendrás un BUCLE INFINITO ♾️

EJEMPLO — Contador simple:
    contador = 1
    while contador <= 5:
        print(f"Iteración número {contador}")
        contador = contador + 1    # También se puede escribir: contador += 1
    print("¡Fin del ciclo!")

    Salida:
    Iteración número 1
    Iteración número 2
    Iteración número 3
    Iteración número 4
    Iteración número 5
    ¡Fin del ciclo!

VARIABLE CENTINELA:
Es una variable que controla cuándo debe terminar el ciclo:
    seguir = True
    while seguir:
        respuesta = input("¿Deseas continuar? (s/n): ")
        if respuesta == "n":
            seguir = False
    print("Programa terminado.")

INSTRUCCIONES DE CONTROL DENTRO DEL WHILE:

    break    → Rompe el ciclo INMEDIATAMENTE, sin importar la condición.
    continue → Salta A LA SIGUIENTE iteración, ignorando el resto del bloque.

    Ejemplo de break:
        while True:  # Ciclo infinito a propósito
            texto = input("Escribe 'salir' para terminar: ")
            if texto == "salir":
                break  # Sale del ciclo
            print(f"Escribiste: {texto}")

    Ejemplo de continue:
        numero = 0
        while numero < 10:
            numero += 1
            if numero % 2 == 0:
                continue  # Salta los pares, no los imprime
            print(numero)  # Solo imprime impares: 1, 3, 5, 7, 9

⚠️ PELIGRO — BUCLE INFINITO:
Si olvidas actualizar la variable de la condición, el ciclo nunca termina:
    contador = 1
    while contador <= 5:
        print(contador)
        # ¡Olvidamos incrementar contador! → Bucle infinito
    Para detenerlo manualmente: Ctrl + C en la terminal.

📝 INSTRUCCIONES:

Crea un script que funcione como un contador con las siguientes características:
1. Pide al usuario un número inicial (entero).
2. Pide al usuario un número final (entero, debe ser mayor que el inicial).
3. Pide al usuario un incremento (entero, debe ser mayor que 0).
4. Si el número final no es mayor que el inicial, muestra un error y no ejecuta
   el ciclo.
5. Si el incremento no es mayor que 0, muestra un error y no ejecuta el ciclo.
6. Usa un ciclo while para imprimir todos los números desde el inicial hasta
   el final (inclusive si es posible), incrementando según el valor dado.
7. Al final del ciclo, muestra cuántas iteraciones realizó el ciclo.

Ejemplo de ejecución:
    Número inicial: 3
    Número final: 15
    Incremento: 4
    Salida: 3, 7, 11, 15
    Total de iteraciones: 4

✅ CRITERIOS DE ACEPTACIÓN:
- Se debe usar input() para recibir los 3 valores.
- Se deben validar las entradas (final > inicial, incremento > 0).
- Se debe usar un ciclo while (no for).
- Se debe llevar un contador de iteraciones.
- Al final se imprime el total de iteraciones.
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
# print("=== Contador con While ===")
# inicio = int(input("Número inicial: "))
# fin = int(input("Número final: "))
# incremento = int(input("Incremento: "))
#
# if fin <= inicio:
#     print("Error: El número final debe ser mayor que el inicial.")
# elif incremento <= 0:
#     print("Error: El incremento debe ser mayor que 0.")
# else:
#     actual = inicio
#     iteraciones = 0
#
#     print("\nSecuencia: ", end="")
#     while actual <= fin:
#         if iteraciones > 0:
#             print(", ", end="")
#         print(actual, end="")
#         actual += incremento
#         iteraciones += 1
#
#     print(f"\nTotal de iteraciones: {iteraciones}")
