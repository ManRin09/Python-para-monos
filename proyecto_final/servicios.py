"""
========================================
🐒 Python para Monos
🚀 Proyecto Final — Archivo 1 de 3: servicios.py
   (Módulo de Servicios — Lógica de Negocio CRUD)
========================================

📚 TEORÍA:

Este archivo es el CORAZÓN LÓGICO del sistema. Contiene todas las funciones
que operan directamente sobre los datos del inventario.

La estructura de datos central es una LISTA DE DICCIONARIOS:

    inventario = [
        {"nombre": "Laptop Dell", "precio": 2500000.00, "cantidad": 5},
        {"nombre": "Mouse Logitech", "precio": 85000.50, "cantidad": 20},
    ]

Cada diccionario representa un PRODUCTO con 3 campos:
    - "nombre" (str): Nombre descriptivo del producto (Title Case).
    - "precio" (float): Precio unitario del producto en pesos.
    - "cantidad" (int): Unidades disponibles en stock.

¿QUÉ ES CRUD?
CRUD es un acrónimo que describe las 4 operaciones básicas de cualquier
sistema que maneja datos:

    C = Create  (Crear)     → agregar_producto()
    R = Read    (Leer)      → mostrar_inventario(), buscar_producto()
    U = Update  (Actualizar) → actualizar_producto()
    D = Delete  (Eliminar)  → eliminar_producto()

Adicionalmente, este módulo incluye calcular_estadisticas(), que utiliza
una función LAMBDA para calcular el subtotal de cada producto:

    subtotal = lambda p: p["precio"] * p["cantidad"]

Una LAMBDA es una función anónima (sin nombre) de una sola línea.
Se usa cuando necesitas una función pequeña y no vale la pena definirla
con def. Su sintaxis es:

    lambda parametros: expresion

Equivale a:
    def mi_funcion(parametros):
        return expresion

PRINCIPIOS DE DISEÑO:
- Cada función tiene UNA sola responsabilidad.
- Las funciones reciben datos por PARÁMETROS (no usan variables globales).
- Las funciones devuelven resultados con RETURN.
- Las búsquedas son CASE-INSENSITIVE (no importan mayúsculas/minúsculas).
- Los datos se almacenan estandarizados (nombres en Title Case, precios
  redondeados a 2 decimales).

📝 INSTRUCCIONES:

Este módulo define las siguientes funciones, cada una documentada con
docstrings (qué hace, parámetros, retorno):

1. agregar_producto(inventario, nombre, precio, cantidad)
   → Verifica que el producto no exista (case-insensitive).
   → Si ya existe, informa al usuario y retorna False.
   → Si no existe, lo agrega como diccionario y retorna True.

2. mostrar_inventario(inventario)
   → Imprime una tabla formateada con ljust/rjust mostrando todos los
     productos, sus subtotales y los totales generales.
   → Si está vacío, muestra un mensaje informativo.

3. buscar_producto(inventario, nombre) → dict o None
   → Recorre la lista buscando por nombre (case-insensitive).
   → Retorna el diccionario del producto o None si no existe.

4. actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None)
   → Solo modifica los campos que se proporcionaron (no son None).
   → Muestra los valores antes y después del cambio.
   → Retorna True si se actualizó, False si no se encontró.

5. eliminar_producto(inventario, nombre)
   → Busca el producto, muestra sus datos y pide confirmación.
   → Lo remueve de la lista solo si el usuario confirma con "S".
   → Retorna True si se eliminó, False si se canceló o no existía.

6. calcular_estadisticas(inventario) → dict o None
   → Usa una lambda para calcular subtotales.
   → Retorna un diccionario con: total_productos, unidades_totales,
     valor_total, precio_promedio, producto_mas_caro (nombre + precio),
     producto_mayor_stock (nombre + cantidad), producto_mayor_valor
     (nombre + subtotal).

7. mostrar_estadisticas(estadisticas)
   → Muestra las estadísticas formateadas en consola.

8. mostrar_detalle_producto(producto)
   → Muestra los datos de un producto individual con formato legible.

✅ CRITERIOS DE ACEPTACIÓN:
- La estructura de datos central es una lista de diccionarios.
- Cada función tiene docstring con descripción, parámetros y retorno.
- Las búsquedas son case-insensitive (upper/lower no importan).
- agregar_producto() no permite duplicados.
- actualizar_producto() acepta actualizar solo precio, solo cantidad, o ambos.
- eliminar_producto() pide confirmación antes de eliminar.
- calcular_estadisticas() usa una lambda para los subtotales.
- Todo el código es 100% procedimental (cero clases, cero self, cero objetos propios).
========================================
"""


# ============================================================
# FUNCIONES CRUD (Create, Read, Update, Delete)
# ============================================================

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario.

    Antes de agregar, verifica que no exista un producto con el mismo
    nombre (comparación case-insensitive). Si ya existe, informa al
    usuario y no lo agrega.

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.
        nombre (str): Nombre del producto a agregar.
        precio (float): Precio unitario del producto (debe ser > 0).
        cantidad (int): Cantidad en stock (debe ser >= 0).

    Retorna:
        bool: True si se agregó exitosamente, False si ya existía.
    """
    # Verificar si el producto ya existe (búsqueda case-insensitive)
    existente = buscar_producto(inventario, nombre)
    if existente is not None:
        print(f"  ⚠️  El producto '{nombre}' ya existe en el inventario.")
        print(f"      Precio: ${existente['precio']:,.2f} | Stock: {existente['cantidad']}")
        print("      Use la opción 'Actualizar' para modificarlo.")
        return False

    # Crear el nuevo producto como diccionario
    nuevo_producto = {
        "nombre": nombre.strip().title(),
        "precio": round(precio, 2),
        "cantidad": int(cantidad)
    }

    # Agregar a la lista
    inventario.append(nuevo_producto)
    print(f"  ✅ Producto '{nuevo_producto['nombre']}' agregado exitosamente.")
    return True


def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario en formato de tabla alineada.

    Si el inventario está vacío, muestra un mensaje informativo.

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.

    Retorna:
        None: Solo imprime en consola.
    """
    if len(inventario) == 0:
        print("  📭 El inventario está vacío. Agrega productos primero.")
        return

    # Constantes de ancho para alineación
    AN = 4    # Ancho número
    AP = 28   # Ancho producto
    APR = 16  # Ancho precio
    AC = 10   # Ancho cantidad
    AS = 18   # Ancho subtotal
    ANCHO_TOTAL = AN + AP + APR + AC + AS

    # Encabezado
    print()
    print("  " + "=" * ANCHO_TOTAL)
    print("  " + " " * ((ANCHO_TOTAL - 22) // 2) + "📦 INVENTARIO ACTUAL 📦")
    print("  " + "=" * ANCHO_TOTAL)

    encabezado = (
        "#".rjust(AN) + "PRODUCTO".ljust(AP) + "PRECIO".rjust(APR)
        + "STOCK".rjust(AC) + "SUBTOTAL".rjust(AS)
    )
    print("  " + encabezado)
    print("  " + "-" * ANCHO_TOTAL)

    # Filas de productos
    valor_total = 0
    unidades_totales = 0

    for i, producto in enumerate(inventario, start=1):
        subtotal = producto["precio"] * producto["cantidad"]
        valor_total += subtotal
        unidades_totales += producto["cantidad"]

        fila = (
            str(i).rjust(AN)
            + producto["nombre"].ljust(AP)
            + f"${producto['precio']:>12,.2f}".rjust(APR)
            + str(producto["cantidad"]).rjust(AC)
            + f"${subtotal:>14,.2f}".rjust(AS)
        )
        print("  " + fila)

    # Pie de tabla
    print("  " + "-" * ANCHO_TOTAL)
    resumen = (
        "TOTALES".rjust(AN + AP)
        + " ".rjust(APR)
        + str(unidades_totales).rjust(AC)
        + f"${valor_total:>14,.2f}".rjust(AS)
    )
    print("  " + resumen)
    print("  " + "=" * ANCHO_TOTAL)
    print(f"  📊 {len(inventario)} producto(s) registrado(s)\n")


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre en el inventario (case-insensitive).

    Recorre la lista completa comparando nombres en minúsculas para
    que la búsqueda no sea sensible a mayúsculas/minúsculas.

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.
        nombre (str): Nombre del producto a buscar.

    Retorna:
        dict o None: El diccionario del producto si se encontró,
                     None si no existe en el inventario.
    """
    nombre_buscar = nombre.strip().lower()

    for producto in inventario:
        if producto["nombre"].lower() == nombre_buscar:
            return producto

    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza el precio y/o la cantidad de un producto existente.

    Solo modifica los campos para los cuales se proporcionó un valor
    (no es None). Si ambos son None, no realiza ningún cambio.

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.
        nombre (str): Nombre del producto a actualizar.
        nuevo_precio (float o None): Nuevo precio. None = no cambiar.
        nueva_cantidad (int o None): Nueva cantidad. None = no cambiar.

    Retorna:
        bool: True si se actualizó, False si no se encontró el producto.
    """
    producto = buscar_producto(inventario, nombre)

    if producto is None:
        print(f"  ❌ Producto '{nombre}' no encontrado en el inventario.")
        return False

    # Guardar valores anteriores para mostrar el cambio
    cambios = []

    if nuevo_precio is not None:
        precio_anterior = producto["precio"]
        producto["precio"] = round(nuevo_precio, 2)
        cambios.append(f"Precio: ${precio_anterior:,.2f} → ${producto['precio']:,.2f}")

    if nueva_cantidad is not None:
        cantidad_anterior = producto["cantidad"]
        producto["cantidad"] = int(nueva_cantidad)
        cambios.append(f"Cantidad: {cantidad_anterior} → {producto['cantidad']}")

    if len(cambios) == 0:
        print("  ℹ️  No se especificaron cambios.")
        return False

    print(f"  ✅ Producto '{producto['nombre']}' actualizado:")
    for cambio in cambios:
        print(f"      • {cambio}")

    return True


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario por nombre.

    Busca el producto, solicita confirmación mostrando sus datos,
    y lo remueve de la lista si se confirma.

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.
        nombre (str): Nombre del producto a eliminar.

    Retorna:
        bool: True si se eliminó, False si no se encontró o se canceló.
    """
    producto = buscar_producto(inventario, nombre)

    if producto is None:
        print(f"  ❌ Producto '{nombre}' no encontrado en el inventario.")
        return False

    # Mostrar datos del producto a eliminar
    print(f"\n  ⚠️  Producto a eliminar:")
    print(f"      Nombre:   {producto['nombre']}")
    print(f"      Precio:   ${producto['precio']:,.2f}")
    print(f"      Cantidad: {producto['cantidad']}")

    # Pedir confirmación
    confirmacion = input("\n  ¿Está seguro de eliminarlo? (S/N): ").strip().upper()

    if confirmacion == "S":
        inventario.remove(producto)
        print(f"  🗑️  Producto '{producto['nombre']}' eliminado del inventario.")
        return True
    else:
        print("  ↩️  Eliminación cancelada.")
        return False


# ============================================================
# FUNCIÓN DE ESTADÍSTICAS
# ============================================================

def calcular_estadisticas(inventario):
    """
    Calcula estadísticas generales del inventario.

    Recorre todos los productos para obtener totales, promedios y
    los productos destacados (más caro, mayor stock).

    Usa una función lambda para calcular el subtotal de cada producto:
        subtotal = lambda p: p["precio"] * p["cantidad"]

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.

    Retorna:
        dict: Diccionario con las siguientes claves:
            - "total_productos" (int): Cantidad de productos distintos.
            - "unidades_totales" (int): Suma de todas las cantidades.
            - "valor_total" (float): Suma de (precio * cantidad) de todos.
            - "precio_promedio" (float): Promedio de precios unitarios.
            - "producto_mas_caro" (dict): {"nombre": str, "precio": float}
            - "producto_mayor_stock" (dict): {"nombre": str, "cantidad": int}
            - "producto_mayor_valor" (dict): {"nombre": str, "subtotal": float}
        Retorna None si el inventario está vacío.
    """
    if len(inventario) == 0:
        print("  📭 El inventario está vacío. No hay estadísticas que calcular.")
        return None

    # Lambda para calcular subtotal de un producto
    subtotal = lambda p: p["precio"] * p["cantidad"]

    # Inicializar acumuladores
    unidades_totales = 0
    valor_total = 0
    suma_precios = 0

    # Inicializar con el primer producto
    producto_mas_caro = inventario[0]
    producto_mayor_stock = inventario[0]
    producto_mayor_valor = inventario[0]

    # Recorrer el inventario
    for producto in inventario:
        unidades_totales += producto["cantidad"]
        valor_total += subtotal(producto)
        suma_precios += producto["precio"]

        if producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto

        if producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto

        if subtotal(producto) > subtotal(producto_mayor_valor):
            producto_mayor_valor = producto

    # Construir el diccionario de estadísticas
    estadisticas = {
        "total_productos": len(inventario),
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "precio_promedio": suma_precios / len(inventario),
        "producto_mas_caro": {
            "nombre": producto_mas_caro["nombre"],
            "precio": producto_mas_caro["precio"]
        },
        "producto_mayor_stock": {
            "nombre": producto_mayor_stock["nombre"],
            "cantidad": producto_mayor_stock["cantidad"]
        },
        "producto_mayor_valor": {
            "nombre": producto_mayor_valor["nombre"],
            "subtotal": subtotal(producto_mayor_valor)
        }
    }

    return estadisticas


def mostrar_estadisticas(estadisticas):
    """
    Muestra las estadísticas del inventario en formato legible.

    Parámetros:
        estadisticas (dict): Diccionario retornado por calcular_estadisticas().

    Retorna:
        None: Solo imprime en consola.
    """
    if estadisticas is None:
        return

    ANCHO = 50

    print()
    print("  " + "=" * ANCHO)
    print("  " + " " * ((ANCHO - 26) // 2) + "📊 ESTADÍSTICAS GENERALES 📊")
    print("  " + "=" * ANCHO)
    print()
    print(f"  {'Productos registrados:':<35}{estadisticas['total_productos']:>10}")
    print(f"  {'Unidades totales en stock:':<35}{estadisticas['unidades_totales']:>10,}")
    print(f"  {'Valor total del inventario:':<35}${estadisticas['valor_total']:>9,.2f}")
    print(f"  {'Precio promedio unitario:':<35}${estadisticas['precio_promedio']:>9,.2f}")
    print()
    print("  " + "-" * ANCHO)
    print(f"  🏆 Producto más caro:")
    print(f"      {estadisticas['producto_mas_caro']['nombre']} "
          f"(${estadisticas['producto_mas_caro']['precio']:,.2f})")
    print(f"  📦 Producto con mayor stock:")
    print(f"      {estadisticas['producto_mayor_stock']['nombre']} "
          f"({estadisticas['producto_mayor_stock']['cantidad']:,} unidades)")
    print(f"  💰 Producto de mayor valor total:")
    print(f"      {estadisticas['producto_mayor_valor']['nombre']} "
          f"(${estadisticas['producto_mayor_valor']['subtotal']:,.2f})")
    print("  " + "=" * ANCHO)
    print()


def mostrar_detalle_producto(producto):
    """
    Muestra los detalles de un producto individual en formato legible.

    Parámetros:
        producto (dict): Diccionario con las claves "nombre", "precio", "cantidad".

    Retorna:
        None: Solo imprime en consola.
    """
    subtotal = producto["precio"] * producto["cantidad"]
    print(f"\n  {'─' * 40}")
    print(f"  📦 Detalle del Producto")
    print(f"  {'─' * 40}")
    print(f"  Nombre:    {producto['nombre']}")
    print(f"  Precio:    ${producto['precio']:,.2f}")
    print(f"  Cantidad:  {producto['cantidad']}")
    print(f"  Subtotal:  ${subtotal:,.2f}")
    print(f"  {'─' * 40}\n")
