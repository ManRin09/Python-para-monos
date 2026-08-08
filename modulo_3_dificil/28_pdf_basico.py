"""
========================================
🐒 Python para Monos
Módulo 3 — Actividad 28: PDF Básico con fpdf2
========================================

📚 TEORÍA:

Generar archivos PDF desde Python es una habilidad muy útil: puedes crear
reportes, certificados, recibos, documentación, etc., todo de forma automática.

LA LIBRERÍA fpdf2:
fpdf2 es una librería ligera para generar PDFs en Python. Es fácil de usar
y no requiere dependencias complicadas.

Instalación (si no lo hiciste en la actividad 27):
    pip install fpdf2

NOTA SOBRE LA REGLA PROCEDIMENTAL:
fpdf2 internamente usa un objeto FPDF para construir el PDF. Nosotros lo
USAMOS como herramienta (igual que usamos 'open()' para archivos), pero NO
estamos creando nuestras propias clases ni diseñando con OOP. Nuestro
código sigue siendo un script lineal con funciones.

CREAR UN PDF BÁSICO — Paso a paso:

    from fpdf import FPDF

    # Paso 1: Crear el documento PDF
    pdf = FPDF()

    # Paso 2: Agregar una página
    pdf.add_page()

    # Paso 3: Configurar la fuente
    pdf.set_font("Helvetica", size=16)

    # Paso 4: Escribir texto
    pdf.cell(text="¡Hola, este es mi primer PDF!")

    # Paso 5: Guardar el archivo
    pdf.output("mi_primer_pdf.pdf")

FUENTES DISPONIBLES (sin instalar nada extra):
    "Helvetica"  (sans-serif, la más usada)
    "Times"      (serif, estilo formal)
    "Courier"    (monoespaciada, estilo código)

ESTILOS DE FUENTE:
    pdf.set_font("Helvetica", style="", size=12)     # Normal
    pdf.set_font("Helvetica", style="B", size=12)    # Bold (negrita)
    pdf.set_font("Helvetica", style="I", size=12)    # Italic (cursiva)
    pdf.set_font("Helvetica", style="BI", size=12)   # Bold + Italic

TAMAÑO DE PÁGINA:
    FPDF()                        # A4 por defecto (210 x 297 mm)
    FPDF(orientation="L")         # Landscape (horizontal)
    FPDF(format="Letter")         # Tamaño carta

MÉTODOS PRINCIPALES PARA TEXTO:

    pdf.cell(w, h, text, border, new_x, new_y, align)
    - w: ancho de la celda (0 = hasta el final de la línea)
    - h: alto de la celda
    - text: el texto a escribir
    - border: 1 para borde, 0 sin borde
    - align: "L" izquierda, "C" centro, "R" derecha

    Ejemplo:
    pdf.cell(w=0, h=10, text="Texto centrado", align="C", new_x="LMARGIN", new_y="NEXT")

    pdf.multi_cell(w, h, text)
    - Para texto largo que necesita saltar de línea automáticamente.

    pdf.ln(h)
    - Agrega un salto de línea de altura h.

📝 INSTRUCCIONES:

Crea un script que genere un PDF simple con el siguiente contenido:

1. Importa FPDF de fpdf.

2. Crea una función 'crear_pdf_simple(ruta_salida)' que:
   a) Cree un documento PDF tamaño carta (Letter).
   b) Agregue una página.
   c) Escriba un TÍTULO centrado en fuente grande y negrita:
      "REPORTE DE ACTIVIDADES"
   d) Agregue una línea horizontal debajo del título.
   e) Escriba 3 párrafos de texto (pueden ser Lorem Ipsum o texto descriptivo)
      usando multi_cell para que el texto se ajuste al ancho.
   f) Agregue una sección con una lista numerada de 5 elementos.
   g) Al final, agregue la fecha actual.
   h) Guarde el archivo en la ruta indicada.

3. En la sección principal, llama a la función y confirma que el archivo
   se creó exitosamente.

✅ CRITERIOS DE ACEPTACIÓN:
- Se importa y usa fpdf2 correctamente.
- Se crea un PDF con al menos una página.
- El PDF tiene un título centrado en negrita.
- Se usan al menos 2 tamaños de fuente diferentes.
- Se usa cell() para líneas individuales y multi_cell() para párrafos.
- Se incluye una línea horizontal (separador visual).
- El archivo se guarda correctamente en disco.
- No se crean clases propias (se usa FPDF solo como herramienta).
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# from fpdf import FPDF
# from datetime import datetime
# import os
#
# ruta_script = os.path.dirname(os.path.abspath(__file__))
# ruta_salida = os.path.join(ruta_script, "reporte_basico.pdf")
#
#
# def crear_pdf_simple(ruta):
#     """Crea un PDF simple con título, párrafos y lista."""
#     pdf = FPDF(format="Letter")
#     pdf.add_page()
#
#     # Título
#     pdf.set_font("Helvetica", style="B", size=20)
#     pdf.cell(w=0, h=15, text="REPORTE DE ACTIVIDADES", align="C",
#              new_x="LMARGIN", new_y="NEXT")
#
#     # Línea horizontal
#     pdf.set_draw_color(50, 50, 50)
#     pdf.set_line_width(0.5)
#     pdf.line(10, pdf.get_y(), 200, pdf.get_y())
#     pdf.ln(10)
#
#     # Párrafo 1
#     pdf.set_font("Helvetica", size=11)
#     pdf.multi_cell(w=0, h=6, text=(
#         "Este documento fue generado automaticamente con Python utilizando "
#         "la libreria fpdf2. La generacion automatica de PDFs es una habilidad "
#         "muy util en el desarrollo de software, ya que permite crear reportes, "
#         "certificados y documentos de forma programatica."
#     ))
#     pdf.ln(5)
#
#     # Párrafo 2
#     pdf.multi_cell(w=0, h=6, text=(
#         "En este ejemplo, estamos demostrando las capacidades basicas de fpdf2: "
#         "crear paginas, agregar texto con diferentes fuentes y tamanos, dibujar "
#         "lineas y posicionar elementos en el documento."
#     ))
#     pdf.ln(8)
#
#     # Sección: Lista numerada
#     pdf.set_font("Helvetica", style="B", size=13)
#     pdf.cell(w=0, h=10, text="Temas cubiertos:", new_x="LMARGIN", new_y="NEXT")
#     pdf.ln(2)
#
#     pdf.set_font("Helvetica", size=11)
#     actividades = [
#         "Variables, tipos de datos y operadores",
#         "Condicionales y ciclos de control",
#         "Funciones y estructuras de datos",
#         "Lectura y escritura de archivos",
#         "Generacion de reportes en PDF",
#     ]
#
#     for i, actividad in enumerate(actividades, start=1):
#         pdf.cell(w=0, h=7, text=f"  {i}. {actividad}",
#                  new_x="LMARGIN", new_y="NEXT")
#
#     # Párrafo final
#     pdf.ln(10)
#     pdf.multi_cell(w=0, h=6, text=(
#         "La capacidad de generar documentos PDF de forma automatica abre las "
#         "puertas a muchas aplicaciones practicas, como la generacion de reportes "
#         "financieros, certificados de participacion, y documentos comerciales."
#     ))
#
#     # Fecha
#     pdf.ln(15)
#     pdf.set_font("Helvetica", style="I", size=9)
#     fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#     pdf.cell(w=0, h=10, text=f"Documento generado el: {fecha}", align="R")
#
#     # Guardar
#     pdf.output(ruta)
#     return ruta
#
#
# # --- Sección principal ---
# print("=== GENERANDO PDF BÁSICO ===\n")
#
# try:
#     archivo_creado = crear_pdf_simple(ruta_salida)
#     print(f"✅ PDF creado exitosamente: {archivo_creado}")
#
#     # Verificar que el archivo existe
#     if os.path.exists(ruta_salida):
#         tamano = os.path.getsize(ruta_salida)
#         print(f"📄 Tamaño del archivo: {tamano:,} bytes")
#     else:
#         print("❌ El archivo no se encontró después de la generación.")
#
# except ImportError:
#     print("❌ fpdf2 no está instalado. Ejecuta: pip install fpdf2")
# except Exception as e:
#     print(f"❌ Error al generar el PDF: {e}")
