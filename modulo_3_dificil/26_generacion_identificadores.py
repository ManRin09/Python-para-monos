"""
========================================
🐒 Python para Monos
Módulo 3 — Actividad 26: Generación de Identificadores Únicos
========================================

📚 TEORÍA:

En muchos sistemas, cada registro necesita un IDENTIFICADOR ÚNICO (ID) que
lo distinga de todos los demás. Piensa en números de documento, códigos de
pedido, números de ticket, etc.

Hay varias estrategias para generar IDs:

ESTRATEGIA 1 — Contador secuencial:
    Simple pero limitado. Solo funciona si tienes control total del sistema.
    id_actual = 0
    def generar_id_secuencial():
        global id_actual     # ⚠️ Usamos global solo como ejemplo
        id_actual += 1
        return id_actual

ESTRATEGIA 2 — Fecha + Número aleatorio:
    Combina la fecha actual con un número aleatorio para mayor unicidad.

    import random
    from datetime import datetime

    def generar_id_fecha():
        ahora = datetime.now()
        fecha = ahora.strftime("%Y%m%d")        # "20250808"
        hora = ahora.strftime("%H%M%S")          # "143045"
        aleatorio = random.randint(1000, 9999)    # 4 dígitos aleatorios
        return f"{fecha}-{hora}-{aleatorio}"
    # Resultado: "20250808-143045-7523"

ESTRATEGIA 3 — Prefijo + Fecha + Secuencia:
    Ideal para códigos legibles y descriptivos.

    def generar_codigo(prefijo, numero):
        ahora = datetime.now()
        fecha = ahora.strftime("%Y%m%d")
        secuencia = str(numero).zfill(4)  # Rellena con ceros: 1 → "0001"
        return f"{prefijo}-{fecha}-{secuencia}"
    # generar_codigo("ORD", 42) → "ORD-20250808-0042"

EL MÓDULO random:
    import random

    random.randint(1, 100)     →  Entero aleatorio entre 1 y 100 (inclusive)
    random.random()            →  Float aleatorio entre 0.0 y 1.0
    random.choice(["a","b","c"]) →  Elige un elemento aleatorio de la lista
    random.sample("ABCDEF", 3)  →  3 caracteres aleatorios sin repetir

    Para un código alfanumérico:
    import string
    caracteres = string.ascii_uppercase + string.digits  # "ABCDE...Z0123...9"
    codigo = ""
    for _ in range(8):
        codigo += random.choice(caracteres)
    # codigo → "X7K2M9PL"

str.zfill(ancho):
    Rellena un string con ceros a la izquierda hasta alcanzar el ancho:
    "42".zfill(6)    →  "000042"
    "7".zfill(4)     →  "0007"
    "123".zfill(3)   →  "123"  (ya tiene 3 dígitos)

📝 INSTRUCCIONES:

Crea un script con múltiples funciones generadoras de identificadores:

1. Función 'generar_id_simple(prefijo, numero)':
   - Combina un prefijo con un número rellenado con ceros a 5 dígitos.
   - Ejemplo: generar_id_simple("PROD", 7) → "PROD-00007"

2. Función 'generar_id_con_fecha(prefijo)':
   - Combina prefijo + fecha actual (YYYYMMDD) + 4 dígitos aleatorios.
   - Ejemplo: "DOC-20250808-4721"

3. Función 'generar_codigo_alfanumerico(longitud)':
   - Genera un código aleatorio de letras mayúsculas y dígitos.
   - Ejemplo: generar_codigo_alfanumerico(8) → "K7X2MP9L"

4. Función 'generar_lote_ids(prefijo, cantidad)':
   - Genera una LISTA de 'cantidad' IDs usando generar_id_con_fecha().
   - Devuelve la lista.

5. En la sección principal:
   - Demuestra cada función con ejemplos.
   - Genera un lote de 5 IDs y muéstralos.
   - Verifica que no haya duplicados en el lote generado.

✅ CRITERIOS DE ACEPTACIÓN:
- Se importa y usa el módulo random correctamente.
- Se importa y usa datetime para incluir fechas en los IDs.
- Se usa zfill() para rellenar con ceros.
- Se crean al menos 3 funciones generadoras diferentes.
- Se genera un lote y se verifica unicidad.
- Los IDs generados son legibles y tienen un formato consistente.
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# import random
# import string
# from datetime import datetime
#
#
# def generar_id_simple(prefijo, numero):
#     """Genera un ID simple: PREFIJO-00007"""
#     secuencia = str(numero).zfill(5)
#     return f"{prefijo}-{secuencia}"
#
#
# def generar_id_con_fecha(prefijo):
#     """Genera un ID con fecha: PREFIJO-YYYYMMDD-XXXX"""
#     ahora = datetime.now()
#     fecha = ahora.strftime("%Y%m%d")
#     aleatorio = random.randint(1000, 9999)
#     return f"{prefijo}-{fecha}-{aleatorio}"
#
#
# def generar_codigo_alfanumerico(longitud):
#     """Genera un código aleatorio de letras mayúsculas y dígitos."""
#     caracteres = string.ascii_uppercase + string.digits
#     codigo = ""
#     for _ in range(longitud):
#         codigo += random.choice(caracteres)
#     return codigo
#
#
# def generar_lote_ids(prefijo, cantidad):
#     """Genera un lote de IDs únicos."""
#     ids = []
#     for _ in range(cantidad):
#         nuevo_id = generar_id_con_fecha(prefijo)
#         ids.append(nuevo_id)
#     return ids
#
#
# # --- Sección principal ---
#
# # 1. ID Simple
# print("=== ID SIMPLE ===")
# for i in [1, 7, 42, 100, 9999]:
#     print(f"  {generar_id_simple('PROD', i)}")
#
# # 2. ID con fecha
# print("\n=== ID CON FECHA ===")
# for prefijo in ["DOC", "ORD", "TKT"]:
#     print(f"  {generar_id_con_fecha(prefijo)}")
#
# # 3. Código alfanumérico
# print("\n=== CÓDIGO ALFANUMÉRICO ===")
# for longitud in [6, 8, 12]:
#     print(f"  Longitud {longitud}: {generar_codigo_alfanumerico(longitud)}")
#
# # 4. Lote de IDs
# print("\n=== LOTE DE IDs ===")
# lote = generar_lote_ids("INV", 5)
# for i, id_generado in enumerate(lote, start=1):
#     print(f"  {i}. {id_generado}")
#
# # 5. Verificar unicidad
# print(f"\n🔍 Verificación de unicidad:")
# ids_unicos = []
# for id_gen in lote:
#     if id_gen in ids_unicos:
#         print(f"  ⚠️ DUPLICADO encontrado: {id_gen}")
#     else:
#         ids_unicos.append(id_gen)
#
# if len(ids_unicos) == len(lote):
#     print(f"  ✅ Todos los {len(lote)} IDs son únicos.")
# else:
#     print(f"  ❌ Se encontraron {len(lote) - len(ids_unicos)} duplicados.")
