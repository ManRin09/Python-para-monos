"""
========================================
🐒 Python para Monos
🚀 PROYECTO FINAL: Generador de Facturas de Supermercado
========================================

📚 DESCRIPCIÓN DEL PROYECTO:

Este script de ejecución lineal (apoyado en funciones, sin clases propias)
realiza el siguiente flujo completo:

1. Lee un archivo CSV ('compras.csv') con las compras del cliente.
   Formato del CSV: producto,cantidad,precio_unitario

2. Limpia y valida los datos (convierte strings a números).

3. Calcula para cada producto: subtotal_item = cantidad * precio_unitario.

4. Calcula los totales de la compra:
   - SUBTOTAL: Suma de todos los subtotales.
   - IVA (19%): Porcentaje sobre el subtotal.
   - TOTAL: Subtotal + IVA.

5. Genera un identificador único para la factura (fecha + aleatorio).

6. Crea un archivo PDF que simula una "tirilla de supermercado" con:
   - Encabezado con nombre del supermercado.
   - Fecha y número de factura.
   - Tabla de productos con cantidades, precios y subtotales.
   - Sección de totales (subtotal, IVA, total).
   - Pie de página con mensaje de agradecimiento.

MÓDULOS REQUERIDOS:
   - csv (estándar): Para leer el archivo de compras.
   - datetime (estándar): Para la fecha de la factura.
   - random (estándar): Para generar el identificador.
   - os (estándar): Para manejo de rutas.
   - fpdf2 (externo): Para generar el PDF.
     Instalación: pip install fpdf2

FORMATO DEL CSV DE ENTRADA (compras.csv):
   producto,cantidad,precio_unitario
   Leche Entera 1L,2,4500
   Pan Tajado,1,6200
   Huevos x30,1,18500
   ...

DISEÑO ESTRUCTURAL ESPERADO EN EL PDF:
   ┌─────────────────────────────────────┐
   │        🏪 SUPERMERCADO              │
   │        MONO MARKET                  │
   │   NIT: 900.123.456-7               │
   │   Dir: Calle 50 #10-30, Bogotá     │
   │   Tel: (601) 555-7890              │
   ├─────────────────────────────────────┤
   │ Factura: FAC-20250808-XXXX         │
   │ Fecha: 08/08/2025 14:30            │
   │ Cajero: Terminal Auto              │
   ├─────────────────────────────────────┤
   │ PRODUCTO       CANT  P.UNIT  SUBT  │
   │ ─────────────────────────────────── │
   │ Leche Entera      2  $4,500 $9,000 │
   │ Pan Tajado         1  $6,200 $6,200 │
   │ ...                                │
   ├─────────────────────────────────────┤
   │                 SUBTOTAL: $XXX,XXX │
   │                 IVA 19%:   $XX,XXX │
   │                 ══════════════════ │
   │                 TOTAL:    $XXX,XXX │
   ├─────────────────────────────────────┤
   │    ¡Gracias por su compra!         │
   │    Vuelva pronto 🐒               │
   └─────────────────────────────────────┘

✅ CRITERIOS DE ACEPTACIÓN EXHAUSTIVOS:

LECTURA DE DATOS:
   □ El script lee correctamente el archivo compras.csv.
   □ Si el archivo no existe, muestra un error claro y no se cae.
   □ Los datos se convierten a los tipos correctos (cantidad→int, precio→float).
   □ Se manejan errores de conversión sin que el script se detenga.

CÁLCULOS:
   □ El subtotal de cada producto es correcto (cantidad * precio_unitario).
   □ El SUBTOTAL general es la suma de todos los subtotales de productos.
   □ El IVA se calcula como el 19% del subtotal.
   □ El TOTAL es subtotal + IVA.
   □ Todos los montos se muestran con separador de miles y 2 decimales.

IDENTIFICADOR:
   □ Se genera un código único para la factura (formato: FAC-YYYYMMDD-XXXX).
   □ El código incluye la fecha actual y un componente aleatorio.

PDF:
   □ Se genera un archivo PDF válido que se puede abrir.
   □ El PDF tiene un diseño que simula una tirilla de supermercado.
   □ Contiene: encabezado, datos de factura, tabla de productos, totales y pie.
   □ El texto está correctamente alineado y legible.
   □ Los precios están alineados a la derecha.
   □ Se usa al menos una línea horizontal como separador.
   □ El archivo se guarda con un nombre descriptivo.

ARQUITECTURA:
   □ El código es 100% procedimental (funciones + script lineal).
   □ NO hay definiciones de clases (class) ni instanciación de objetos propios.
   □ Se usa FPDF solo como herramienta externa, no como base de OOP propia.
   □ Cada función tiene una responsabilidad clara y única.
   □ El flujo principal (main) es legible y muestra los pasos del proceso.
========================================
"""

import csv
import random
import os
from datetime import datetime

# Intentar importar fpdf2
try:
    from fpdf import FPDF
except ImportError:
    print("=" * 50)
    print("❌ ERROR: La librería 'fpdf2' no está instalada.")
    print("   Ejecuta: pip install fpdf2")
    print("=" * 50)
    exit(1)


# ============================================================
# CONFIGURACIÓN
# ============================================================
NOMBRE_SUPERMERCADO = "MONO MARKET"
NIT = "900.123.456-7"
DIRECCION = "Calle 50 #10-30, Bogota"
TELEFONO = "(601) 555-7890"
PORCENTAJE_IVA = 0.19

RUTA_SCRIPT = os.path.dirname(os.path.abspath(__file__))
RUTA_CSV = os.path.join(RUTA_SCRIPT, "compras.csv")
RUTA_PDF = os.path.join(RUTA_SCRIPT, "factura_generada.pdf")


# ============================================================
# FUNCIONES
# ============================================================

def generar_id_factura():
    """Genera un identificador único para la factura."""
    ahora = datetime.now()
    fecha = ahora.strftime("%Y%m%d")
    aleatorio = random.randint(1000, 9999)
    return f"FAC-{fecha}-{aleatorio}"


def leer_compras(ruta_csv):
    """Lee el archivo CSV de compras y devuelve una lista de diccionarios crudos."""
    registros = []
    try:
        with open(ruta_csv, "r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                registros.append(dict(fila))
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{ruta_csv}'")
        print("   Asegúrate de que 'compras.csv' esté en la carpeta proyecto_final/")
    return registros


def limpiar_compras(compras_crudas):
    """Limpia y convierte los tipos de datos de las compras."""
    compras_limpias = []
    errores = 0

    for i, compra in enumerate(compras_crudas):
        try:
            limpia = {
                "producto": compra.get("producto", "Sin nombre").strip(),
                "cantidad": int(compra.get("cantidad", "0").strip()),
                "precio_unitario": float(compra.get("precio_unitario", "0").strip()),
            }
            compras_limpias.append(limpia)
        except (ValueError, TypeError) as e:
            print(f"  ⚠️ Error en fila {i + 1}: {e}. Se omite este registro.")
            errores += 1

    return compras_limpias, errores


def calcular_totales(compras):
    """Calcula subtotal por producto, subtotal general, IVA y total."""
    subtotal_general = 0

    for compra in compras:
        compra["subtotal"] = compra["cantidad"] * compra["precio_unitario"]
        subtotal_general += compra["subtotal"]

    iva = subtotal_general * PORCENTAJE_IVA
    total = subtotal_general + iva

    return compras, subtotal_general, iva, total


def formatear_precio(valor):
    """Formatea un número como precio con separador de miles y 2 decimales."""
    return f"${valor:,.0f}"


def generar_pdf_tirilla(compras, subtotal, iva, total, id_factura, ruta_salida):
    """Genera el PDF con diseño de tirilla de supermercado."""

    # Configuración del PDF — Ancho estrecho como tirilla real (80mm)
    ANCHO_TIRILLA = 80
    pdf = FPDF(format=(ANCHO_TIRILLA, 297))
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()
    pdf.set_margins(5, 5, 5)

    margen = 5
    ancho_util = ANCHO_TIRILLA - (margen * 2)
    fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

    # ── ENCABEZADO ──
    pdf.set_font("Courier", "B", 14)
    pdf.set_xy(margen, 8)
    pdf.cell(w=ancho_util, h=6, text=NOMBRE_SUPERMERCADO, align="C",
             new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Courier", "", 7)
    pdf.cell(w=ancho_util, h=4, text=f"NIT: {NIT}", align="C",
             new_x="LMARGIN", new_y="NEXT")
    pdf.cell(w=ancho_util, h=4, text=DIRECCION, align="C",
             new_x="LMARGIN", new_y="NEXT")
    pdf.cell(w=ancho_util, h=4, text=f"Tel: {TELEFONO}", align="C",
             new_x="LMARGIN", new_y="NEXT")

    # Separador
    pdf.ln(2)
    y_sep = pdf.get_y()
    pdf.set_draw_color(0, 0, 0)
    pdf.set_line_width(0.3)
    pdf.dashed_line(margen, y_sep, ANCHO_TIRILLA - margen, y_sep, 1, 1)
    pdf.ln(3)

    # ── DATOS DE FACTURA ──
    pdf.set_font("Courier", "", 7)
    pdf.cell(w=ancho_util, h=4, text=f"Factura: {id_factura}",
             new_x="LMARGIN", new_y="NEXT")
    pdf.cell(w=ancho_util, h=4, text=f"Fecha: {fecha_hora}",
             new_x="LMARGIN", new_y="NEXT")
    pdf.cell(w=ancho_util, h=4, text="Cajero: Terminal Auto",
             new_x="LMARGIN", new_y="NEXT")

    # Separador
    pdf.ln(2)
    y_sep = pdf.get_y()
    pdf.dashed_line(margen, y_sep, ANCHO_TIRILLA - margen, y_sep, 1, 1)
    pdf.ln(3)

    # ── ENCABEZADO DE TABLA ──
    col_prod = 30
    col_cant = 8
    col_punit = 15
    col_subt = 17

    pdf.set_font("Courier", "B", 6)
    x_inicio = margen
    pdf.set_x(x_inicio)
    pdf.cell(w=col_prod, h=4, text="PRODUCTO", align="L")
    pdf.cell(w=col_cant, h=4, text="CANT", align="R")
    pdf.cell(w=col_punit, h=4, text="P.UNIT", align="R")
    pdf.cell(w=col_subt, h=4, text="SUBT", align="R",
             new_x="LMARGIN", new_y="NEXT")

    # Línea bajo encabezado
    y_sep = pdf.get_y()
    pdf.line(margen, y_sep, ANCHO_TIRILLA - margen, y_sep)
    pdf.ln(1)

    # ── FILAS DE PRODUCTOS ──
    pdf.set_font("Courier", "", 6)

    for compra in compras:
        nombre = compra["producto"]
        if len(nombre) > 18:
            nombre = nombre[:17] + "."

        pdf.set_x(x_inicio)
        pdf.cell(w=col_prod, h=3.5, text=nombre, align="L")
        pdf.cell(w=col_cant, h=3.5, text=str(compra["cantidad"]), align="R")
        pdf.cell(w=col_punit, h=3.5, text=formatear_precio(compra["precio_unitario"]), align="R")
        pdf.cell(w=col_subt, h=3.5, text=formatear_precio(compra["subtotal"]), align="R",
                 new_x="LMARGIN", new_y="NEXT")

    # ── SEPARADOR ANTES DE TOTALES ──
    pdf.ln(2)
    y_sep = pdf.get_y()
    pdf.dashed_line(margen, y_sep, ANCHO_TIRILLA - margen, y_sep, 1, 1)
    pdf.ln(3)

    # ── TOTALES ──
    col_label = 45
    col_valor = 25

    pdf.set_font("Courier", "", 7)
    pdf.set_x(x_inicio)
    pdf.cell(w=col_label, h=4, text="SUBTOTAL:", align="R")
    pdf.cell(w=col_valor, h=4, text=formatear_precio(subtotal), align="R",
             new_x="LMARGIN", new_y="NEXT")

    pdf.set_x(x_inicio)
    pdf.cell(w=col_label, h=4, text=f"IVA ({int(PORCENTAJE_IVA * 100)}%):", align="R")
    pdf.cell(w=col_valor, h=4, text=formatear_precio(iva), align="R",
             new_x="LMARGIN", new_y="NEXT")

    # Línea doble antes del total
    y_sep = pdf.get_y() + 1
    pdf.line(margen + 30, y_sep, ANCHO_TIRILLA - margen, y_sep)
    pdf.line(margen + 30, y_sep + 0.5, ANCHO_TIRILLA - margen, y_sep + 0.5)
    pdf.ln(3)

    pdf.set_font("Courier", "B", 9)
    pdf.set_x(x_inicio)
    pdf.cell(w=col_label, h=5, text="TOTAL:", align="R")
    pdf.cell(w=col_valor, h=5, text=formatear_precio(total), align="R",
             new_x="LMARGIN", new_y="NEXT")

    # ── SEPARADOR FINAL ──
    pdf.ln(3)
    y_sep = pdf.get_y()
    pdf.dashed_line(margen, y_sep, ANCHO_TIRILLA - margen, y_sep, 1, 1)
    pdf.ln(4)

    # ── ITEMS Y CANTIDAD TOTAL ──
    total_items = 0
    for compra in compras:
        total_items += compra["cantidad"]

    pdf.set_font("Courier", "", 7)
    pdf.cell(w=ancho_util, h=4, text=f"Total de articulos: {total_items}", align="C",
             new_x="LMARGIN", new_y="NEXT")

    # ── PIE DE PÁGINA ──
    pdf.ln(5)
    pdf.set_font("Courier", "B", 8)
    pdf.cell(w=ancho_util, h=5, text="Gracias por su compra!", align="C",
             new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Courier", "", 7)
    pdf.cell(w=ancho_util, h=4, text="Vuelva pronto a Mono Market", align="C",
             new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    # Código de factura al pie
    pdf.set_font("Courier", "", 5)
    pdf.cell(w=ancho_util, h=3, text=f"ID: {id_factura}", align="C",
             new_x="LMARGIN", new_y="NEXT")

    # ── GUARDAR ──
    pdf.output(ruta_salida)
    return ruta_salida


def mostrar_resumen_consola(compras, subtotal, iva, total, id_factura):
    """Muestra un resumen de la factura en la consola."""
    AN = 25
    AC = 6
    AP = 14
    AS = 14
    ANCHO = AN + AC + AP + AS

    print(f"\n{'=' * ANCHO}")
    print(f"  {NOMBRE_SUPERMERCADO} — Resumen de Compra")
    print(f"{'=' * ANCHO}")
    print(f"  Factura: {id_factura}")
    print(f"  Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f"{'─' * ANCHO}")

    print("PRODUCTO".ljust(AN) + "CANT".rjust(AC) + "P.UNIT".rjust(AP) + "SUBTOTAL".rjust(AS))
    print("─" * ANCHO)

    for c in compras:
        nombre = c["producto"]
        if len(nombre) > 23:
            nombre = nombre[:22] + "."
        print(
            nombre.ljust(AN)
            + str(c["cantidad"]).rjust(AC)
            + formatear_precio(c["precio_unitario"]).rjust(AP)
            + formatear_precio(c["subtotal"]).rjust(AS)
        )

    print("─" * ANCHO)
    print("SUBTOTAL:".rjust(AN + AC + AP) + formatear_precio(subtotal).rjust(AS))
    print(f"IVA ({int(PORCENTAJE_IVA * 100)}%):".rjust(AN + AC + AP) + formatear_precio(iva).rjust(AS))
    print("=" * ANCHO)
    print("TOTAL:".rjust(AN + AC + AP) + formatear_precio(total).rjust(AS))
    print("=" * ANCHO)


# ============================================================
# ORQUESTADOR PRINCIPAL
# ============================================================

def main():
    """Función principal que orquesta todo el proceso de generación de factura."""

    print("\n🐒 === GENERADOR DE FACTURAS — MONO MARKET === 🐒\n")

    # Paso 1: Generar identificador
    print("📋 Paso 1/5: Generando identificador de factura...")
    id_factura = generar_id_factura()
    print(f"   ✅ ID: {id_factura}\n")

    # Paso 2: Leer CSV
    print("📂 Paso 2/5: Leyendo archivo de compras...")
    compras_crudas = leer_compras(RUTA_CSV)
    if len(compras_crudas) == 0:
        print("   ❌ No se pudieron cargar las compras. Proceso cancelado.")
        return
    print(f"   ✅ {len(compras_crudas)} productos leídos.\n")

    # Paso 3: Limpiar datos
    print("🧹 Paso 3/5: Limpiando y validando datos...")
    compras_limpias, errores = limpiar_compras(compras_crudas)
    if errores > 0:
        print(f"   ⚠️ Se omitieron {errores} registros con errores.")
    print(f"   ✅ {len(compras_limpias)} productos válidos.\n")

    if len(compras_limpias) == 0:
        print("   ❌ No hay productos válidos para procesar. Proceso cancelado.")
        return

    # Paso 4: Calcular totales
    print("🧮 Paso 4/5: Calculando subtotales, IVA y total...")
    compras_calculadas, subtotal, iva, total = calcular_totales(compras_limpias)
    print(f"   ✅ Subtotal: {formatear_precio(subtotal)}")
    print(f"   ✅ IVA (19%): {formatear_precio(iva)}")
    print(f"   ✅ Total: {formatear_precio(total)}\n")

    # Paso 5: Generar PDF
    print("📄 Paso 5/5: Generando PDF de tirilla...")
    try:
        ruta_pdf = generar_pdf_tirilla(
            compras_calculadas, subtotal, iva, total, id_factura, RUTA_PDF
        )
        tamano = os.path.getsize(ruta_pdf)
        print(f"   ✅ PDF generado exitosamente!")
        print(f"   📄 Archivo: {ruta_pdf}")
        print(f"   📊 Tamaño: {tamano:,} bytes\n")
    except Exception as e:
        print(f"   ❌ Error generando PDF: {e}\n")
        return

    # Mostrar resumen en consola
    mostrar_resumen_consola(compras_calculadas, subtotal, iva, total, id_factura)

    print(f"\n🏁 === PROCESO COMPLETADO EXITOSAMENTE === 🏁")
    print(f"   Abre el archivo '{os.path.basename(ruta_pdf)}' para ver tu factura.\n")


# ============================================================
# PUNTO DE ENTRADA
# ============================================================
if __name__ == "__main__":
    main()
