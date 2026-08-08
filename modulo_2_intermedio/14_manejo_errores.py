"""
========================================
🐒 Python para Monos
Módulo 2 — Actividad 14: Manejo de Errores
========================================

📚 TEORÍA:

Los ERRORES (excepciones) son situaciones inesperadas que hacen que tu programa
se detenga abruptamente. En el mundo real, los errores son inevitables: el
usuario escribe texto donde debería ir un número, un archivo no existe, se
intenta dividir entre cero, etc.

El MANEJO DE EXCEPCIONES permite que tu programa detecte estos errores,
los maneje con gracia, y continúe ejecutándose en lugar de "crashear".

ERRORES COMUNES EN PYTHON:
    ValueError       → Valor incorrecto (ej: int("hola"))
    TypeError        → Tipo incorrecto (ej: "5" + 3)
    ZeroDivisionError → División entre cero (ej: 10 / 0)
    FileNotFoundError → Archivo no encontrado (ej: open("inexistente.txt"))
    KeyError         → Clave inexistente en diccionario (ej: d["clave_falsa"])
    IndexError       → Índice fuera de rango (ej: lista[100] en lista de 3)

ESTRUCTURA TRY/EXCEPT:

    try:
        # Código que PODRÍA fallar
        resultado = 10 / 0
    except ZeroDivisionError:
        # Se ejecuta SOLO si ocurre ese error específico
        print("Error: No se puede dividir entre cero.")

CAPTURAR MÚLTIPLES EXCEPCIONES:

    try:
        numero = int(input("Número: "))
        resultado = 100 / numero
    except ValueError:
        print("Error: Eso no es un número válido.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

CAPTURAR CUALQUIER EXCEPCIÓN (genérico):

    try:
        # código riesgoso
        pass
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    ⚠️ Usar 'except Exception' es útil pero impreciso. Siempre que puedas,
    captura la excepción ESPECÍFICA.

BLOQUE ELSE (se ejecuta si NO hubo error):

    try:
        numero = int(input("Número: "))
    except ValueError:
        print("Error: No es un número.")
    else:
        print(f"Ingresaste el número {numero}")  # Solo si no hubo error

BLOQUE FINALLY (se ejecuta SIEMPRE, haya o no error):

    try:
        archivo = open("datos.txt")
        contenido = archivo.read()
    except FileNotFoundError:
        print("El archivo no existe.")
    finally:
        print("Este mensaje aparece siempre.")
        # Útil para cerrar archivos, conexiones, etc.

PATRÓN: VALIDAR INPUT CON WHILE + TRY:
    while True:
        try:
            edad = int(input("Tu edad: "))
            break  # Sale del while si la conversión fue exitosa
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

📝 INSTRUCCIONES:

Crea un script con las siguientes funciones de validación segura:

1. Función 'pedir_entero(mensaje)':
   - Usa un while True con try/except para pedir un entero al usuario.
   - Si el usuario escribe algo que no es un entero, muestra un error
     y vuelve a pedir.
   - Devuelve el entero válido.

2. Función 'dividir_seguro(a, b)':
   - Intenta dividir a / b.
   - Captura ZeroDivisionError si b es 0.
   - Captura TypeError si a o b no son numéricos.
   - Devuelve el resultado o None si hubo error.

3. Función 'acceder_lista_seguro(lista, indice)':
   - Intenta acceder a lista[indice].
   - Captura IndexError si el índice no existe.
   - Devuelve el elemento o un mensaje de error.

4. En la sección principal del script:
   - Usa pedir_entero() para pedir dos números.
   - Usa dividir_seguro() para dividirlos.
   - Crea una lista pequeña y usa acceder_lista_seguro() con un índice válido
     y otro inválido.

✅ CRITERIOS DE ACEPTACIÓN:
- Se usan bloques try/except en las 3 funciones.
- Se capturan excepciones ESPECÍFICAS (no un except genérico).
- pedir_entero() usa un while True para re-pedir si hay error.
- dividir_seguro() maneja ZeroDivisionError y TypeError.
- acceder_lista_seguro() maneja IndexError.
- Se demuestra el funcionamiento con llamadas de prueba.
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# def pedir_entero(mensaje):
#     """Pide un entero al usuario de forma segura."""
#     while True:
#         try:
#             valor = int(input(mensaje))
#             return valor
#         except ValueError:
#             print("❌ Error: Por favor ingresa un número entero válido.")
#
#
# def dividir_seguro(a, b):
#     """Divide a / b de forma segura."""
#     try:
#         resultado = a / b
#         return resultado
#     except ZeroDivisionError:
#         print("❌ Error: No se puede dividir entre cero.")
#         return None
#     except TypeError:
#         print("❌ Error: Ambos valores deben ser numéricos.")
#         return None
#
#
# def acceder_lista_seguro(lista, indice):
#     """Accede a un elemento de la lista de forma segura."""
#     try:
#         elemento = lista[indice]
#         return elemento
#     except IndexError:
#         print(f"❌ Error: El índice {indice} no existe. La lista tiene {len(lista)} elementos (0-{len(lista)-1}).")
#         return None
#
#
# # === Sección principal ===
# print("=== MANEJO DE ERRORES ===\n")
#
# # Probar pedir_entero
# num1 = pedir_entero("Ingresa el primer número: ")
# num2 = pedir_entero("Ingresa el segundo número: ")
#
# # Probar dividir_seguro
# print(f"\nDividiendo {num1} / {num2}...")
# resultado = dividir_seguro(num1, num2)
# if resultado is not None:
#     print(f"✅ Resultado: {resultado:.2f}")
#
# # Probar acceder_lista_seguro
# colores = ["rojo", "verde", "azul"]
# print(f"\nLista de colores: {colores}")
#
# elemento = acceder_lista_seguro(colores, 1)
# print(f"Elemento en índice 1: {elemento}")
#
# elemento = acceder_lista_seguro(colores, 10)
# print(f"Elemento en índice 10: {elemento}")
