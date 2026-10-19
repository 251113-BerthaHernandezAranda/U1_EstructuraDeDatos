from collections import deque
import time

cola_reproduccion=deque()

#EL USUARIO AGREGA CANCIONES
cola_reproduccion.append("1.Antología")
cola_reproduccion.append("2.Historia de amor")
cola_reproduccion.append("3.Historia entre tus dedos")

#MOSTRAR LAS CANCIONES EN ESPERA
print("Canciones en espera: ")
for cancion in cola_reproduccion:
    print("_", cancion)
    print("iniciando reproducción")

#EL REPRODUCTOR PROCESA LA COLA CANCIÓN POR CANCIÓN(DESENCOLAR)
while cola_reproduccion:
    cancion_actual=cola_reproduccion.popleft()
    print(f"Soñando ahora{cancion_actual}")
    time.sleep(1) #SIMULA LA DURACIÓN DEL TEMA
    print(f"Finalizó:{cancion_actual}")
    #MUESTRA CUANTAS CANCIONES QUEDAN EN LA COLA
    print(f"Quedan{len(cola_reproduccion)}) canciones en la cola)")
    print("La cola de reproducción ha terminado.")