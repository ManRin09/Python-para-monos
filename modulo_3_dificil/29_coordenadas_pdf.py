"""
========================================
🐒 Python para Monos
Módulo 3 — Actividad 29: Coordenadas y Posicionamiento en PDF
========================================

📚 TEORÍA:

En la actividad anterior, escribimos texto de forma secuencial (uno debajo
de otro). Pero para crear documentos con diseños más complejos, necesitas
POSICIONAR texto en coordenadas específicas del lienzo PDF.

SISTEMA DE COORDENADAS EN PDF:
El origen (0, 0) está en la ESQUINA SUPERIOR IZQUIERDA de la página.
- El eje X va de izquierda a derecha.
- El eje Y va de arriba hacia abajo.
- Las unidades por defecto son milímetros (mm).

    (0,0) ──────────────────── (210, 0)   ← Ancho A4: 210mm
      │                              │
      │         PÁGINA               │
      │                              │
      │                              │
    (0,297) ─────────────────── (210,297)  ← Alto A4: 297mm

    Para tamaño carta (Letter): 215.9 x 279.4 mm

POSICIONAMIENTO con set_xy():
    pdf.set_xy(x, y)  → Mueve el "cursor" a la posición (x, y)
    Luego cualquier texto que escribas aparecerá en esa posición.

    pdf.set_xy(50, 100)
    pdf.cell(text="Este texto está en la posición (50, 100)")

OBTENER POSICIÓN ACTUAL:
    x_actual = pdf.get_x()
    y_actual = pdf.get_y()

DIBUJAR LÍNEAS:
    pdf.line(x1, y1, x2, y2)

    # Línea horizontal completa:
    pdf.line(10, 50, 200, 50)

    # Línea vertical:
    pdf.line(100, 10, 100, 280)

DIBUJAR RECTÁNGULOS:
    pdf.rect(x, y, w, h)          # Solo borde
    pdf.rect(x, y, w, h, "F")    # Relleno (Fill)
    pdf.rect(x, y, w, h, "DF")   # Borde + Relleno

COLORES:
    pdf.set_text_color(r, g, b)    # Color del texto
    pdf.set_draw_color(r, g, b)    # Color de las líneas/bordes
    pdf.set_fill_color(r, g, b)    # Color de relleno

    # Ejemplo: texto rojo
    pdf.set_text_color(255, 0, 0)
    pdf.cell(text="Texto en rojo")

    # Ejemplo: rectángulo gris
    pdf.set_fill_color(200, 200, 200)
    pdf.rect(10, 10, 50, 20, "F")

EJEMPLO — Diseño con posicionamiento:

    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()

    # Encabezado en la parte superior
    pdf.set_xy(10, 10)
    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(text="EMPRESA XYZ")

    # Dirección en la esquina derecha
    pdf.set_xy(130, 10)
    pdf.set_font("Helvetica", size=10)
    pdf.cell(text="Calle 123, Ciudad")

    # Línea separadora
    pdf.line(10, 25, 200, 25)

    # Contenido en la mitad
    pdf.set_xy(10, 35)
    pdf.set_font("Helvetica", size=12)
    pdf.cell(text="Contenido principal aquí")

    pdf.output("documento.pdf")

TRUCO — Tablas manuales con celdas:
Puedes crear tablas posicionando celdas con bordes:

    pdf.set_xy(10, 50)
    pdf.cell(w=60, h=8, text="Columna 1", border=1)
    pdf.cell(w=60, h=8, text="Columna 2", border=1)
    pdf.cell(w=60, h=8, text="Columna 3", border=1)

📝 INSTRUCCIONES:

Crea un script que genere un PDF con un diseño de "tarjeta de presentación"
o membrete:

1. Crea una función 'crear_pdf_posicionado(ruta_salida)' que genere un PDF
   con el siguiente diseño:

   a) ENCABEZADO (parte superior):
      - Un rectángulo de color de fondo que ocupe todo el ancho.
      - Nombre de una empresa ficticia en letras grandes y blancas.
      - Un eslogan debajo en letra más pequeña.

   b) INFORMACIÓN (lado izquierdo, debajo del encabezado):
      - Dirección
      - Teléfono
      - Email

   c) TABLA DE DATOS (centro de la página):
      - Una tabla de 4 columnas y al menos 4 filas con bordes.
      - Encabezado de tabla con fondo de color.
      - Datos alineados dentro de las celdas.

   d) PIE DE PÁGINA (parte inferior):
      - Texto en letra pequeña y cursiva.
      - Fecha de generación.

2. Usa al menos 3 posiciones diferentes con set_xy().
3. Usa al menos 2 colores diferentes.
4. Usa rect() para al menos un rectángulo decorativo.

✅ CRITERIOS DE ACEPTACIÓN:
- Se usa set_xy() para posicionar texto en coordenadas específicas.
- Se usa set_text_color() y set_fill_color() para aplicar colores.
- Se crea una tabla con celdas (cell con border=1).
- Se dibuja al menos un rectángulo con rect().
- El diseño tiene al menos 3 secciones visualmente distintas.
- El PDF se genera sin errores y se guarda en disco.
- No se crean clases propias.
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
# ruta_salida = os.path.join(ruta_script, "reporte_posicionado.pdf")
#
#
# def crear_pdf_posicionado(ruta):
#     """Crea un PDF con posicionamiento preciso de elementos."""
#     pdf = FPDF(format="Letter")
#     pdf.add_page()
#
#     # === ENCABEZADO ===
#     # Rectángulo de fondo azul oscuro
#     pdf.set_fill_color(30, 60, 110)
#     pdf.rect(0, 0, 220, 40, "F")
#
#     # Nombre de empresa (blanco, grande)
#     pdf.set_text_color(255, 255, 255)
#     pdf.set_font("Helvetica", "B", 22)
#     pdf.set_xy(15, 8)
#     pdf.cell(text="TECH SOLUTIONS S.A.")
#
#     # Eslogan (blanco, pequeño)
#     pdf.set_font("Helvetica", "I", 10)
#     pdf.set_xy(15, 22)
#     pdf.cell(text="Innovacion y tecnologia para el futuro")
#
#     # === INFORMACIÓN DE CONTACTO ===
#     pdf.set_text_color(50, 50, 50)
#     pdf.set_font("Helvetica", size=9)
#
#     info_y = 50
#     pdf.set_xy(15, info_y)
#     pdf.cell(text="Calle 100 #15-25, Bogota, Colombia")
#     pdf.set_xy(15, info_y + 5)
#     pdf.cell(text="Tel: +57 (1) 555-0123")
#     pdf.set_xy(15, info_y + 10)
#     pdf.cell(text="Email: contacto@techsolutions.com")
#
#     # Línea separadora
#     pdf.set_draw_color(30, 60, 110)
#     pdf.set_line_width(0.5)
#     pdf.line(15, 70, 200, 70)
#
#     # === TABLA DE DATOS ===
#     pdf.set_xy(15, 80)
#     pdf.set_font("Helvetica", "B", 13)
#     pdf.set_text_color(30, 60, 110)
#     pdf.cell(text="Resumen de Servicios")
#
#     # Encabezado de tabla
#     tabla_y = 90
#     col_anchos = [60, 40, 40, 45]
#     encabezados = ["Servicio", "Horas", "Tarifa/h", "Total"]
#
#     pdf.set_xy(15, tabla_y)
#     pdf.set_font("Helvetica", "B", 10)
#     pdf.set_fill_color(30, 60, 110)
#     pdf.set_text_color(255, 255, 255)
#
#     for i, enc in enumerate(encabezados):
#         alineacion = "L" if i == 0 else "R"
#         pdf.cell(w=col_anchos[i], h=8, text=enc, border=1, fill=True, align=alineacion)
#     pdf.ln()
#
#     # Filas de datos
#     datos = [
#         ["Desarrollo Web", "120", "$85,000", "$10,200,000"],
#         ["Consultoria IT", "40", "$120,000", "$4,800,000"],
#         ["Soporte Tecnico", "80", "$45,000", "$3,600,000"],
#         ["Capacitacion", "24", "$95,000", "$2,280,000"],
#     ]
#
#     pdf.set_font("Helvetica", size=10)
#     pdf.set_text_color(50, 50, 50)
#     pdf.set_fill_color(240, 240, 245)
#
#     for idx, fila in enumerate(datos):
#         rellenar = idx % 2 == 0
#         for i, dato in enumerate(fila):
#             alineacion = "L" if i == 0 else "R"
#             pdf.cell(w=col_anchos[i], h=7, text=dato, border=1,
#                      fill=rellenar, align=alineacion)
#         pdf.ln()
#
#     # Fila total
#     pdf.set_font("Helvetica", "B", 10)
#     pdf.set_fill_color(230, 235, 240)
#     pdf.cell(w=140, h=8, text="TOTAL", border=1, fill=True, align="R")
#     pdf.cell(w=45, h=8, text="$20,880,000", border=1, fill=True, align="R")
#
#     # === PIE DE PÁGINA ===
#     pdf.set_xy(15, 260)
#     pdf.set_draw_color(180, 180, 180)
#     pdf.line(15, 260, 200, 260)
#
#     pdf.set_xy(15, 263)
#     pdf.set_font("Helvetica", "I", 8)
#     pdf.set_text_color(130, 130, 130)
#     fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
#     pdf.cell(text=f"Documento generado automaticamente el {fecha}")
#
#     pdf.set_xy(150, 263)
#     pdf.cell(text="Pagina 1 de 1")
#
#     # Guardar
#     pdf.output(ruta)
#     return ruta
#
#
# # --- Sección principal ---
# print("=== GENERANDO PDF CON POSICIONAMIENTO ===\n")
#
# try:
#     archivo = crear_pdf_posicionado(ruta_salida)
#     tamano = os.path.getsize(ruta_salida)
#     print(f"✅ PDF generado: {archivo}")
#     print(f"📄 Tamaño: {tamano:,} bytes")
# except ImportError:
#     print("❌ fpdf2 no está instalado. Ejecuta: pip install fpdf2")
# except Exception as e:
#     print(f"❌ Error: {e}")
