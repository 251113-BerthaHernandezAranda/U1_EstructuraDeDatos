import datetime
import random

def saludar():
    print("Hola, Bienvenidos")
saludar()

def mostrar_hora():
    hora_actual=datetime.datetime.now().strftime("%H:%M:%S")
    print(f"La hora actual es: {hora_actual}")
mostrar_hora()
#Now() consulta el reloj o la hora del SO
#Strftime convertir la fecha y hora en texto, usando el formato establecido
#f-string la letra f indica a python que procese el texto
#e inserte las variables dentro de las llaves
#{hora_actual} se toma el valor almacenado en la variable de la hora_actual
#y lo reemplaza ahí mismo

#Actividad: Definir dos funciones sin parametros
def lanzar_dado():
    resultado = random.randint(1,6)
    print(f"Has lanzado el dado y salió: {resultado}")
lanzar_dado()
lanzar_dado()

def preguntar_oraculo():
    respuestas = ["¡Sí, totalmente!", "No, ni lo pienses...", "Es probable", "No lo sé, intenta más tarde"]
    prediccion = random.choice(respuestas)
    print(f"El oráculo dice: {prediccion}")

# Llamadas a la función
preguntar_oraculo()
preguntar_oraculo()