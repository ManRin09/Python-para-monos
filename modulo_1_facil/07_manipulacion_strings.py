"""
========================================
🐒 Python para Monos
Módulo 1 — Actividad 07: Manipulación de Strings
========================================

📚 TEORÍA:

Los STRINGS (cadenas de texto) en Python son secuencias inmutables de caracteres.
Esto significa que una vez creado un string, no puedes cambiar sus caracteres
individuales; pero sí puedes crear un NUEVO string transformado.

Python incluye una gran cantidad de MÉTODOS incorporados para manipular strings.
Un método se llama con la sintaxis:  string.metodo()

MÉTODOS DE CAMBIO DE CASO:
    texto = "Hola Mundo"
    texto.upper()      →  "HOLA MUNDO"     # Todo a mayúsculas
    texto.lower()      →  "hola mundo"     # Todo a minúsculas
    texto.capitalize() →  "Hola mundo"     # Primera letra mayúscula, resto minúscula
    texto.title()      →  "Hola Mundo"     # Primera letra de cada palabra en mayúscula
    texto.swapcase()   →  "hOLA mUNDO"    # Invierte mayúsculas y minúsculas

MÉTODOS DE LIMPIEZA:
    texto = "   Hola Mundo   "
    texto.strip()      →  "Hola Mundo"     # Elimina espacios al inicio y al final
    texto.lstrip()     →  "Hola Mundo   "  # Elimina espacios solo al inicio (left)
    texto.rstrip()     →  "   Hola Mundo"  # Elimina espacios solo al final (right)

    ¿Por qué importa strip()? Porque cuando un usuario escribe en input(),
    a veces agrega espacios sin querer: "  Carlos  " → strip() → "Carlos"

MÉTODOS DE BÚSQUEDA Y REEMPLAZO:
    texto = "Python es genial, Python es poderoso"
    texto.replace("Python", "Java")  →  "Java es genial, Java es poderoso"
    texto.find("genial")             →  10   (índice donde empieza "genial")
    texto.find("Ruby")              →  -1   (no lo encontró)
    texto.count("Python")           →  2    (aparece 2 veces)

MÉTODOS DE VERIFICACIÓN (devuelven True o False):
    "123".isdigit()      →  True    # ¿Solo contiene dígitos?
    "Hola".isalpha()     →  True    # ¿Solo contiene letras?
    "hola".islower()     →  True    # ¿Está todo en minúsculas?
    "HOLA".isupper()     →  True    # ¿Está todo en mayúsculas?
    "  ".isspace()       →  True    # ¿Solo contiene espacios?

MÉTODOS DE SEPARACIÓN Y UNIÓN:
    texto = "uno,dos,tres,cuatro"
    texto.split(",")     →  ["uno", "dos", "tres", "cuatro"]  # Divide en lista

    lista = ["uno", "dos", "tres"]
    " - ".join(lista)    →  "uno - dos - tres"  # Une lista en string

SLICING (REBANADO):
Permite extraer partes de un string usando índices [inicio:fin:paso]:
    texto = "Python"
    texto[0]       →  "P"        # Primer carácter (índice 0)
    texto[-1]      →  "n"        # Último carácter
    texto[0:3]     →  "Pyt"      # Desde índice 0 hasta 2 (fin no incluido)
    texto[2:]      →  "thon"     # Desde índice 2 hasta el final
    texto[::-1]    →  "nohtyP"   # String invertido

LONGITUD:
    len("Python")  →  6

📝 INSTRUCCIONES:

Crea un script que haga lo siguiente:
1. Declara una variable con el texto: "  hOLa, bIeNvEnIdO aL cUrSo De PyThOn  "
2. Aplica las siguientes transformaciones EN ORDEN, guardando cada resultado
   en una variable nueva e imprimiendo cada paso:
   a) Eliminar espacios sobrantes al inicio y al final (strip).
   b) Convertir todo el texto a minúsculas (lower).
   c) Reemplazar "python" por "programación" (replace).
   d) Convertir a formato título — primera letra de cada palabra en mayúscula (title).
   e) Contar cuántas veces aparece la letra "a" en el resultado final.
   f) Mostrar el texto invertido usando slicing.
3. Imprime la longitud del texto final.

✅ CRITERIOS DE ACEPTACIÓN:
- Se deben usar al menos estos métodos: strip(), lower(), replace(), title().
- Cada transformación se guarda en una variable nueva y se imprime.
- Se debe contar las apariciones de un carácter usando count().
- Se debe mostrar el texto invertido con slicing [::-1].
- Se debe mostrar la longitud con len().
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# texto_original = "  hOLa, bIeNvEnIdO aL cUrSo De PyThOn  "
# print(f"Original: '{texto_original}'")
#
# # a) Strip
# paso_a = texto_original.strip()
# print(f"a) Strip: '{paso_a}'")
#
# # b) Lower
# paso_b = paso_a.lower()
# print(f"b) Lower: '{paso_b}'")
#
# # c) Replace
# paso_c = paso_b.replace("python", "programación")
# print(f"c) Replace: '{paso_c}'")
#
# # d) Title
# paso_d = paso_c.title()
# print(f"d) Title: '{paso_d}'")
#
# # e) Count
# conteo_a = paso_d.lower().count("a")
# print(f"e) La letra 'a' aparece {conteo_a} veces")
#
# # f) Invertir
# invertido = paso_d[::-1]
# print(f"f) Invertido: '{invertido}'")
#
# # Longitud
# print(f"\nLongitud del texto final: {len(paso_d)} caracteres")
