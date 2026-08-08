"""
========================================
🐒 Python para Monos
Módulo 3 — Actividad 27: Entorno Virtual y pip
========================================

📚 TEORÍA:

Hasta ahora hemos usado SOLO la biblioteca estándar de Python (módulos que
vienen pre-instalados como csv, datetime, random, os, etc.). Pero Python
tiene un ecosistema ENORME de librerías creadas por la comunidad que puedes
instalar para extender sus capacidades.

¿QUÉ ES pip?
pip es el gestor de paquetes de Python. Es un programa de línea de comandos
que te permite instalar, actualizar y desinstalar librerías externas desde
el repositorio oficial PyPI (Python Package Index).

    pip install nombre_paquete      # Instalar un paquete
    pip install fpdf2               # Ejemplo: instalar la librería fpdf2
    pip uninstall nombre_paquete    # Desinstalar
    pip list                        # Ver todos los paquetes instalados
    pip show nombre_paquete         # Ver detalles de un paquete

¿QUÉ ES UN ENTORNO VIRTUAL (venv)?
Un entorno virtual es una carpeta aislada que contiene su PROPIA copia de
Python y sus propios paquetes instalados. Esto es fundamental porque:

1. EVITA CONFLICTOS: Diferentes proyectos pueden necesitar diferentes
   versiones de la misma librería.
   - Proyecto A necesita fpdf2 versión 2.7
   - Proyecto B necesita fpdf2 versión 2.8
   - Sin entorno virtual, solo puedes tener UNA versión instalada.

2. MANTIENE LIMPIO tu Python global: No contaminas la instalación del sistema.

3. REPRODUCIBILIDAD: Puedes compartir tu proyecto con la lista exacta de
   dependencias y cualquiera puede recrear el mismo entorno.

CREAR UN ENTORNO VIRTUAL:
    # En la terminal, desde la carpeta de tu proyecto:
    python3 -m venv venv

    # Esto crea una carpeta llamada 'venv/' con:
    # venv/
    # ├── bin/          (Linux/Mac) o Scripts/ (Windows)
    # ├── lib/          Librerías instaladas
    # └── pyvenv.cfg    Configuración

ACTIVAR EL ENTORNO VIRTUAL:
    # Linux / Mac:
    source venv/bin/activate

    # Windows (CMD):
    venv\\Scripts\\activate.bat

    # Windows (PowerShell):
    venv\\Scripts\\Activate.ps1

    Cuando está activado, verás (venv) al inicio del prompt:
    (venv) usuario@pc:~/proyecto$

DESACTIVAR:
    deactivate

INSTALAR PAQUETES DENTRO DEL ENTORNO:
    # Con el entorno activado:
    pip install fpdf2
    pip install requests
    pip install pandas

REQUIREMENTS.TXT:
Es un archivo que lista todas las dependencias de tu proyecto:

    # Generar el archivo:
    pip freeze > requirements.txt

    # Contenido del archivo:
    fpdf2==2.8.1
    Pillow==10.4.0

    # Instalar desde el archivo (en otro computador o entorno):
    pip install -r requirements.txt

FLUJO COMPLETO para un proyecto nuevo:
    mkdir mi_proyecto
    cd mi_proyecto
    python3 -m venv venv
    source venv/bin/activate      # Activar
    pip install fpdf2             # Instalar dependencias
    pip freeze > requirements.txt # Guardar dependencias
    python3 mi_script.py          # Ejecutar tu código
    deactivate                    # Desactivar al terminar

⚠️ IMPORTANTE: La carpeta venv/ NUNCA se sube a Git. Agrégala a .gitignore:
    echo "venv/" >> .gitignore

📝 INSTRUCCIONES:

Esta actividad es principalmente PRÁCTICA EN TERMINAL. El archivo .py sirve
como guía y documentación.

EJERCICIOS A REALIZAR EN LA TERMINAL:

1. Abre la terminal en la raíz del repositorio Python-para-monos.

2. Crea un entorno virtual:
   python3 -m venv venv

3. Activa el entorno virtual:
   source venv/bin/activate   (Linux/Mac)

4. Verifica que está activado:
   which python3    (debe mostrar una ruta dentro de venv/)
   pip list         (debe mostrar solo pip y setuptools)

5. Instala la librería fpdf2 (la usaremos en las actividades 28 y 29):
   pip install fpdf2

6. Verifica la instalación:
   pip show fpdf2
   pip list

7. Genera el archivo requirements.txt:
   pip freeze > requirements.txt

8. Verifica el contenido de requirements.txt:
   cat requirements.txt

9. BONUS: Desactiva el entorno, elimínalo, recréalo e instala desde
   requirements.txt:
   deactivate
   rm -rf venv
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

AHORA EN ESTE ARCHIVO: Escribe un pequeño script que verifique si fpdf2
está instalado correctamente.

✅ CRITERIOS DE ACEPTACIÓN:
- Se creó un entorno virtual con python3 -m venv.
- Se activó correctamente (el prompt muestra (venv)).
- Se instaló fpdf2 con pip install.
- Se generó requirements.txt con pip freeze.
- El script de verificación se ejecuta sin errores.
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:
# (Verifica que fpdf2 está instalado)



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# print("=== VERIFICACIÓN DE ENTORNO ===\n")
#
# # Verificar Python
# import sys
# print(f"Python: {sys.version}")
# print(f"Ejecutable: {sys.executable}")
#
# # Verificar si estamos en un entorno virtual
# if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
#     print("✅ Entorno virtual ACTIVADO")
# else:
#     print("⚠️ NO estás en un entorno virtual")
#
# # Verificar fpdf2
# print("\n--- Verificando fpdf2 ---")
# try:
#     from fpdf import FPDF
#     print("✅ fpdf2 está instalado correctamente")
#     print(f"   Versión del módulo disponible")
#
#     # Prueba básica: crear un PDF vacío
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Helvetica", size=12)
#     pdf.cell(text="¡fpdf2 funciona correctamente!")
#     print("✅ Se pudo crear un objeto PDF sin errores")
#
# except ImportError:
#     print("❌ fpdf2 NO está instalado")
#     print("   Ejecuta: pip install fpdf2")
#
# print("\n=== VERIFICACIÓN COMPLETADA ===")
