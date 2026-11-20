# Ejercicio 1: Limpiador de publicaciones repetidas en un Feed
def limpiar_feed(publicaciones: list) -> list:
    if len(publicaciones) <= 1:
        return publicaciones

    if publicaciones[0] == publicaciones[1]:
        return limpiar_feed(publicaciones[1:])
    else:
        return [publicaciones[0]] + limpiar_feed(publicaciones[1:])


# Ejercicio 2: Proyección de Ahorro con Interés Compuesto
def calcular_saldo_final(depositos: list, tasa_interes: float) -> float:
    if not depositos:
        return 0.0

    saldo_anterior = calcular_saldo_final(depositos[:-1], tasa_interes)
    return (saldo_anterior + depositos[-1]) * (1 + tasa_interes)


# Ejercicio 3: Medir la profundidad de un hilo de comentarios
def maxima_profundidad(comentarios: list) -> int:
    if not comentarios:
        return 0

    profundidades = []
    for elem in comentarios:
        if isinstance(elem, list):
            profundidades.append(1 + maxima_profundidad(elem))
        else:
            profundidades.append(1)

    return max(profundidades)


# resultados
if __name__ == "__main__":
    feed = ["Post A", "Post B", "Post B", "Post C", "Post B"]
    print("RESULTADO 1:", limpiar_feed(feed))

    depositos = [1000, 2000, 1500]
    print("RESULTADO 2:", round(calcular_saldo_final(depositos, 0.05), 2))

    hilo = ["Comentario 1", ["Respuesta 1.1", ["Respuesta 1.1.1"]], "Comentario 2"]
    print("RESULTADO 3:", maxima_profundidad(hilo))
