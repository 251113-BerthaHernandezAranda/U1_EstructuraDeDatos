def calcular_area_triangulo(base,altura):
    area=(base*altura)/2
    return area
resultado = calcular_area_triangulo(10,5)
print(f"El área del triángulo es:{resultado}")

def saludar_persona(nombre,edad):
    print(f"Hola {nombre}, tienes {edad} años.")
saludar_persona("Elena", 28)


#Actividad: Definir dos funciones con parametros
def sumar(a,b):
    print(f"El resultado de la suma es: {a+b}")
sumar(20,10)

def promedio(suma_calificaciones, total_materias):
    resultado_promedio = suma_calificaciones / total_materias
    return resultado_promedio
promedio_ana = promedio(47,5)
print(f"El promedio de Ana es: {promedio_ana}")