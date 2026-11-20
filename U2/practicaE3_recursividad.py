def maxima_profundidad(comentarios: list) -> int:
    # Caso base: si la lista está vacía, la profundidad es 0
    if not comentarios:
        return 0

    profundidades = []

    # Caso recursivo: evaluar cada elemento del nivel actual
    for elem in comentarios:
        if isinstance(elem, list):
            # Si es una sublista, sumamos 1 al máximo de su contenido
            profundidades.append(1 + maxima_profundidad(elem))
        else:
            # Si es un comentario simple (str), su profundidad base aquí es 1
            profundidades.append(1)

    # Retornar la mayor profundidad encontrada en este nivel
    return max(profundidades)

hilo = ["Comentario 1", ["Respuesta 1.1", ["Respuesta 1.1.1"]], "Comentario 2"]
print("RESULTADO 3:", maxima_profundidad(hilo))