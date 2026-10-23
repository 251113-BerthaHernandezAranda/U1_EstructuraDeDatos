from collections import deque
import time

# 1. Inicializar la cola de turnos
cola_turnos = deque()

cola_turnos.append("Turno A01 - ISIDRO ORTIZ RAMIREZ")
cola_turnos.append("Turno A02 - GUADALUPE PEREZ DIAZ")
cola_turnos.append("Turno A03 - JUANA LAZCANO RODRIGUEZ")

# 3. Mostrar turnos emitidos inicialmente
print("Turnos emitidos en la fila del banco:")
for turno in cola_turnos:
    print(f"  - {turno}")

print("\nIniciando atención en ventanilla\n")

# 4. Procesar la atención en ventanilla (Desencolar - FIFO)
while cola_turnos:
    cliente_actual = cola_turnos.popleft()
    print(f"Llamando a ventanilla: {cliente_actual}")
    
    time.sleep(1)
    
    print(f"Atención finalizada: {cliente_actual}")
    print(f"   (Clientes restantes en la fila: {len(cola_turnos)})\n")

print("Se han atendido todos los turnos. Fila vacía.")