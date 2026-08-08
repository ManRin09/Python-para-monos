"""
========================================
🐒 Python para Monos
Módulo 3 — Actividad 30: Orquestador de Funciones
========================================

📚 TEORÍA:

Un ORQUESTADOR es un script principal que coordina la ejecución de múltiples
funciones en un orden específico para completar un flujo de trabajo completo.
Es como un director de orquesta: no toca ningún instrumento, pero decide
quién toca, cuándo y en qué orden.

Este patrón es fundamental en programación del mundo real:
- Pipelines de datos (ETL: Extract → Transform → Load)
- Automatización de procesos
- Scripts de despliegue
- Generación de reportes

ESTRUCTURA DE UN ORQUESTADOR:

    def paso_1_cargar_datos():
        print("Cargando datos...")
        datos = [...]
        return datos

    def paso_2_procesar(datos):
        print("Procesando...")
        resultado = [...]
        return resultado

    def paso_3_generar_reporte(resultado):
        print("Generando reporte...")
        # crear archivo
        return "ruta/al/reporte.txt"

    def paso_4_notificar(ruta_reporte):
        print(f"Reporte generado en: {ruta_reporte}")

    # === ORQUESTADOR ===
    def main():
        print("=== INICIO DEL PROCESO ===")

        datos = paso_1_cargar_datos()
        resultado = paso_2_procesar(datos)
        ruta = paso_3_generar_reporte(resultado)
        paso_4_notificar(ruta)

        print("=== PROCESO COMPLETADO ===")

    # Ejecutar
    main()

PRINCIPIOS CLAVE:

1. CADA FUNCIÓN HACE UNA SOLA COSA:
   No mezcles leer un archivo y procesarlo en la misma función.

2. LAS FUNCIONES SE COMUNICAN POR PARÁMETROS Y RETURNS:
   No uses variables globales. El resultado de una función se pasa como
   parámetro a la siguiente.

3. EL ORQUESTADOR ES LINEAL Y LEGIBLE:
   Al leer la función main(), deberías entender el flujo completo del
   programa sin necesidad de ver el detalle de cada función.

4. MANEJO DE ERRORES EN EL ORQUESTADOR:
   El orquestador puede envolver cada paso en try/except:

    def main():
        try:
            datos = paso_1_cargar_datos()
        except FileNotFoundError:
            print("Error: Archivo no encontrado")
            return

        try:
            resultado = paso_2_procesar(datos)
        except Exception as e:
            print(f"Error en el procesamiento: {e}")
            return

        paso_3_generar_reporte(resultado)
        print("Proceso completado exitosamente")

PATRÓN if __name__ == "__main__":
    Este patrón permite que el script se ejecute directamente pero también
    pueda ser importado por otros scripts sin ejecutar el main:

    if __name__ == "__main__":
        main()

📝 INSTRUCCIONES:

Crea un script orquestador que ejecute un flujo completo de procesamiento:

FLUJO: Leer datos → Limpiar → Calcular → Formatear → Guardar reporte

1. Función 'cargar_datos()':
   - Define una lista de diccionarios con datos de empleados:
     [{"nombre": "...", "departamento": "...", "horas": "...", "tarifa": "..."}]
   - (Simula la carga desde una fuente externa)
   - Devuelve la lista de diccionarios (con datos como strings, simulando CSV).

2. Función 'limpiar_datos(datos_crudos)':
   - Convierte "horas" a int y "tarifa" a float.
   - Limpia los nombres (strip + title).
   - Devuelve una lista de diccionarios con tipos correctos.

3. Función 'calcular_pagos(datos_limpios)':
   - Para cada empleado, calcula: pago = horas * tarifa.
   - Agrega la clave "pago" a cada diccionario.
   - Calcula y devuelve también el total general.
   - Devuelve (datos_con_pagos, total_general).

4. Función 'formatear_tabla(datos_con_pagos, total)':
   - Crea un string con una tabla formateada usando ljust/rjust.
   - Incluye encabezados, filas de datos y total.
   - Devuelve el string completo.

5. Función 'guardar_reporte(contenido, ruta)':
   - Escribe el string en un archivo .txt.
   - Devuelve True si se guardó exitosamente.

6. Función 'main()':
   - Llama a cada función en orden, pasando el resultado de una a la siguiente.
   - Imprime mensajes de progreso: "Paso 1/5: Cargando datos..."
   - Maneja errores con try/except.
   - Imprime el reporte en consola Y lo guarda en archivo.

✅ CRITERIOS DE ACEPTACIÓN:
- Se crean al menos 5 funciones independientes.
- Cada función recibe parámetros y devuelve resultados (no usa globales).
- El main() orquesta las funciones en secuencia.
- Los datos fluyen de función en función por parámetros y returns.
- Se muestra progreso paso a paso.
- Se genera un archivo de reporte .txt.
- Se usa if __name__ == "__main__".
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# import os
#
# ruta_script = os.path.dirname(os.path.abspath(__file__))
# ruta_reporte = os.path.join(ruta_script, "reporte_pagos.txt")
#
#
# def cargar_datos():
#     """Paso 1: Simula la carga de datos desde una fuente externa."""
#     datos = [
#         {"nombre": "  ana lópez  ", "departamento": "ingeniería", "horas": "160", "tarifa": "45000"},
#         {"nombre": "carlos méndez", "departamento": "diseño", "horas": "140", "tarifa": "38000"},
#         {"nombre": "  MARÍA GARCÍA ", "departamento": "ingeniería", "horas": "168", "tarifa": "52000"},
#         {"nombre": "juan pérez", "departamento": "soporte", "horas": "150", "tarifa": "30000"},
#         {"nombre": "  sofía herrera  ", "departamento": "diseño", "horas": "155", "tarifa": "40000"},
#         {"nombre": "pedro castillo", "departamento": "soporte", "horas": "145", "tarifa": "32000"},
#     ]
#     return datos
#
#
# def limpiar_datos(datos_crudos):
#     """Paso 2: Limpia y convierte tipos de datos."""
#     datos_limpios = []
#     for reg in datos_crudos:
#         limpio = {
#             "nombre": reg["nombre"].strip().title(),
#             "departamento": reg["departamento"].strip().title(),
#             "horas": int(reg["horas"].strip()),
#             "tarifa": float(reg["tarifa"].strip()),
#         }
#         datos_limpios.append(limpio)
#     return datos_limpios
#
#
# def calcular_pagos(datos_limpios):
#     """Paso 3: Calcula el pago de cada empleado y el total."""
#     total_general = 0
#     for emp in datos_limpios:
#         emp["pago"] = emp["horas"] * emp["tarifa"]
#         total_general += emp["pago"]
#     return datos_limpios, total_general
#
#
# def formatear_tabla(datos_con_pagos, total):
#     """Paso 4: Crea una tabla formateada como string."""
#     AN = 22   # Ancho nombre
#     AD = 16   # Ancho departamento
#     AH = 8    # Ancho horas
#     AT = 14   # Ancho tarifa
#     AP = 18   # Ancho pago
#     ANCHO_TOTAL = AN + AD + AH + AT + AP
#
#     lineas = []
#     lineas.append("=" * ANCHO_TOTAL)
#     lineas.append("  REPORTE DE PAGOS A EMPLEADOS")
#     lineas.append("=" * ANCHO_TOTAL)
#     lineas.append("")
#
#     # Encabezado
#     encabezado = (
#         "NOMBRE".ljust(AN) + "DEPTO".ljust(AD)
#         + "HORAS".rjust(AH) + "TARIFA".rjust(AT)
#         + "PAGO".rjust(AP)
#     )
#     lineas.append(encabezado)
#     lineas.append("-" * ANCHO_TOTAL)
#
#     # Filas
#     for emp in datos_con_pagos:
#         fila = (
#             emp["nombre"].ljust(AN)
#             + emp["departamento"].ljust(AD)
#             + str(emp["horas"]).rjust(AH)
#             + f"${emp['tarifa']:,.0f}".rjust(AT)
#             + f"${emp['pago']:,.0f}".rjust(AP)
#         )
#         lineas.append(fila)
#
#     lineas.append("=" * ANCHO_TOTAL)
#     lineas.append("TOTAL".ljust(AN + AD + AH + AT) + f"${total:,.0f}".rjust(AP))
#     lineas.append("=" * ANCHO_TOTAL)
#
#     return "\n".join(lineas)
#
#
# def guardar_reporte(contenido, ruta):
#     """Paso 5: Guarda el reporte en un archivo de texto."""
#     try:
#         with open(ruta, "w", encoding="utf-8") as archivo:
#             archivo.write(contenido + "\n")
#         return True
#     except Exception as e:
#         print(f"❌ Error al guardar: {e}")
#         return False
#
#
# def main():
#     """Orquestador: coordina todos los pasos del proceso."""
#     print("🚀 === INICIO DEL PROCESO ===\n")
#
#     # Paso 1
#     print("📦 Paso 1/5: Cargando datos...")
#     try:
#         datos_crudos = cargar_datos()
#         print(f"   ✅ {len(datos_crudos)} registros cargados.\n")
#     except Exception as e:
#         print(f"   ❌ Error cargando datos: {e}")
#         return
#
#     # Paso 2
#     print("🧹 Paso 2/5: Limpiando datos...")
#     try:
#         datos_limpios = limpiar_datos(datos_crudos)
#         print(f"   ✅ {len(datos_limpios)} registros limpiados.\n")
#     except Exception as e:
#         print(f"   ❌ Error limpiando datos: {e}")
#         return
#
#     # Paso 3
#     print("🧮 Paso 3/5: Calculando pagos...")
#     try:
#         datos_pagos, total = calcular_pagos(datos_limpios)
#         print(f"   ✅ Pagos calculados. Total: ${total:,.0f}\n")
#     except Exception as e:
#         print(f"   ❌ Error en cálculos: {e}")
#         return
#
#     # Paso 4
#     print("📊 Paso 4/5: Formateando reporte...")
#     reporte = formatear_tabla(datos_pagos, total)
#     print(f"   ✅ Reporte formateado.\n")
#
#     # Paso 5
#     print("💾 Paso 5/5: Guardando reporte...")
#     exito = guardar_reporte(reporte, ruta_reporte)
#     if exito:
#         print(f"   ✅ Guardado en: {ruta_reporte}\n")
#     else:
#         print(f"   ❌ No se pudo guardar.\n")
#
#     # Mostrar reporte en consola
#     print("=" * 50)
#     print("  📋 REPORTE GENERADO:")
#     print("=" * 50)
#     print()
#     print(reporte)
#
#     print("\n🏁 === PROCESO COMPLETADO ===")
#
#
# if __name__ == "__main__":
#     main()
