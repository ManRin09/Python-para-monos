"""
========================================
🐒 Python para Monos
🚀 Proyecto Final — Archivo 2 de 3: archivos.py
   (Módulo de Persistencia — Lectura/Escritura CSV)
========================================

📚 TEORÍA:

La PERSISTENCIA es la capacidad de un programa de guardar datos de forma
que sobrevivan después de cerrar la aplicación. Sin persistencia, todos
los datos que el usuario ingresa se pierden al salir del programa.

En este proyecto usamos archivos CSV (Comma-Separated Values) como
mecanismo de persistencia. Es una solución simple, legible y portable
que no requiere instalar bases de datos.

FLUJO DE PERSISTENCIA:

    [Programa en memoria]  ──guardar──>  [Archivo CSV en disco]
    [Archivo CSV en disco] ──cargar──>   [Programa en memoria]

GUARDAR (Serialización):
Convertir los datos en memoria (lista de diccionarios) a un formato
de texto plano (CSV) y escribirlo en disco.

    inventario (memoria)  →  csv.DictWriter  →  inventario.csv (disco)

    Ejemplo de salida en el archivo:
        nombre,precio,cantidad
        Laptop Dell,2500000.00,5
        Mouse Logitech,85000.50,20

CARGAR (Deserialización):
Leer el archivo CSV del disco, validar cada fila, y reconstruir la
lista de diccionarios en memoria.

    inventario.csv (disco)  →  csv.reader  →  inventario (memoria)

POLÍTICA DE CARGA (SOBRESCRIBIR vs FUSIONAR):
Cuando el usuario carga un CSV y ya tiene datos en memoria, debe
decidir qué hacer:

    SOBRESCRIBIR (S): Borrar el inventario actual y reemplazarlo
    completamente con los datos del archivo. Es un "reset" total.

    FUSIONAR (N): Combinar los datos del archivo con el inventario
    actual. Si un producto ya existe:
      → Se SUMAN las cantidades.
      → Se ACTUALIZA el precio al nuevo (del archivo).
    Si el producto es nuevo, se agrega.

VALIDACIÓN DE DATOS AL CARGAR:
Los archivos pueden estar corruptos, tener formatos incorrectos, o
haber sido editados manualmente con errores. Por eso, cada fila del
CSV se valida antes de ser aceptada:
    - ¿Tiene exactamente 3 columnas?
    - ¿El nombre no está vacío?
    - ¿El precio se puede convertir a float y es > 0?
    - ¿La cantidad se puede convertir a int y es >= 0?
Las filas que no cumplan se OMITEN silenciosamente y se cuentan
para un reporte final al usuario.

MANEJO DE ERRORES (try/except):
Las operaciones con archivos pueden fallar por muchas razones:
    - FileNotFoundError: El archivo no existe.
    - PermissionError: No tienes permisos para leer/escribir.
    - UnicodeDecodeError: El archivo no está en formato UTF-8.
    - ValueError: Los datos no se pueden convertir al tipo esperado.
    - OSError: Problemas del sistema operativo (disco lleno, etc.).

Cada uno de estos errores se captura con try/except para que el
programa NUNCA se caiga — solo informa al usuario del problema.

📝 INSTRUCCIONES:

Este módulo implementa 2 funciones públicas y 1 función auxiliar interna:

1. guardar_csv(inventario, ruta, incluir_header=True)
   → Valida que el inventario no esté vacío antes de guardar.
   → Crea el directorio destino si no existe (os.makedirs).
   → Escribe el CSV usando csv.DictWriter con campos: nombre,precio,cantidad.
   → Maneja PermissionError y OSError con try/except.
   → Imprime mensaje de éxito con la ruta y tamaño del archivo.
   → Retorna True si se guardó, False si hubo error.

2. cargar_csv(ruta, inventario_actual)
   → Verifica que el archivo exista (os.path.exists).
   → Lee el archivo con csv.reader, detectando automáticamente si la
     primera fila es encabezado ("nombre") y omitiéndola.
   → Valida cada fila con _validar_fila() — las inválidas se omiten.
   → Muestra un resumen de lectura (productos válidos + filas omitidas).
   → Si el inventario actual tiene datos, pregunta la política:
     "S" = Sobrescribir | "N" = Fusionar.
   → Al fusionar: si el producto ya existe, SUMA la cantidad y
     ACTUALIZA el precio al nuevo.
   → Muestra un reporte final con productos nuevos y actualizados.
   → Retorna True si se cargó al menos un producto.

3. _validar_fila(fila, numero_fila) [función interna]
   → Verifica: 3 columnas, nombre no vacío, precio>0, cantidad>=0.
   → Retorna el diccionario del producto si es válida, None si no.

✅ CRITERIOS DE ACEPTACIÓN:
- Se usa csv.DictWriter para guardar y csv.reader para cargar.
- Se valida que el inventario no esté vacío antes de guardar.
- Se valida que el archivo exista antes de intentar cargarlo.
- Cada fila del CSV se valida (3 columnas, tipos correctos, rangos válidos).
- Las filas inválidas se OMITEN y se cuentan (no rompen el programa).
- Se implementa la política Sobrescribir/Fusionar al cargar.
- Al fusionar, los productos existentes SUMAN cantidad y ACTUALIZAN precio.
- Se manejan FileNotFoundError, PermissionError, UnicodeDecodeError y ValueError.
- Se usa encoding="utf-8" y newline="" en todas las operaciones de archivo.
- Todo el código es 100% procedimental (cero clases, cero self, cero objetos propios).
========================================
"""

import csv
import os

# Importar la función buscar_producto del módulo de servicios
from servicios import buscar_producto


# ============================================================
# FUNCIÓN: GUARDAR INVENTARIO EN CSV
# ============================================================

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario completo en un archivo CSV.

    Valida que el inventario no esté vacío antes de intentar guardar.
    Maneja errores de permisos y escritura con try/except.
    Crea el directorio destino si no existe.

    Formato de salida:
        nombre,precio,cantidad

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.
        ruta (str): Ruta del archivo CSV de destino.
        incluir_header (bool): Si True, escribe la fila de encabezados.
                               Por defecto es True.

    Retorna:
        bool: True si se guardó exitosamente, False si hubo error.
    """
    # Validar que el inventario no esté vacío
    if len(inventario) == 0:
        print("  ⚠️  El inventario está vacío. No hay nada que guardar.")
        return False

    # Validar que la ruta no esté vacía
    if not ruta or ruta.strip() == "":
        print("  ❌ Error: La ruta del archivo no puede estar vacía.")
        return False

    try:
        # Crear directorio si no existe
        directorio = os.path.dirname(ruta)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)

        # Escribir el archivo CSV
        campos = ["nombre", "precio", "cantidad"]

        with open(ruta, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)

            if incluir_header:
                escritor.writeheader()

            escritor.writerows(inventario)

        # Mensaje de éxito con estadísticas
        tamano = os.path.getsize(ruta)
        print(f"\n  ✅ Inventario guardado exitosamente.")
        print(f"      📁 Archivo: {ruta}")
        print(f"      📊 Productos: {len(inventario)}")
        print(f"      💾 Tamaño: {tamano:,} bytes")
        return True

    except PermissionError:
        print(f"  ❌ Error de permisos: No se puede escribir en '{ruta}'.")
        print("      Verifica que tengas permisos de escritura en esa ubicación.")
        return False

    except OSError as e:
        print(f"  ❌ Error del sistema al guardar: {e}")
        return False

    except Exception as e:
        print(f"  ❌ Error inesperado al guardar: {e}")
        return False


# ============================================================
# FUNCIÓN: CARGAR INVENTARIO DESDE CSV
# ============================================================

def cargar_csv(ruta, inventario_actual):
    """
    Carga productos desde un archivo CSV al inventario.

    Proceso de carga:
    1. Verifica que el archivo exista.
    2. Lee cada fila validando:
       - Que tenga exactamente 3 columnas.
       - Que el precio sea un float positivo (> 0).
       - Que la cantidad sea un int no negativo (>= 0).
       - Que el nombre no esté vacío.
    3. Las filas que no cumplan se OMITEN y se cuentan como errores.
    4. Pregunta al usuario la POLÍTICA de carga:
       - "S" = SOBRESCRIBIR: Vaciar el inventario actual y reemplazarlo.
       - "N" = FUSIONAR: Agregar los nuevos productos. Si un producto ya
               existe, SUMA la cantidad y ACTUALIZA el precio al nuevo.
    5. Muestra un reporte final con estadísticas de la operación.

    Parámetros:
        ruta (str): Ruta del archivo CSV a cargar.
        inventario_actual (list): Referencia a la lista del inventario en memoria.

    Retorna:
        bool: True si se cargó al menos un producto, False si hubo error total.
    """
    # Validar que la ruta no esté vacía
    if not ruta or ruta.strip() == "":
        print("  ❌ Error: La ruta del archivo no puede estar vacía.")
        return False

    # --- PASO 1: Verificar que el archivo existe ---
    if not os.path.exists(ruta):
        print(f"  ❌ Error: El archivo '{ruta}' no existe.")
        print("      Verifica la ruta e intenta de nuevo.")
        return False

    # --- PASO 2: Leer y validar el archivo ---
    productos_leidos = []
    filas_omitidas = 0
    errores_detalle = []
    numero_fila = 0

    try:
        with open(ruta, "r", encoding="utf-8", newline="") as archivo:
            lector = csv.reader(archivo)

            # Intentar detectar si la primera fila es un encabezado
            primera_fila = next(lector, None)
            if primera_fila is None:
                print("  ⚠️  El archivo está vacío.")
                return False

            numero_fila = 1

            # Verificar si la primera fila es encabezado o datos
            es_encabezado = False
            if len(primera_fila) >= 1:
                # Si el primer campo es exactamente "nombre" (case-insensitive),
                # lo tratamos como encabezado
                if primera_fila[0].strip().lower() == "nombre":
                    es_encabezado = True

            # Si no es encabezado, procesarla como datos
            if not es_encabezado:
                resultado = _validar_fila(primera_fila, numero_fila)
                if resultado is not None:
                    productos_leidos.append(resultado)
                else:
                    filas_omitidas += 1
                    errores_detalle.append(f"Fila {numero_fila}: formato inválido")

            # Procesar el resto de filas
            for fila in lector:
                numero_fila += 1
                resultado = _validar_fila(fila, numero_fila)
                if resultado is not None:
                    productos_leidos.append(resultado)
                else:
                    filas_omitidas += 1
                    errores_detalle.append(f"Fila {numero_fila}: formato inválido")

    except PermissionError:
        print(f"  ❌ Error de permisos: No se puede leer '{ruta}'.")
        return False

    except UnicodeDecodeError:
        print(f"  ❌ Error de codificación: El archivo no está en formato UTF-8.")
        return False

    except Exception as e:
        print(f"  ❌ Error inesperado al leer: {e}")
        return False

    # --- Verificar que se leyeron productos ---
    if len(productos_leidos) == 0:
        print("  ⚠️  No se encontraron productos válidos en el archivo.")
        if filas_omitidas > 0:
            print(f"      Se omitieron {filas_omitidas} fila(s) por errores de formato.")
        return False

    # --- Mostrar resumen de lectura ---
    print(f"\n  📂 Archivo leído: {ruta}")
    print(f"      ✅ Productos válidos: {len(productos_leidos)}")
    if filas_omitidas > 0:
        print(f"      ⚠️  Filas omitidas:    {filas_omitidas}")
        for detalle in errores_detalle:
            print(f"         • {detalle}")

    # --- PASO 3: Preguntar política de carga ---
    print()
    if len(inventario_actual) > 0:
        print(f"  ℹ️  El inventario actual tiene {len(inventario_actual)} producto(s).")
        print("  ¿Desea SOBRESCRIBIR el inventario actual o FUSIONAR con los nuevos datos?")
        print("      S = Sobrescribir (reemplazar todo)")
        print("      N = Fusionar (agregar/actualizar)")

        politica = input("\n  Elija (S/N): ").strip().upper()
    else:
        politica = "S"  # Si está vacío, directamente sobrescribir

    # --- PASO 4: Aplicar la política ---
    productos_nuevos = 0
    productos_actualizados = 0

    if politica == "S":
        # SOBRESCRIBIR: Vaciar y reemplazar
        inventario_actual.clear()
        for producto in productos_leidos:
            inventario_actual.append(producto)
            productos_nuevos += 1
        print(f"\n  🔄 Inventario SOBRESCRITO con {productos_nuevos} producto(s).")

    else:
        # FUSIONAR: Agregar nuevos y actualizar existentes
        for producto_nuevo in productos_leidos:
            existente = buscar_producto(inventario_actual, producto_nuevo["nombre"])

            if existente is not None:
                # Producto ya existe: sumar cantidad y actualizar precio
                cantidad_anterior = existente["cantidad"]
                existente["cantidad"] += producto_nuevo["cantidad"]

                if existente["precio"] != producto_nuevo["precio"]:
                    existente["precio"] = producto_nuevo["precio"]

                productos_actualizados += 1
            else:
                # Producto nuevo: agregar
                inventario_actual.append(producto_nuevo)
                productos_nuevos += 1

        print(f"\n  🔀 Inventario FUSIONADO:")
        print(f"      ➕ Productos nuevos:       {productos_nuevos}")
        print(f"      🔄 Productos actualizados: {productos_actualizados}")

    # --- PASO 5: Reporte final ---
    print(f"\n  📊 Estado final del inventario: {len(inventario_actual)} producto(s).")
    return True


# ============================================================
# FUNCIONES AUXILIARES (internas)
# ============================================================

def _validar_fila(fila, numero_fila):
    """
    Valida una fila del CSV y la convierte a diccionario.

    Verifica:
    - Exactamente 3 columnas.
    - Nombre no vacío.
    - Precio convertible a float y mayor que 0.
    - Cantidad convertible a int y mayor o igual a 0.

    Parámetros:
        fila (list): Lista de strings con los campos de la fila.
        numero_fila (int): Número de fila para reportar errores.

    Retorna:
        dict o None: Diccionario del producto si es válida, None si no.
    """
    # Verificar que tenga exactamente 3 columnas
    if len(fila) != 3:
        return None

    nombre = fila[0].strip()
    precio_raw = fila[1].strip()
    cantidad_raw = fila[2].strip()

    # Validar nombre no vacío
    if nombre == "":
        return None

    # Validar y convertir precio
    try:
        precio = float(precio_raw)
        if precio <= 0:
            return None
    except ValueError:
        return None

    # Validar y convertir cantidad
    try:
        cantidad = int(float(cantidad_raw))  # int(float()) para manejar "5.0"
        if cantidad < 0:
            return None
    except ValueError:
        return None

    return {
        "nombre": nombre.title(),
        "precio": round(precio, 2),
        "cantidad": cantidad
    }
