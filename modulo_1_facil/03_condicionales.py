"""
========================================
🐒 Python para Monos
Módulo 1 — Actividad 03: Condicionales
========================================

📚 TEORÍA:

Los CONDICIONALES son la forma en que un programa toma decisiones. Permiten
ejecutar un bloque de código SOLO si se cumple una condición específica.

ESTRUCTURA BÁSICA:

    if condicion:
        # Se ejecuta si la condición es True
    elif otra_condicion:
        # Se ejecuta si la primera fue False y esta es True
    else:
        # Se ejecuta si NINGUNA condición anterior fue True

REGLAS IMPORTANTES:
- La condición debe evaluar a True o False (un valor booleano).
- Después de if/elif/else SIEMPRE va dos puntos (:).
- El bloque de código dentro va INDENTADO (4 espacios por convención).
- 'elif' es la abreviatura de "else if". Puedes tener tantos elif como necesites.
- 'else' es opcional y solo puede haber uno al final.

OPERADORES DE COMPARACIÓN:
    ==    Igual a              (5 == 5  →  True)
    !=    Diferente de         (5 != 3  →  True)
    >     Mayor que            (5 > 3   →  True)
    <     Menor que            (3 < 5   →  True)
    >=    Mayor o igual que    (5 >= 5  →  True)
    <=    Menor o igual que    (3 <= 5  →  True)

OPERADORES LÓGICOS (para combinar condiciones):
    and   → True si AMBAS condiciones son True
            (5 > 3 and 10 > 7)  →  True
    or    → True si AL MENOS UNA condición es True
            (5 > 3 or 10 < 7)   →  True
    not   → Invierte el valor booleano
            not True  →  False

EJEMPLO PRÁCTICO:
    temperatura = 32

    if temperatura >= 35:
        print("Hace mucho calor 🔥")
    elif temperatura >= 25:
        print("El clima es agradable 😎")
    elif temperatura >= 15:
        print("Hace un poco de frío 🧥")
    else:
        print("¡Hace mucho frío! 🥶")

Python evalúa las condiciones DE ARRIBA HACIA ABAJO. En cuanto encuentra una
que sea True, ejecuta su bloque y SALTA todas las demás.

CONDICIONALES ANIDADOS:
Puedes poner un if dentro de otro if:
    if edad >= 18:
        if tiene_licencia:
            print("Puede conducir")
        else:
            print("Necesita licencia")
    else:
        print("Es menor de edad")

📝 INSTRUCCIONES:

Crea un script que determine el estado de un estudiante según su nota (calificación):
1. Declara una variable 'nota' con un valor numérico entre 0 y 100.
2. Usa condicionales para clasificar la nota según estas reglas:
   - 90 a 100: "Excelente 🌟"
   - 80 a 89: "Sobresaliente 💪"
   - 70 a 79: "Bueno 👍"
   - 60 a 69: "Aceptable 🤔"
   - Menor a 60: "Reprobado ❌"
3. Antes de clasificar, valida que la nota esté en el rango 0-100.
   Si no lo está, imprime: "Error: La nota debe estar entre 0 y 100".
4. Imprime el resultado con el formato: "Nota: [nota] — Estado: [estado]"

✅ CRITERIOS DE ACEPTACIÓN:
- El script debe usar if, elif y else correctamente.
- Debe validar que la nota esté entre 0 y 100 (usar operadores lógicos).
- Debe cubrir los 5 rangos de clasificación descritos.
- El mensaje de salida debe incluir tanto la nota como el estado.
- El script debe ejecutarse sin errores con cualquier valor de nota.
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# nota = 85
#
# if nota < 0 or nota > 100:
#     print("Error: La nota debe estar entre 0 y 100")
# elif nota >= 90:
#     estado = "Excelente 🌟"
#     print(f"Nota: {nota} — Estado: {estado}")
# elif nota >= 80:
#     estado = "Sobresaliente 💪"
#     print(f"Nota: {nota} — Estado: {estado}")
# elif nota >= 70:
#     estado = "Bueno 👍"
#     print(f"Nota: {nota} — Estado: {estado}")
# elif nota >= 60:
#     estado = "Aceptable 🤔"
#     print(f"Nota: {nota} — Estado: {estado}")
# else:
#     estado = "Reprobado ❌"
#     print(f"Nota: {nota} — Estado: {estado}")
