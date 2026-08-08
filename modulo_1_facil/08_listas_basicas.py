"""
========================================
🐒 Python para Monos
Módulo 1 — Actividad 08: Listas Básicas
========================================

📚 TEORÍA:

Una LISTA es una colección ordenada y mutable de elementos. Es una de las
estructuras de datos más importantes en Python. Puedes guardar cualquier tipo
de dato dentro de una lista, e incluso mezclar tipos.

CREAR UNA LISTA:
    numeros = [10, 20, 30, 40, 50]
    nombres = ["Ana", "Carlos", "María"]
    mixta = [1, "hola", True, 3.14]
    vacia = []

ACCEDER A ELEMENTOS (por índice, empieza en 0):
    frutas = ["manzana", "banana", "cereza", "durazno"]
    frutas[0]    →  "manzana"     # Primer elemento
    frutas[2]    →  "cereza"      # Tercer elemento
    frutas[-1]   →  "durazno"     # Último elemento
    frutas[-2]   →  "cereza"      # Penúltimo

MODIFICAR UN ELEMENTO:
    frutas[1] = "pera"   # Cambia "banana" por "pera"

MÉTODOS PRINCIPALES:

    lista.append(elemento)   → Agrega un elemento AL FINAL de la lista.
        frutas.append("uva")  →  ["manzana", "pera", "cereza", "durazno", "uva"]

    lista.insert(indice, elemento) → Inserta en una posición específica.
        frutas.insert(1, "kiwi")

    lista.remove(elemento)   → Elimina la PRIMERA aparición del elemento.
        frutas.remove("cereza")
        ⚠️ Si el elemento no existe, lanza un ValueError.

    lista.pop()              → Elimina y DEVUELVE el último elemento.
    lista.pop(indice)        → Elimina y devuelve el elemento en ese índice.
        eliminado = frutas.pop(0)  # Elimina "manzana" y lo guarda

    lista.sort()             → Ordena la lista de menor a mayor (in-place).
    lista.sort(reverse=True) → Ordena de mayor a menor.
    lista.reverse()          → Invierte el orden actual de la lista.

    lista.index(elemento)    → Devuelve el índice de la primera aparición.
    lista.count(elemento)    → Cuenta cuántas veces aparece un elemento.

    len(lista)               → Devuelve la cantidad de elementos.

VERIFICAR SI UN ELEMENTO EXISTE:
    if "manzana" in frutas:
        print("¡Sí está!")

COPIAR UNA LISTA:
    copia = frutas.copy()    # Crea una copia independiente
    # ⚠️ copia = frutas  NO crea una copia, ambas apuntan a la misma lista.

SLICING (funciona igual que con strings):
    numeros = [10, 20, 30, 40, 50]
    numeros[1:4]   →  [20, 30, 40]
    numeros[:3]    →  [10, 20, 30]
    numeros[2:]    →  [30, 40, 50]

📝 INSTRUCCIONES:

Crea un script que administre una lista de tareas pendientes:

1. Inicia con una lista llamada 'tareas' que contenga 3 tareas predefinidas:
   ["Estudiar Python", "Hacer ejercicio", "Leer un libro"]

2. Imprime la lista inicial con un encabezado "=== LISTA DE TAREAS ==="

3. Realiza las siguientes operaciones EN ORDEN (imprime la lista después de cada una):
   a) Agrega la tarea "Comprar víveres" al final.
   b) Inserta la tarea "Meditar 10 minutos" en la posición 2 (índice 2).
   c) Elimina la tarea "Hacer ejercicio" usando remove().
   d) Ordena la lista alfabéticamente.
   e) Muestra cuántas tareas hay en total con len().

4. Al final, imprime la lista enumerada (con números) usando un ciclo for
   con enumerate():
   "1. Comprar víveres"
   "2. Estudiar Python"
   ...

✅ CRITERIOS DE ACEPTACIÓN:
- La lista inicia con 3 elementos predefinidos.
- Se deben usar los métodos: append(), insert(), remove(), sort().
- Se debe usar len() para mostrar la cantidad de elementos.
- La lista se imprime después de CADA operación para ver los cambios.
- La lista final se muestra enumerada con for y enumerate().
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# tareas = ["Estudiar Python", "Hacer ejercicio", "Leer un libro"]
# print("=== LISTA DE TAREAS ===")
# print(f"Lista inicial: {tareas}\n")
#
# # a) Agregar al final
# tareas.append("Comprar víveres")
# print(f"a) Después de append: {tareas}")
#
# # b) Insertar en posición 2
# tareas.insert(2, "Meditar 10 minutos")
# print(f"b) Después de insert: {tareas}")
#
# # c) Eliminar "Hacer ejercicio"
# tareas.remove("Hacer ejercicio")
# print(f"c) Después de remove: {tareas}")
#
# # d) Ordenar alfabéticamente
# tareas.sort()
# print(f"d) Después de sort: {tareas}")
#
# # e) Cantidad total
# print(f"\ne) Total de tareas: {len(tareas)}")
#
# # Lista final enumerada
# print("\n=== LISTA FINAL ===")
# for indice, tarea in enumerate(tareas, start=1):
#     print(f"{indice}. {tarea}")
