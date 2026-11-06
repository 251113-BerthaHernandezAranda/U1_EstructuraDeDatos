def torres_de_hanoi(n, origen, destino, auxiliar):
    # Caso base: si solo queda un disco, se mueve directamente
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    
    # 1. Mover los n-1 discos superiores del origen al auxiliar
    torres_de_hanoi(n - 1, origen, auxiliar, destino)
    
    # 2. Mover el disco restante (el más grande) del origen al destino
    print(f"Mover disco {n} de {origen} a {destino}")
    
    # 3. Mover los n-1 discos del auxiliar al destino
    torres_de_hanoi(n - 1, auxiliar, destino, origen)

# --- Ejemplo de uso ---
# Definimos el número de discos
numero_de_discos = 3

print(f"Pasos para resolver las Torres de Hanói con {numero_de_discos} discos:")
torres_de_hanoi(numero_de_discos, 'Torre A', 'Torre C', 'Torre B')
