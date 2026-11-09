class Nodo:
    # 1. Se necesitan dos guiones bajos antes y después de init
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# CREACIÓN DE UN NODO INDIVIDUAL
nodo_singular = Nodo("Primer Dato")

print(nodo_singular.dato)       # Imprime: Primer Dato
print(nodo_singular.siguiente)  # Imprime: None
