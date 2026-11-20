def limpiar_feed(publicaciones: list) -> list:
    # Caso base: 0 o 1 elementos no pueden tener duplicados consecutivos
    if len(publicaciones) <= 1:
        return publicaciones

    # Caso recursivo: comparar los dos primeros elementos
    if publicaciones[0] == publicaciones[1]:
        # Si son iguales, se omite el primero y se evalúa desde el segundo
        return limpiar_feed(publicaciones[1:])
    else:
        # Si son diferentes, se conserva el primero y se concatena el resto
        return [publicaciones[0]] + limpiar_feed(publicaciones[1:])

feed = ["Post A", "Post B", "Post B", "Post C", "Post B"]
print(limpiar_feed(feed))