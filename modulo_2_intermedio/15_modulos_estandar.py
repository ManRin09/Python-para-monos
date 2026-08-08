"""
========================================
🐒 Python para Monos
Módulo 2 — Actividad 15: Módulos Estándar (datetime)
========================================

📚 TEORÍA:

Python viene con una enorme BIBLIOTECA ESTÁNDAR: una colección de módulos
listos para usar que no necesitas instalar. Solo tienes que IMPORTARLOS.

IMPORTAR UN MÓDULO:
    import datetime                     # Importa el módulo completo
    from datetime import datetime       # Importa una parte específica
    from datetime import datetime as dt # Importa con un alias

EL MÓDULO datetime:
Es el módulo estándar para trabajar con fechas y horas.

OBTENER LA FECHA Y HORA ACTUAL:
    from datetime import datetime

    ahora = datetime.now()
    print(ahora)  →  2025-08-08 14:30:45.123456

ACCEDER A COMPONENTES INDIVIDUALES:
    ahora = datetime.now()
    ahora.year     →  2025       # Año
    ahora.month    →  8          # Mes (1-12)
    ahora.day      →  8          # Día (1-31)
    ahora.hour     →  14         # Hora (0-23)
    ahora.minute   →  30         # Minuto (0-59)
    ahora.second   →  45         # Segundo (0-59)

FORMATEAR FECHAS con strftime() (String Format Time):
Convierte un objeto datetime a un STRING con el formato que quieras:

    ahora.strftime("%d/%m/%Y")          →  "08/08/2025"
    ahora.strftime("%Y-%m-%d")          →  "2025-08-08"
    ahora.strftime("%d de %B de %Y")    →  "08 de August de 2025"
    ahora.strftime("%H:%M:%S")          →  "14:30:45"
    ahora.strftime("%I:%M %p")          →  "02:30 PM"

    Códigos de formato comunes:
    %Y = Año 4 dígitos     %y = Año 2 dígitos
    %m = Mes (01-12)       %B = Nombre del mes    %b = Mes abreviado
    %d = Día (01-31)
    %H = Hora 24h          %I = Hora 12h          %p = AM/PM
    %M = Minuto            %S = Segundo

CREAR UNA FECHA ESPECÍFICA:
    fecha = datetime(2025, 12, 25, 10, 30, 0)  # 25 dic 2025, 10:30:00
    print(fecha)  →  2025-12-25 10:30:00

OPERACIONES CON FECHAS usando timedelta:
    from datetime import datetime, timedelta

    hoy = datetime.now()
    manana = hoy + timedelta(days=1)
    hace_una_semana = hoy - timedelta(days=7)
    en_3_horas = hoy + timedelta(hours=3)

CALCULAR DIFERENCIA ENTRE FECHAS:
    fecha_1 = datetime(2025, 1, 1)
    fecha_2 = datetime(2025, 8, 8)
    diferencia = fecha_2 - fecha_1
    print(diferencia.days)  →  219  (días de diferencia)

SOLO FECHA (sin hora) con date:
    from datetime import date
    hoy = date.today()
    print(hoy)  →  2025-08-08

📝 INSTRUCCIONES:

Crea un script que trabaje con fechas y horas:

1. Importa lo necesario del módulo datetime.

2. Obtén e imprime la fecha y hora actual en estos 3 formatos:
   a) "08/08/2025 14:30:45"          (formato DD/MM/YYYY HH:MM:SS)
   b) "2025-08-08"                    (formato ISO)
   c) "Viernes, 08 de Agosto de 2025" (formato largo — no importa si el nombre
      del mes sale en inglés)

3. Pide al usuario su fecha de nacimiento (año, mes y día como 3 inputs separados).
   Calcula e imprime:
   a) Su edad en años (aproximada: diferencia de años).
   b) Cuántos días han pasado desde que nació.
   c) Cuántos días faltan para su próximo cumpleaños.

4. Imprime la fecha de dentro de exactamente 100 días usando timedelta.

✅ CRITERIOS DE ACEPTACIÓN:
- Se importa correctamente el módulo datetime.
- Se usa datetime.now() para obtener la fecha actual.
- Se usa strftime() para formatear la fecha en al menos 3 formatos.
- Se usa input() para recibir la fecha de nacimiento.
- Se usa timedelta para calcular fechas futuras.
- Se calcula la diferencia entre fechas (.days).
- No se deben usar clases ni objetos propios.
========================================
"""

# === ZONA DE CÓDIGO DEL ESTUDIANTE ===
# Escribe tu solución aquí abajo:



# === FIN DE LA ZONA DEL ESTUDIANTE ===


# ============================================
# 💡 SOLUCIÓN DE REFERENCIA (No espiar antes de intentarlo)
# ============================================
# from datetime import datetime, timedelta
#
# # 2. Fecha y hora actual en 3 formatos
# ahora = datetime.now()
# print("=== FECHA Y HORA ACTUAL ===")
# print(f"a) {ahora.strftime('%d/%m/%Y %H:%M:%S')}")
# print(f"b) {ahora.strftime('%Y-%m-%d')}")
# print(f"c) {ahora.strftime('%A, %d de %B de %Y')}")
#
# # 3. Fecha de nacimiento del usuario
# print("\n=== CALCULADORA DE EDAD ===")
# anio = int(input("¿En qué año naciste? "))
# mes = int(input("¿En qué mes (1-12)? "))
# dia = int(input("¿Qué día (1-31)? "))
#
# fecha_nacimiento = datetime(anio, mes, dia)
# diferencia = ahora - fecha_nacimiento
#
# # a) Edad aproximada
# edad = ahora.year - fecha_nacimiento.year
# if (ahora.month, ahora.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
#     edad -= 1
# print(f"\na) Tu edad aproximada: {edad} años")
#
# # b) Días desde que nació
# print(f"b) Han pasado {diferencia.days} días desde que naciste")
#
# # c) Próximo cumpleaños
# proximo_cumple = datetime(ahora.year, mes, dia)
# if proximo_cumple < ahora:
#     proximo_cumple = datetime(ahora.year + 1, mes, dia)
# dias_para_cumple = (proximo_cumple - ahora).days
# print(f"c) Faltan {dias_para_cumple} días para tu próximo cumpleaños 🎂")
#
# # 4. Fecha dentro de 100 días
# en_100_dias = ahora + timedelta(days=100)
# print(f"\n📅 Dentro de 100 días será: {en_100_dias.strftime('%d/%m/%Y')}")
