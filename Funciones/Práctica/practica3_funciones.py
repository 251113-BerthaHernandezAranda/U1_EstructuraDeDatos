#PRACTICA DE LABORATORIO "REGISTRO Y EVALUACIÓN DE CALIFICACIONES"

#1.mostrar_encabezado_escuela()(Sin parámtros)
def mostrar_encabezado_escuela():
    print("========================================")
    print("         INSTITUTO X         ")
    print("  REPORTE DE CALIFICACIONES  ")
    print("========================================")
    print("")

#2. obtener_nota_minima_aprobatoria()(Sin parámetros)
def obtener_nota_minima_aprobatoria():
    return 6.0

#3. evaluar_rendimiento(nota_final)(Con 1 parámetro)
def evaluar_rendimiento(nota_final):
    if nota_final < 7.0:
        return "Reprobado"
    elif nota_final >= 7.0 and nota_final <= 9.4:
        return "Aprobado"
    elif nota_final >= 9.5 and nota_final <= 10.0:
        return "Excelente"
    else:
        return "ERROR: Nota fuera de rango"

#4. calcular_promedio_ponderado(nota_examenes, nota_tareas)
def calcular_promedio_ponderado(nota_examenes, nota_tareas):
    promedio_ponderado = (nota_examenes * 0.7) + (nota_tareas * 0.3)
    return round(promedio_ponderado, 1)

#5. generar_boleta(nombre_alumno, nota_examenes, nota_tareas) (Con 3 parámetros)
def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tareas)
    nota_minima = obtener_nota_minima_aprobatoria()
    estado_academico = evaluar_rendimiento(nota_final)
    
    necesita_extraordinario = "Si" if nota_final < nota_minima else "No"

    mostrar_encabezado_escuela()
    print(f"Boleta de Calificaciones de {nombre_alumno}")
    print(f"Nota Final: {nota_final}")  
    print(f"Estado Académico: {estado_academico}")
    print(f"¿Necesita examen extraordinario?: {necesita_extraordinario}")
    print("")
generar_boleta("Juan Pérez", 8.5, 9.2)  
