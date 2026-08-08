"""
========================================
🐒 Python para Monos
Módulo 2 — Actividad 11: Funciones Básicas
========================================

📚 TEORÍA:

Una FUNCIÓN es un bloque de código reutilizable que realiza una tarea específica.
En lugar de escribir el mismo código una y otra vez, lo encapsulas en una función
y lo llamas cada vez que lo necesites.

DEFINIR UNA FUNCIÓN con def:
    def saludar():
        print("¡Hola, mundo!")

    saludar()  # Llamar a la función → Imprime: ¡Hola, mundo!

PARÁMETROS (datos que recibe la función):
    def saludar(nombre):
        print(f"¡Hola, {nombre}!")

    saludar("Carlos")  →  ¡Hola, Carlos!
    saludar("María")   →  ¡Hola, María!

    Puedes tener múltiples parámetros:
    def sumar(a, b):
        resultado = a + b
        print(f"{a} + {b} = {resultado}")

    sumar(5, 3)  →  5 + 3 = 8

RETURN (devolver un valor):
Las funciones pueden DEVOLVER un resultado al código que las llamó:

    def multiplicar(a, b):
        return a * b

    resultado = multiplicar(4, 5)
    print(resultado)  →  20

    Sin return, la función devuelve None por defecto.
    Cuando Python llega a return, SALE de la función inmediatamente.

PARÁMETROS CON VALORES POR DEFECTO:
    def saludar(nombre, saludo="Hola"):
        return f"{saludo}, {nombre}!"

    saludar("Carlos")             →  "Hola, Carlos!"
    saludar("Carlos", "Buenos días")  →  "Buenos días, Carlos!"

    ⚠️ Los parámetros con valor por defecto deben ir AL FINAL.

SCOPE (ALCANCE) DE VARIABLES:
- Variables LOCALES: existen SOLO dentro de la función.
- Variables GLOBALES: existen fuera de las funciones, en el nivel del script.

    mensaje = "Soy global"  # Variable global

    def mi_funcion():
        mensaje_local = "Soy local"  # Variable local
        print(mensaje)        # ✅ Puede acceder a variables globales
        print(mensaje_local)  # ✅ Puede acceder a sus propias variables locales

    mi_funcion()
    print(mensaje)        # ✅ Funciona
    print(mensaje_local)  # ❌ Error! No existe fuera de la función

FUNCIONES QUE LLAMAN A OTRAS FUNCIONES:
    def calcular_area(base, altura):
        return base * altura

    def mostrar_area(base, altura):
        area = calcular_area(base, altura)
        print(f"El área es: {area}")

    mostrar_area(5, 3)  →  El área es: 15

📝 INSTRUCCIONES:

Crea un script con las siguientes funciones (y luego llámalas para probarlas):

1. Función 'calcular_promedio(notas)':
   - Recibe una lista de notas numéricas.
   - Devuelve (return) el promedio.
   - Si la lista está vacía, devuelve 0.

2. Función 'determinar_estado(promedio)':
   - Recibe un promedio numérico.
   - Devuelve un string con el estado:
     >= 90: "Excelente", >= 80: "Bueno", >= 60: "Regular", < 60: "Insuficiente"

3. Función 'generar_reporte(nombre_estudiante, notas)':
   - Recibe el nombre del estudiante y su lista de notas.
   - Usa calcular_promedio() y determinar_estado() internamente.
   - Imprime un reporte formateado con: nombre, notas, promedio y estado.
   - No devuelve nada (solo imprime).

4. En la sección principal del script, crea 3 estudiantes con sus notas y
   llama a generar_reporte() para cada uno.

✅ CRITERIOS DE ACEPTACIÓN:
- Se definen al menos 3 funciones con def.
- Al menos una función tiene parámetros y usa return.
- Una función llama a otras funciones internamente.
- Las funciones se prueban con datos de ejemplo en la sección principal.
- No se usan variables globales para pasar datos entre funciones.
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# def calcular_promedio(notas):
#     """Calcula el promedio de una lista de notas."""
#     if len(notas) == 0:
#         return 0
#     suma = 0
#     for nota in notas:
#         suma += nota
#     return suma / len(notas)
#
#
# def determinar_estado(promedio):
#     """Determina el estado académico según el promedio."""
#     if promedio >= 90:
#         return "Excelente 🌟"
#     elif promedio >= 80:
#         return "Bueno 👍"
#     elif promedio >= 60:
#         return "Regular 🤔"
#     else:
#         return "Insuficiente ❌"
#
#
# def generar_reporte(nombre_estudiante, notas):
#     """Genera e imprime un reporte del estudiante."""
#     promedio = calcular_promedio(notas)
#     estado = determinar_estado(promedio)
#
#     print(f"\n{'=' * 35}")
#     print(f"  Reporte de: {nombre_estudiante}")
#     print(f"{'=' * 35}")
#     print(f"  Notas: {notas}")
#     print(f"  Promedio: {promedio:.2f}")
#     print(f"  Estado: {estado}")
#     print(f"{'=' * 35}")
#
#
# # === Sección principal ===
# generar_reporte("Ana López", [85, 92, 78, 90, 88])
# generar_reporte("Carlos Méndez", [60, 55, 70, 65, 58])
# generar_reporte("Sofía Herrera", [95, 98, 92, 100, 97])
