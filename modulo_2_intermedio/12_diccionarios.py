"""
========================================
🐒 Python para Monos
Módulo 2 — Actividad 12: Diccionarios
========================================

📚 TEORÍA:

Un DICCIONARIO es una colección de datos que almacena información en pares
CLAVE-VALOR. A diferencia de las listas (que usan índices numéricos), los
diccionarios usan claves descriptivas para acceder a los valores.

CREAR UN DICCIONARIO:
    persona = {
        "nombre": "Carlos",
        "edad": 28,
        "ciudad": "Bogotá",
        "es_estudiante": True
    }

    También puedes crear uno vacío:
    datos = {}

ACCEDER A VALORES:
    persona["nombre"]      →  "Carlos"
    persona["edad"]        →  28

    ⚠️ Si la clave no existe, lanza un KeyError.
    Para evitar el error, usa .get():
    persona.get("telefono")         →  None (no lanza error)
    persona.get("telefono", "N/A")  →  "N/A" (valor por defecto)

AGREGAR O MODIFICAR VALORES:
    persona["telefono"] = "3001234567"  # Agrega nueva clave
    persona["edad"] = 29                # Modifica valor existente

ELIMINAR CLAVES:
    del persona["es_estudiante"]          # Elimina la clave
    valor = persona.pop("ciudad")         # Elimina y devuelve el valor
    persona.pop("inexistente", "default") # No lanza error si no existe

MÉTODOS IMPORTANTES:
    persona.keys()    →  dict_keys(["nombre", "edad", ...])   # Todas las claves
    persona.values()  →  dict_values(["Carlos", 28, ...])     # Todos los valores
    persona.items()   →  dict_items([("nombre","Carlos"), ("edad",28), ...])

ITERAR SOBRE UN DICCIONARIO:

    # Solo claves (comportamiento por defecto)
    for clave in persona:
        print(clave)

    # Claves y valores
    for clave, valor in persona.items():
        print(f"{clave}: {valor}")

    # Solo valores
    for valor in persona.values():
        print(valor)

VERIFICAR SI UNA CLAVE EXISTE:
    if "nombre" in persona:
        print("La clave 'nombre' existe")

COPIAR UN DICCIONARIO:
    copia = persona.copy()

DIFERENCIA CLAVE: LISTA vs DICCIONARIO
    Lista:        datos[0], datos[1], datos[2]       ← Acceso por posición
    Diccionario:  datos["nombre"], datos["edad"]     ← Acceso por nombre

📝 INSTRUCCIONES:

Crea un script que administre un directorio de contactos usando diccionarios:

1. Crea un diccionario llamado 'contacto_1' con las claves:
   "nombre", "telefono", "email", "ciudad"
   (llénalo con datos inventados).

2. Crea un segundo diccionario 'contacto_2' de la misma forma.

3. Imprime TODOS los datos de contacto_1 usando un ciclo for con .items().

4. Agrega una nueva clave "ocupacion" a contacto_1.

5. Modifica el teléfono de contacto_2.

6. Intenta acceder a una clave inexistente usando .get() con un valor por defecto.

7. Elimina la clave "ciudad" de contacto_2 usando .pop() y guarda el valor
   eliminado. Imprime qué ciudad fue eliminada.

8. Imprime SOLO las claves de contacto_1 y SOLO los valores de contacto_2.

✅ CRITERIOS DE ACEPTACIÓN:
- Se crean al menos 2 diccionarios con al menos 4 pares clave-valor cada uno.
- Se usa .items() para iterar e imprimir todos los datos.
- Se demuestra agregar y modificar valores.
- Se usa .get() con valor por defecto para acceder a una clave inexistente.
- Se usa .pop() para eliminar una clave.
- Se usan .keys() y .values() para imprimir claves y valores por separado.
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# # 1. Crear contacto_1
# contacto_1 = {
#     "nombre": "Ana López",
#     "telefono": "3001112233",
#     "email": "ana.lopez@email.com",
#     "ciudad": "Bogotá"
# }
#
# # 2. Crear contacto_2
# contacto_2 = {
#     "nombre": "Pedro Castillo",
#     "telefono": "3109998877",
#     "email": "pedro.castillo@email.com",
#     "ciudad": "Medellín"
# }
#
# # 3. Imprimir todos los datos de contacto_1
# print("=== CONTACTO 1 ===")
# for clave, valor in contacto_1.items():
#     print(f"  {clave}: {valor}")
#
# # 4. Agregar ocupación
# contacto_1["ocupacion"] = "Ingeniera de Software"
# print(f"\n✅ Ocupación agregada a contacto_1: {contacto_1['ocupacion']}")
#
# # 5. Modificar teléfono
# contacto_2["telefono"] = "3205554433"
# print(f"✅ Teléfono de contacto_2 actualizado: {contacto_2['telefono']}")
#
# # 6. Acceder a clave inexistente con .get()
# instagram = contacto_1.get("instagram", "No registrado")
# print(f"\nInstagram de contacto_1: {instagram}")
#
# # 7. Eliminar ciudad de contacto_2
# ciudad_eliminada = contacto_2.pop("ciudad")
# print(f"Ciudad eliminada de contacto_2: {ciudad_eliminada}")
#
# # 8. Claves de contacto_1 y valores de contacto_2
# print(f"\n📋 Claves de contacto_1: {list(contacto_1.keys())}")
# print(f"📋 Valores de contacto_2: {list(contacto_2.values())}")
