matriz=[
    [1,2],
    [3,4]
]

def suma(matriz, fila, columna):
    if(fila==2):
        return 0
    if(columna==2):
        return suma(matriz, fila+1, 0)
    else:
        return matriz[fila][columna]+suma(matriz,fila, columna+1)
print("La suma total de la matriz es: ", suma(matriz,0,0))