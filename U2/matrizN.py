#CREACIÓN DE MATRIZ DE 3x3
matriz=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
#ACCESO A ELEMENTOS DE LA MATRIZ (FILA)(COLUMNA)
print(matriz[1][2])#imprimiría la fila indice 1, columna 2
#MODIFICAR UN ELEMENTO
matriz[0][0]=100
#RECORRER LA MATRIZ
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()