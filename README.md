# 🐒 Python para Monos

Bienvenido a **Python para Monos**, un repositorio diseñado para entrenar tu lógica de programación en Python de forma progresiva. El objetivo de este material es llevarte desde las bases absolutas hasta la capacidad de construir scripts avanzados que resuelvan problemas del mundo real.

## 📂 Estructura del Repositorio

```
Python-para-monos/
├── README.md
├── modulo_1_facil/          # Actividades 01-10
├── modulo_2_intermedio/     # Actividades 11-20
├── modulo_3_dificil/        # Actividades 21-30
├── proyecto_final/          # Generador de Facturas
└── datos/                   # Archivos de soporte (.txt, .csv)
```

---

## 🟢 Módulo 1: Fácil (Fundamentos y Lógica Básica)

En este módulo afianzarás las bases. Aprenderás a declarar variables, controlar el flujo de información, tomar decisiones, repetir acciones y manejar texto y colecciones de datos.

| # | Archivo | Tema |
|---|---------|------|
| 01 | `01_variables.py` | Tipos de datos básicos y su impresión en consola |
| 02 | `02_operadores.py` | Operaciones matemáticas básicas |
| 03 | `03_condicionales.py` | Uso de `if`, `elif`, `else` |
| 04 | `04_calculadora_basica.py` | Ingreso de datos por consola (`input`) |
| 05 | `05_ciclo_while.py` | Contador y control de bucles condicionales |
| 06 | `06_ciclo_for.py` | Iteración estructurada sobre elementos |
| 07 | `07_manipulacion_strings.py` | Métodos de texto (`upper`, `lower`, `strip`, `replace`) |
| 08 | `08_listas_basicas.py` | Colecciones de datos, `append` y `remove` |
| 09 | `09_formateo_cadenas.py` | f-strings para textos dinámicos |
| 10 | `10_menu_consola.py` | Menú interactivo infinito con ciclos y condicionales |

---

## 🟡 Módulo 2: Intermedio (Funciones y Estructuras de Datos)

Aquí el código se vuelve modular y organizado. Comenzarás a encapsular lógica en funciones, manejar datos complejos con diccionarios y a trabajar con archivos externos.

| # | Archivo | Tema |
|---|---------|------|
| 11 | `11_funciones_basicas.py` | Funciones con parámetros y `return` |
| 12 | `12_diccionarios.py` | Pares clave-valor |
| 13 | `13_lista_diccionarios.py` | Listas que contienen diccionarios |
| 14 | `14_manejo_errores.py` | Control de excepciones `try/except` |
| 15 | `15_modulos_estandar.py` | Módulo `datetime` para fechas y horas |
| 16 | `16_lectura_txt.py` | Lectura de archivos de texto línea por línea |
| 17 | `17_escritura_txt.py` | Escritura de resultados en un archivo `.txt` |
| 18 | `18_formato_columnas.py` | Alineación de texto con `ljust` y `rjust` |
| 19 | `19_calculos_iterativos.py` | Subtotal, porcentaje y total sobre listas numéricas |
| 20 | `20_validador_datos.py` | Funciones de limpieza y validación de datos |

---

## 🔴 Módulo 3: Difícil (Archivos Estructurados y Reportes)

En este nivel, los datos sueltos se convierten en información estructurada. Te enfocarás en extraer, transformar y presentar datos con precisión, incluyendo la generación de documentos PDF.

| # | Archivo | Tema |
|---|---------|------|
| 21 | `21_lectura_csv_basica.py` | Parseo manual de CSV con `split(',')` |
| 22 | `22_modulo_csv.py` | Librería integrada `csv` |
| 23 | `23_extraccion_datos.py` | Extracción de columnas específicas de un CSV |
| 24 | `24_limpieza_datos.py` | Conversión de tipos (strings a `float`) |
| 25 | `25_agrupacion_datos.py` | Consolidación de elementos repetidos |
| 26 | `26_generacion_identificadores.py` | Códigos únicos con `datetime` y `random` |
| 27 | `27_entorno_virtual.py` | Entornos virtuales y `pip install` |
| 28 | `28_pdf_basico.py` | Crear un PDF con una librería externa (`fpdf2`) |
| 29 | `29_coordenadas_pdf.py` | Posicionamiento de texto en un lienzo PDF |
| 30 | `30_orquestador_funciones.py` | Script que orquesta múltiples funciones en secuencia |

---

## 🚀 Proyecto Final: Generador de Facturas de Supermercado

Un script de ejecución lineal que:
1. Lee un archivo `compras.csv` (producto, cantidad, precio unitario).
2. Calcula subtotal, IVA (19%) y total de la compra.
3. Genera automáticamente un archivo `.pdf` que simula una tirilla de supermercado.

**Ubicación**: `proyecto_final/generar_factura.py`

---

## ⚙️ Entorno de Desarrollo

### Requisitos previos
- Python 3.8 o superior
- Ubuntu (o cualquier distribución Linux)
- IDE Antigravity (o cualquier editor de texto)

### Instalación

```bash
# 1. Clona este repositorio
git clone https://github.com/tu-usuario/Python-para-monos.git
cd Python-para-monos

# 2. (Opcional) Crea un entorno virtual para el Módulo 3 y Proyecto Final
python3 -m venv venv
source venv/bin/activate

# 3. Instala las dependencias para PDF (solo necesario desde la actividad 28)
pip install fpdf2
```

### Ejecución de actividades

```bash
# Ejecuta cada actividad individualmente
python3 modulo_1_facil/01_variables.py
python3 modulo_2_intermedio/11_funciones_basicas.py
python3 modulo_3_dificil/21_lectura_csv_basica.py

# Ejecuta el proyecto final
python3 proyecto_final/generar_factura.py
```

---

## 📖 Formato de cada actividad

Cada archivo `.py` contiene:
1. 📚 **Teoría**: Explicación clara y profunda del tema.
2. 📝 **Instrucciones**: Descripción exacta del ejercicio a resolver.
3. ✅ **Criterios de Aceptación**: Qué debe cumplir tu código para estar correcto.
4. 💡 **Solución de referencia**: Código comentado al final para que puedas verificar tu trabajo.

---

## 🤝 Contribuciones

Este es un proyecto de aprendizaje personal. Si encuentras errores o quieres sugerir mejoras, abre un *Issue* o envía un *Pull Request*.

---

## 📄 Licencia

Este proyecto es de uso educativo y libre.
