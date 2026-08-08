"""
========================================
🐒 Python para Monos
Módulo 1 — Actividad 01: Variables y Tipos de Datos
========================================

📚 TEORÍA:

En Python, una VARIABLE es un nombre que le asignamos a un espacio en la memoria
del computador para guardar un dato. Piensa en ella como una caja etiquetada:
la etiqueta es el nombre de la variable y dentro de la caja está el valor.

Para crear una variable, simplemente escribes:
    nombre = valor

Python es un lenguaje de TIPADO DINÁMICO, lo que significa que no necesitas
declarar el tipo de dato de antemano. Python lo detecta automáticamente según
el valor que le asignes.

Los tipos de datos básicos (primitivos) en Python son:

1. int (entero): Números sin decimales.
   Ejemplo: edad = 25

2. float (flotante): Números con decimales.
   Ejemplo: estatura = 1.75

3. str (cadena de texto): Texto encerrado entre comillas simples o dobles.
   Ejemplo: nombre = "Carlos"

4. bool (booleano): Solo puede ser True (verdadero) o False (falso).
   Ejemplo: es_estudiante = True

Para verificar el tipo de una variable, usamos la función type():
    type(edad)  →  <class 'int'>

Para imprimir valores en la consola, usamos print():
    print(nombre)       →  Carlos
    print(type(edad))   →  <class 'int'>

REGLAS PARA NOMBRAR VARIABLES:
- Deben comenzar con una letra o guion bajo (_), nunca con un número.
- No pueden contener espacios (usa guion bajo: mi_variable).
- Son sensibles a mayúsculas/minúsculas (Edad ≠ edad).
- No pueden ser palabras reservadas de Python (if, for, while, etc.).
- Por convención en Python se usa snake_case: mi_nombre, precio_total.

📝 INSTRUCCIONES:

Crea un script que haga lo siguiente:
1. Declara una variable de tipo int llamada 'edad' con tu edad.
2. Declara una variable de tipo float llamada 'estatura' con tu estatura en metros.
3. Declara una variable de tipo str llamada 'nombre' con tu nombre completo.
4. Declara una variable de tipo bool llamada 'es_programador' con el valor True.
5. Imprime en consola cada variable junto con su tipo usando print() y type().
   El formato de salida debe ser:
   "Mi nombre es [nombre] y soy de tipo [tipo]"
   "Mi edad es [edad] y soy de tipo [tipo]"
   ... (para cada variable)

✅ CRITERIOS DE ACEPTACIÓN:
- El script debe declarar exactamente 4 variables, una de cada tipo básico.
- Cada variable debe tener un nombre descriptivo en snake_case.
- Se debe imprimir el VALOR y el TIPO de cada variable (usando type()).
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
# edad = 28
# estatura = 1.75
# nombre = "Carlos Méndez"
# es_programador = True
#
# print(f"Mi nombre es {nombre} y soy de tipo {type(nombre)}")
# print(f"Mi edad es {edad} y soy de tipo {type(edad)}")
# print(f"Mi estatura es {estatura} y soy de tipo {type(estatura)}")
# print(f"¿Soy programador? {es_programador} y soy de tipo {type(es_programador)}")
