#CREACIÓN DE MATRIZ DE 2x2
matriz=[
    [1,2],
    [3,4]
]

def suma(matriz, fila=0, columna=0):
    if fila == len(matriz):
        return 0
    if columna == len(fila, matriz):
        return suma(matriz, fila+1, 0)

    return matriz(fila[i],col[j]+suma(matriz,fila, columna +1))

salida = suma(matriz)
print("La suma total de la matriz es: ", salida)