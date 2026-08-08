"""
========================================
🐒 Python para Monos
Módulo 1 — Actividad 10: Menú de Consola Interactivo
========================================

📚 TEORÍA:

Un MENÚ DE CONSOLA es un programa que muestra opciones al usuario, espera su
elección, ejecuta la acción correspondiente, y vuelve a mostrar el menú.
Esto se repite infinitamente hasta que el usuario decida salir.

Este patrón combina TODO lo aprendido en el Módulo 1:
- Variables para guardar datos.
- input() para recibir la opción del usuario.
- Condicionales (if/elif/else) para ejecutar la acción correcta.
- Ciclo while True para mantener el menú activo.
- break para salir del ciclo cuando el usuario elige la opción de salida.
- Listas para almacenar datos.
- f-strings para formatear la salida.

ESTRUCTURA TÍPICA DE UN MENÚ:

    while True:
        print("\\n=== MENÚ PRINCIPAL ===")
        print("1. Opción A")
        print("2. Opción B")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            # Código para la opción A
            print("Ejecutando opción A...")
        elif opcion == "2":
            # Código para la opción B
            print("Ejecutando opción B...")
        elif opcion == "3":
            print("¡Hasta luego! 👋")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

BUENAS PRÁCTICAS:
1. Siempre incluir una opción de SALIDA clara.
2. Siempre manejar opciones INVÁLIDAS con un else.
3. Limpiar visualmente la consola entre acciones con saltos de línea (\\n).
4. Usar comparación con strings ("1", "2") en lugar de int para evitar errores
   si el usuario escribe letras.
5. Dar retroalimentación al usuario después de cada acción.

VARIANTE — Menú con funcionalidad acumulativa:
El menú puede ir acumulando datos en una lista que persiste entre iteraciones:

    nombres = []  # Lista que persiste fuera del ciclo
    while True:
        opcion = input("1. Agregar nombre  2. Ver nombres  3. Salir: ")
        if opcion == "1":
            nombre = input("Nombre: ")
            nombres.append(nombre)
        elif opcion == "2":
            for n in nombres:
                print(f"- {n}")
        elif opcion == "3":
            break

📝 INSTRUCCIONES:

Crea un menú interactivo de "Administrador de Notas de Estudiantes" que ofrezca
las siguientes opciones:

    === ADMINISTRADOR DE NOTAS ===
    1. Agregar nota
    2. Ver todas las notas
    3. Calcular promedio
    4. Ver nota más alta y más baja
    5. Salir

Comportamiento esperado:
1. AGREGAR NOTA: Pide un número al usuario y lo agrega a una lista de notas.
   Debe validar que el número esté entre 0 y 100. Si no, muestra un error
   y NO lo agrega.

2. VER TODAS LAS NOTAS: Imprime todas las notas guardadas. Si no hay notas,
   muestra: "No hay notas registradas."

3. CALCULAR PROMEDIO: Calcula e imprime el promedio de todas las notas.
   Si no hay notas, muestra: "No hay notas para calcular el promedio."

4. VER NOTA MÁS ALTA Y MÁS BAJA: Muestra la nota máxima y mínima.
   Si no hay notas, muestra un mensaje apropiado.

5. SALIR: Muestra un mensaje de despedida y termina el programa.

Si el usuario elige una opción inválida, muestra:
   "Opción no válida. Por favor elige del 1 al 5."

✅ CRITERIOS DE ACEPTACIÓN:
- El menú se muestra repetidamente hasta que el usuario elija "5" (Salir).
- Se usa while True con break para controlar el ciclo.
- Se usa una lista para almacenar las notas (persiste entre iteraciones).
- Opción 1: valida rango 0-100 antes de agregar.
- Opción 2: muestra mensaje si la lista está vacía.
- Opción 3: calcula el promedio correctamente (suma / cantidad).
- Opción 4: encuentra el máximo y mínimo usando un ciclo for (no max()/min()).
- Opciones inválidas se manejan con else.
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# notas = []
#
# while True:
#     print("\n=== ADMINISTRADOR DE NOTAS ===")
#     print("1. Agregar nota")
#     print("2. Ver todas las notas")
#     print("3. Calcular promedio")
#     print("4. Ver nota más alta y más baja")
#     print("5. Salir")
#
#     opcion = input("\nElige una opción: ")
#
#     if opcion == "1":
#         nota_texto = input("Ingresa la nota (0-100): ")
#         nota = float(nota_texto)
#         if nota < 0 or nota > 100:
#             print("❌ Error: La nota debe estar entre 0 y 100.")
#         else:
#             notas.append(nota)
#             print(f"✅ Nota {nota} agregada correctamente.")
#
#     elif opcion == "2":
#         if len(notas) == 0:
#             print("No hay notas registradas.")
#         else:
#             print(f"\n📋 Notas registradas ({len(notas)}):")
#             for i, n in enumerate(notas, start=1):
#                 print(f"  {i}. {n}")
#
#     elif opcion == "3":
#         if len(notas) == 0:
#             print("No hay notas para calcular el promedio.")
#         else:
#             suma = 0
#             for n in notas:
#                 suma += n
#             promedio = suma / len(notas)
#             print(f"📊 Promedio de notas: {promedio:.2f}")
#
#     elif opcion == "4":
#         if len(notas) == 0:
#             print("No hay notas registradas para comparar.")
#         else:
#             mayor = notas[0]
#             menor = notas[0]
#             for n in notas:
#                 if n > mayor:
#                     mayor = n
#                 if n < menor:
#                     menor = n
#             print(f"📈 Nota más alta: {mayor}")
#             print(f"📉 Nota más baja: {menor}")
#
#     elif opcion == "5":
#         print("¡Hasta luego! 👋 Gracias por usar el administrador.")
#         break
#
#     else:
#         print("❌ Opción no válida. Por favor elige del 1 al 5.")
