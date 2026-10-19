from collections import deque
cola = deque()
#Agregar elementos a la cola (encolar)
cola.append("Cliente 1")
cola.append("Cliente 2")
cola.append("Cliente 3")
#Sacar el primer elemento que llegó (Desencolar)
atendido = cola.popleft()
#MOSTRAR RESULTADOS
print("Atendido", atendido)
print("Cola restante:", cola)