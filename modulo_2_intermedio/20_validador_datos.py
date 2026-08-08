"""
========================================
🐒 Python para Monos
Módulo 2 — Actividad 20: Validador de Datos
========================================

📚 TEORÍA:

En el mundo real, los datos que recibes (de usuarios, archivos, APIs) rara
vez están "limpios". Pueden tener espacios extra, valores vacíos, tipos
incorrectos, o valores fuera de rango. Un VALIDADOR DE DATOS es una colección
de funciones que verifican y limpian datos antes de usarlos.

VALIDACIONES COMUNES:

1. VALOR VACÍO:
    def esta_vacio(valor):
        if valor is None:
            return True
        if isinstance(valor, str) and valor.strip() == "":
            return True
        return False

    isinstance(valor, str) verifica si 'valor' es de tipo string.

2. TIPO DE DATO:
    def es_numerico(valor):
        \"\"\"Verifica si un string puede convertirse a número.\"\"\"
        try:
            float(valor)
            return True
        except (ValueError, TypeError):
            return False

    es_numerico("123")    →  True
    es_numerico("12.5")   →  True
    es_numerico("hola")   →  False
    es_numerico("")       →  False

3. RANGO DE VALORES:
    def en_rango(valor, minimo, maximo):
        return minimo <= valor <= maximo

    en_rango(25, 0, 100)   →  True
    en_rango(150, 0, 100)  →  False

4. LIMPIEZA DE STRINGS:
    def limpiar_texto(texto):
        if not isinstance(texto, str):
            return str(texto)
        return texto.strip().title()

    limpiar_texto("  carlos MÉNDEZ  ")  →  "Carlos Méndez"

5. CONVERSIÓN SEGURA:
    def convertir_a_float(valor):
        try:
            return float(valor)
        except (ValueError, TypeError):
            return 0.0

PATRÓN — Pipeline de validación:
Encadenas varias funciones de validación para limpiar un dato paso a paso:

    dato_crudo = "  45.5  "
    # 1. Verificar que no está vacío
    # 2. Limpiar (strip)
    # 3. Verificar que es numérico
    # 4. Convertir a float
    # 5. Verificar que está en rango

FILOSOFÍA: "Nunca confíes en los datos de entrada".
Siempre valida y limpia ANTES de procesar. Es mejor rechazar un dato malo
que dejar que provoque un error más adelante.

📝 INSTRUCCIONES:

Crea un módulo de funciones de validación y luego pruébalas:

1. Función 'validar_no_vacio(valor)':
   - Devuelve True si el valor no es None, no es "" y no es solo espacios.
   - Devuelve False en caso contrario.

2. Función 'validar_numerico(valor)':
   - Devuelve True si el valor (string) se puede convertir a float.
   - Devuelve False si no.

3. Función 'validar_rango(valor, minimo, maximo)':
   - Devuelve True si el valor numérico está entre minimo y maximo (inclusive).
   - Devuelve False si no.

4. Función 'limpiar_texto(texto)':
   - Elimina espacios al inicio y al final.
   - Convierte a formato título (primera letra de cada palabra en mayúscula).
   - Devuelve el texto limpio.

5. Función 'convertir_a_numero(valor, tipo="float")':
   - Intenta convertir el valor a float o int según el parámetro 'tipo'.
   - Si falla, devuelve 0 (o 0.0).

6. Función 'validar_registro(registro)':
   - Recibe un diccionario con claves "nombre", "edad", "email".
   - Valida cada campo usando las funciones anteriores.
   - Devuelve un diccionario con los datos limpios o un diccionario de errores.

7. En la sección principal, crea una lista de registros (algunos válidos,
   algunos con errores) y procesa cada uno mostrando si pasó o falló.

✅ CRITERIOS DE ACEPTACIÓN:
- Se crean al menos 5 funciones de validación independientes.
- Cada función tiene una responsabilidad única y clara.
- Se usa try/except para validar conversiones numéricas.
- Se demuestra validar_registro() con datos buenos y datos malos.
- Las funciones se prueban con múltiples casos de prueba.
- Se imprimen mensajes claros indicando qué validaciones pasan y cuáles fallan.
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# # --- Funciones de validación ---
#
# def validar_no_vacio(valor):
#     """Verifica que el valor no sea vacío, None, o solo espacios."""
#     if valor is None:
#         return False
#     if isinstance(valor, str) and valor.strip() == "":
#         return False
#     return True
#
#
# def validar_numerico(valor):
#     """Verifica si un valor se puede convertir a número."""
#     try:
#         float(str(valor))
#         return True
#     except (ValueError, TypeError):
#         return False
#
#
# def validar_rango(valor, minimo, maximo):
#     """Verifica que un valor numérico esté dentro de un rango."""
#     return minimo <= valor <= maximo
#
#
# def limpiar_texto(texto):
#     """Limpia un texto: quita espacios y aplica formato título."""
#     if not isinstance(texto, str):
#         return str(texto).strip()
#     return texto.strip().title()
#
#
# def convertir_a_numero(valor, tipo="float"):
#     """Convierte un valor a float o int de forma segura."""
#     try:
#         if tipo == "int":
#             return int(float(str(valor)))
#         return float(str(valor))
#     except (ValueError, TypeError):
#         return 0.0 if tipo == "float" else 0
#
#
# def validar_registro(registro):
#     """Valida un registro completo y devuelve datos limpios o errores."""
#     errores = []
#     datos_limpios = {}
#
#     # Validar nombre
#     if not validar_no_vacio(registro.get("nombre")):
#         errores.append("El nombre no puede estar vacío")
#     else:
#         datos_limpios["nombre"] = limpiar_texto(registro["nombre"])
#
#     # Validar edad
#     edad_raw = registro.get("edad")
#     if not validar_numerico(edad_raw):
#         errores.append(f"La edad '{edad_raw}' no es un número válido")
#     else:
#         edad = convertir_a_numero(edad_raw, "int")
#         if not validar_rango(edad, 0, 150):
#             errores.append(f"La edad {edad} está fuera del rango válido (0-150)")
#         else:
#             datos_limpios["edad"] = edad
#
#     # Validar email
#     if not validar_no_vacio(registro.get("email")):
#         errores.append("El email no puede estar vacío")
#     else:
#         email = registro["email"].strip().lower()
#         if "@" not in email:
#             errores.append(f"El email '{email}' no contiene @")
#         else:
#             datos_limpios["email"] = email
#
#     if len(errores) > 0:
#         return {"valido": False, "errores": errores}
#     return {"valido": True, "datos": datos_limpios}
#
#
# # --- Sección principal: Pruebas ---
# registros = [
#     {"nombre": "  carlos méndez  ", "edad": "28", "email": "Carlos@Email.COM"},
#     {"nombre": "", "edad": "25", "email": "ana@email.com"},
#     {"nombre": "María García", "edad": "abc", "email": "maria@email.com"},
#     {"nombre": "Juan Pérez", "edad": "200", "email": "juan@email.com"},
#     {"nombre": "Sofía Herrera", "edad": "30", "email": "sofi-sin-arroba"},
#     {"nombre": "  pedro castillo  ", "edad": "45", "email": "  Pedro@Test.Com  "},
# ]
#
# print("=== VALIDADOR DE REGISTROS ===\n")
# for i, reg in enumerate(registros, start=1):
#     resultado = validar_registro(reg)
#     print(f"Registro #{i}: {reg}")
#     if resultado["valido"]:
#         print(f"  ✅ VÁLIDO → {resultado['datos']}")
#     else:
#         print(f"  ❌ INVÁLIDO:")
#         for error in resultado["errores"]:
#             print(f"     - {error}")
#     print()
