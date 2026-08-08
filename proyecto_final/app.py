"""
========================================
🐒 Python para Monos
🚀 Proyecto Final — Archivo 3 de 3: app.py
   (Aplicación Principal — Menú Interactivo)
========================================

📚 TEORÍA:

Este archivo es el PUNTO DE ENTRADA del sistema. Es el único archivo
que el usuario ejecuta directamente:

    python3 app.py

Su responsabilidad es triple:

1. INTERFAZ DE USUARIO: Muestra el menú, recibe las opciones del usuario
   y muestra los resultados. Es la "cara" del sistema.

2. VALIDACIÓN DE INPUTS: Protege al programa de entradas inválidas.
   Si el usuario escribe "hola" donde debería ir un número, el programa
   NO se cae — le pide que ingrese un valor válido.

3. ORQUESTACIÓN: Coordina las llamadas entre los módulos servicios.py
   y archivos.py. Es el "director de orquesta" que sabe en qué orden
   llamar a cada función.

ARQUITECTURA DE 3 CAPAS:
    ┌──────────────────────┐
    │      app.py          │  ← Capa de PRESENTACIÓN (interfaz)
    │   (menú + inputs)    │
    ├──────────────────────┤
    │    servicios.py      │  ← Capa de LÓGICA (CRUD + cálculos)
    │  (funciones CRUD)    │
    ├──────────────────────┤
    │    archivos.py       │  ← Capa de DATOS (persistencia)
    │  (guardar/cargar)    │
    └──────────────────────┘

Esta separación en capas es un principio fundamental de la ingeniería
de software. Cada capa tiene una responsabilidad clara y se comunica
con las demás solo a través de funciones y parámetros.

PATRÓN DE MENÚ INTERACTIVO:
El menú funciona con un bucle while True que:
1. Muestra las opciones.
2. Lee la elección del usuario.
3. Ejecuta la acción correspondiente (if/elif).
4. Vuelve al paso 1.
5. Solo termina cuando el usuario elige "Salir" (break).

VALIDACIÓN DE INPUTS:
Para cada tipo de dato que necesitamos del usuario, existe una función
de validación dedicada que usa un while True con try/except:

    pedir_texto()    → Valida que no esté vacío.
    pedir_flotante() → Valida que sea numérico y esté en rango.
    pedir_entero()   → Valida que sea entero y esté en rango.
    pedir_ruta_csv() → Valida existencia, agrega .csv si falta.

IMPORTACIONES ENTRE MÓDULOS:
Este archivo importa funciones de los otros dos módulos:

    from servicios import agregar_producto, buscar_producto, ...
    from archivos import guardar_csv, cargar_csv

Python busca estos archivos en el mismo directorio. Por eso los 3
archivos DEBEN estar en la misma carpeta (proyecto_final/).

📝 INSTRUCCIONES:

Este módulo implementa las siguientes funciones:

FUNCIONES DE VALIDACIÓN (protegen contra inputs inválidos):
1. pedir_texto(mensaje, permitir_vacio=False) → str
2. pedir_flotante(mensaje, minimo=None, maximo=None) → float
3. pedir_entero(mensaje, minimo=None, maximo=None) → int
4. pedir_ruta_csv(mensaje, debe_existir=False) → str

FUNCIONES DE MENÚ (una por cada opción del 1 al 8):
5. opcion_agregar(inventario)       → Opción 1
6. opcion_mostrar(inventario)       → Opción 2
7. opcion_buscar(inventario)        → Opción 3
8. opcion_actualizar(inventario)    → Opción 4
9. opcion_eliminar(inventario)      → Opción 5
10. opcion_estadisticas(inventario) → Opción 6
11. opcion_guardar(inventario)      → Opción 7
12. opcion_cargar(inventario)       → Opción 8

FUNCIONES PRINCIPALES:
13. mostrar_menu() → Imprime las 9 opciones del menú.
14. main() → Bucle principal del sistema.

MENÚ CON 9 OPCIONES:
    1. ➕ Agregar producto
    2. 📋 Mostrar inventario
    3. 🔍 Buscar producto
    4. ✏️  Actualizar producto
    5. 🗑️  Eliminar producto
    6. 📊 Estadísticas
    7. 💾 Guardar en CSV
    8. 📂 Cargar desde CSV
    9. 🚪 Salir

EXTRAS IMPLEMENTADOS:
- Al iniciar, detecta si existe un CSV previo y ofrece cargarlo.
- Al salir, si hay productos en memoria, ofrece guardarlos.

✅ CRITERIOS DE ACEPTACIÓN:
- El menú se muestra en un bucle while True hasta elegir opción 9 (Salir).
- Cada opción del menú llama a funciones de servicios.py o archivos.py.
- Los inputs numéricos (opciones, precios, cantidades) están protegidos
  con try/except — no rompen la app si el usuario escribe letras.
- Los precios no aceptan valores negativos ni cero (minimo=0.01).
- Las cantidades no aceptan valores negativos (minimo=0).
- Las opciones inválidas (fuera de 1-9) se manejan con un mensaje de error.
- Se ofrece auto-carga al inicio y auto-guardado al salir.
- Se usa if __name__ == "__main__" para el punto de entrada.
- Todo el código es 100% procedimental (cero clases, cero self, cero objetos propios).
========================================
"""

import os

# Importar funciones de los módulos del proyecto
from servicios import (
    agregar_producto,
    mostrar_inventario,
    buscar_producto,
    actualizar_producto,
    eliminar_producto,
    calcular_estadisticas,
    mostrar_estadisticas,
    mostrar_detalle_producto
)

from archivos import guardar_csv, cargar_csv


# ============================================================
# CONFIGURACIÓN
# ============================================================
RUTA_SCRIPT = os.path.dirname(os.path.abspath(__file__))
RUTA_CSV_DEFECTO = os.path.join(RUTA_SCRIPT, "inventario.csv")


# ============================================================
# FUNCIONES DE VALIDACIÓN DE INPUT
# ============================================================

def pedir_texto(mensaje, permitir_vacio=False):
    """
    Pide al usuario un texto, validando que no esté vacío.

    Parámetros:
        mensaje (str): Mensaje a mostrar al usuario.
        permitir_vacio (bool): Si True, acepta strings vacíos.

    Retorna:
        str: El texto ingresado (con strip aplicado).
    """
    while True:
        texto = input(mensaje).strip()
        if texto != "" or permitir_vacio:
            return texto
        print("  ❌ Este campo no puede estar vacío. Intenta de nuevo.")


def pedir_flotante(mensaje, minimo=None, maximo=None):
    """
    Pide al usuario un número decimal, validando tipo y rango.

    Reintenta automáticamente si el usuario ingresa letras o valores
    fuera de rango.

    Parámetros:
        mensaje (str): Mensaje a mostrar.
        minimo (float o None): Valor mínimo permitido (inclusive).
        maximo (float o None): Valor máximo permitido (inclusive).

    Retorna:
        float: El número decimal validado.
    """
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = float(entrada)
        except ValueError:
            print(f"  ❌ '{entrada}' no es un número válido. Intenta de nuevo.")
            continue

        if minimo is not None and valor < minimo:
            print(f"  ❌ El valor debe ser mayor o igual a {minimo}.")
            continue

        if maximo is not None and valor > maximo:
            print(f"  ❌ El valor debe ser menor o igual a {maximo}.")
            continue

        return valor


def pedir_entero(mensaje, minimo=None, maximo=None):
    """
    Pide al usuario un número entero, validando tipo y rango.

    Reintenta automáticamente si el usuario ingresa letras, decimales
    o valores fuera de rango.

    Parámetros:
        mensaje (str): Mensaje a mostrar.
        minimo (int o None): Valor mínimo permitido (inclusive).
        maximo (int o None): Valor máximo permitido (inclusive).

    Retorna:
        int: El número entero validado.
    """
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
        except ValueError:
            print(f"  ❌ '{entrada}' no es un número entero válido. Intenta de nuevo.")
            continue

        if minimo is not None and valor < minimo:
            print(f"  ❌ El valor debe ser mayor o igual a {minimo}.")
            continue

        if maximo is not None and valor > maximo:
            print(f"  ❌ El valor debe ser menor o igual a {maximo}.")
            continue

        return valor


def pedir_ruta_csv(mensaje, debe_existir=False):
    """
    Pide al usuario una ruta de archivo CSV.

    Si el usuario presiona Enter sin escribir nada, usa la ruta por defecto.

    Parámetros:
        mensaje (str): Mensaje a mostrar.
        debe_existir (bool): Si True, valida que el archivo exista.

    Retorna:
        str: La ruta del archivo.
    """
    while True:
        ruta = input(mensaje).strip()

        # Si está vacía, usar ruta por defecto
        if ruta == "":
            ruta = RUTA_CSV_DEFECTO
            print(f"  ℹ️  Usando ruta por defecto: {ruta}")

        # Agregar extensión .csv si no la tiene
        if not ruta.endswith(".csv"):
            ruta += ".csv"

        # Verificar existencia si es necesario
        if debe_existir and not os.path.exists(ruta):
            print(f"  ❌ El archivo '{ruta}' no existe. Intenta de nuevo.")
            continue

        return ruta


# ============================================================
# FUNCIONES DEL MENÚ (una por opción)
# ============================================================

def opcion_agregar(inventario):
    """Maneja la opción 1: Agregar un nuevo producto."""
    print("\n  ╔══════════════════════════════════╗")
    print("  ║     ➕ AGREGAR PRODUCTO          ║")
    print("  ╚══════════════════════════════════╝")

    nombre = pedir_texto("  Nombre del producto: ")
    precio = pedir_flotante("  Precio unitario ($): ", minimo=0.01)
    cantidad = pedir_entero("  Cantidad en stock: ", minimo=0)

    agregar_producto(inventario, nombre, precio, cantidad)


def opcion_mostrar(inventario):
    """Maneja la opción 2: Mostrar el inventario completo."""
    mostrar_inventario(inventario)


def opcion_buscar(inventario):
    """Maneja la opción 3: Buscar un producto por nombre."""
    print("\n  ╔══════════════════════════════════╗")
    print("  ║     🔍 BUSCAR PRODUCTO           ║")
    print("  ╚══════════════════════════════════╝")

    nombre = pedir_texto("  Nombre a buscar: ")
    producto = buscar_producto(inventario, nombre)

    if producto is not None:
        mostrar_detalle_producto(producto)
    else:
        print(f"\n  ❌ No se encontró el producto '{nombre}' en el inventario.")
        print("      Tip: La búsqueda no distingue mayúsculas/minúsculas.")


def opcion_actualizar(inventario):
    """Maneja la opción 4: Actualizar precio y/o cantidad de un producto."""
    print("\n  ╔══════════════════════════════════╗")
    print("  ║     ✏️  ACTUALIZAR PRODUCTO       ║")
    print("  ╚══════════════════════════════════╝")

    nombre = pedir_texto("  Nombre del producto a actualizar: ")

    # Verificar que exista
    producto = buscar_producto(inventario, nombre)
    if producto is None:
        print(f"  ❌ Producto '{nombre}' no encontrado.")
        return

    # Mostrar datos actuales
    mostrar_detalle_producto(producto)

    # Pedir nuevos valores (Enter = no cambiar)
    print("  (Presiona Enter para mantener el valor actual)\n")

    # Precio
    entrada_precio = input(f"  Nuevo precio (actual: ${producto['precio']:,.2f}): ").strip()
    nuevo_precio = None
    if entrada_precio != "":
        try:
            nuevo_precio = float(entrada_precio)
            if nuevo_precio <= 0:
                print("  ⚠️  El precio debe ser mayor que 0. No se actualizará el precio.")
                nuevo_precio = None
        except ValueError:
            print("  ⚠️  Valor no válido para precio. No se actualizará el precio.")

    # Cantidad
    entrada_cantidad = input(f"  Nueva cantidad (actual: {producto['cantidad']}): ").strip()
    nueva_cantidad = None
    if entrada_cantidad != "":
        try:
            nueva_cantidad = int(entrada_cantidad)
            if nueva_cantidad < 0:
                print("  ⚠️  La cantidad no puede ser negativa. No se actualizará.")
                nueva_cantidad = None
        except ValueError:
            print("  ⚠️  Valor no válido para cantidad. No se actualizará la cantidad.")

    # Ejecutar actualización
    if nuevo_precio is None and nueva_cantidad is None:
        print("  ℹ️  No se realizaron cambios.")
    else:
        actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)


def opcion_eliminar(inventario):
    """Maneja la opción 5: Eliminar un producto."""
    print("\n  ╔══════════════════════════════════╗")
    print("  ║     🗑️  ELIMINAR PRODUCTO        ║")
    print("  ╚══════════════════════════════════╝")

    nombre = pedir_texto("  Nombre del producto a eliminar: ")
    eliminar_producto(inventario, nombre)


def opcion_estadisticas(inventario):
    """Maneja la opción 6: Mostrar estadísticas del inventario."""
    estadisticas = calcular_estadisticas(inventario)
    mostrar_estadisticas(estadisticas)


def opcion_guardar(inventario):
    """Maneja la opción 7: Guardar inventario en CSV."""
    print("\n  ╔══════════════════════════════════╗")
    print("  ║     💾 GUARDAR EN CSV            ║")
    print("  ╚══════════════════════════════════╝")

    print(f"  Ruta por defecto: {RUTA_CSV_DEFECTO}")
    ruta = pedir_ruta_csv("  Ruta del archivo (Enter = defecto): ")

    # Si el archivo ya existe, pedir confirmación
    if os.path.exists(ruta):
        print(f"\n  ⚠️  El archivo '{os.path.basename(ruta)}' ya existe.")
        confirmar = input("  ¿Desea sobrescribirlo? (S/N): ").strip().upper()
        if confirmar != "S":
            print("  ↩️  Guardado cancelado.")
            return

    guardar_csv(inventario, ruta)


def opcion_cargar(inventario):
    """Maneja la opción 8: Cargar inventario desde CSV."""
    print("\n  ╔══════════════════════════════════╗")
    print("  ║     📂 CARGAR DESDE CSV          ║")
    print("  ╚══════════════════════════════════╝")

    print(f"  Ruta por defecto: {RUTA_CSV_DEFECTO}")
    ruta = pedir_ruta_csv("  Ruta del archivo (Enter = defecto): ", debe_existir=True)

    cargar_csv(ruta, inventario)


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def mostrar_menu():
    """Imprime el menú principal con todas las opciones."""
    print("\n  ╔══════════════════════════════════════════╗")
    print("  ║   🐒 SISTEMA DE GESTIÓN DE INVENTARIO   ║")
    print("  ╠══════════════════════════════════════════╣")
    print("  ║                                          ║")
    print("  ║   1. ➕  Agregar producto                ║")
    print("  ║   2. 📋  Mostrar inventario              ║")
    print("  ║   3. 🔍  Buscar producto                 ║")
    print("  ║   4. ✏️   Actualizar producto             ║")
    print("  ║   5. 🗑️   Eliminar producto              ║")
    print("  ║   6. 📊  Estadísticas                    ║")
    print("  ║   7. 💾  Guardar en CSV                  ║")
    print("  ║   8. 📂  Cargar desde CSV                ║")
    print("  ║   9. 🚪  Salir                           ║")
    print("  ║                                          ║")
    print("  ╚══════════════════════════════════════════╝")


def main():
    """
    Función principal que orquesta todo el sistema.

    Mantiene el inventario en memoria como una lista de diccionarios.
    Ejecuta un bucle infinito (while True) mostrando el menú y
    procesando la opción elegida hasta que el usuario elija Salir (9).
    """
    # Estructura de datos central: lista de diccionarios
    inventario = []

    # Mensaje de bienvenida
    print("\n" + "=" * 50)
    print("  🐒 Bienvenido a Python para Monos 🐒")
    print("  Sistema de Gestión de Inventario v1.0")
    print("=" * 50)

    # Intentar cargar datos previos automáticamente
    if os.path.exists(RUTA_CSV_DEFECTO):
        print(f"\n  📂 Se detectó un archivo previo: {os.path.basename(RUTA_CSV_DEFECTO)}")
        cargar_auto = input("  ¿Desea cargarlo? (S/N): ").strip().upper()
        if cargar_auto == "S":
            cargar_csv(RUTA_CSV_DEFECTO, inventario)

    # === BUCLE PRINCIPAL DEL MENÚ ===
    while True:
        mostrar_menu()

        # Pedir opción con validación
        entrada = input("\n  Elige una opción (1-9): ").strip()

        # Validar que sea un número entre 1 y 9
        try:
            opcion = int(entrada)
        except ValueError:
            print(f"\n  ❌ '{entrada}' no es una opción válida. Ingresa un número del 1 al 9.")
            continue

        if opcion < 1 or opcion > 9:
            print(f"\n  ❌ La opción {opcion} no existe. Elige un número del 1 al 9.")
            continue

        # Ejecutar la opción elegida
        if opcion == 1:
            opcion_agregar(inventario)

        elif opcion == 2:
            opcion_mostrar(inventario)

        elif opcion == 3:
            opcion_buscar(inventario)

        elif opcion == 4:
            opcion_actualizar(inventario)

        elif opcion == 5:
            opcion_eliminar(inventario)

        elif opcion == 6:
            opcion_estadisticas(inventario)

        elif opcion == 7:
            opcion_guardar(inventario)

        elif opcion == 8:
            opcion_cargar(inventario)

        elif opcion == 9:
            # Preguntar si desea guardar antes de salir
            if len(inventario) > 0:
                print("\n  💾 ¿Desea guardar el inventario antes de salir?")
                guardar_antes = input("     (S/N): ").strip().upper()
                if guardar_antes == "S":
                    guardar_csv(inventario, RUTA_CSV_DEFECTO)

            print("\n  " + "=" * 46)
            print("  👋 ¡Hasta luego! Gracias por usar el sistema.")
            print("  🐒 Python para Monos — Proyecto Final")
            print("  " + "=" * 46 + "\n")
            break


# ============================================================
# PUNTO DE ENTRADA
# ============================================================
if __name__ == "__main__":
    main()
