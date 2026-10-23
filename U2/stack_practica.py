# Paso 1: Crear la estructura (Constructor)
pila = []
print("Paso 1: Pila creada")
print(f"Pila inicial: {pila}\n")

# Paso 2: Apilar 10 elementos (Push)
print("Paso 2: Apilando 10 elementos (Push)")
for i in range(1, 11):
    plato = f"Plato {i}"
    pila.append(plato)
    print(f"Agregado: {plato}")

print(f"\nEstado de la pila ({len(pila)} elementos): {pila}\n")

# Paso 3: Consultar el elemento en la Cima (Top / Peek)
print("Paso 3: Consultar la cima (Top / Peek)")
cima = pila[-1]
print(f"Elemento en la cima: {cima}\n")

# Paso 4: Desapilar 4 elementos (Pop)
print("Paso 4: Desapilando 4 elementos (Pop)")
for _ in range(4):
    plato_retirado = pila.pop()
    print(f"Se retiró de la cima: {plato_retirado}")

print(f"\nEstado de la pila tras desapilar: {pila}\n")

# Paso 5: Consultar Tamaño (Size) y Estado Vacío (Empty)
print("Paso 5: Tamaño y Estado Vacío")
tamano = len(pila)
esta_vacia = len(pila) == 0

print(f"Tamaño actual de la pila: {tamano}")
print(f"¿La pila está vacía?: {esta_vacia}\n")

# EXTRA Paso 6: Vaciar la pila por completo
print("EXTRA Paso 6: Vaciar la pila por completo")
while pila:
    plato_retirado = pila.pop()
    print(f"Desapilando: {plato_retirado}")

print(f"\nPila final: {pila}")
print(f"¿La pila está vacía?: {len(pila) == 0}")