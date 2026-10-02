calificaciones =[9,10,7,8,10,5,9,8,8,10,9,8,7,10,9]
a = len(calificaciones)
swapped = True
while swapped:
    swapped = False
    for i in range(a-1):
        if calificaciones[i]>calificaciones[i+1]:
            calificaciones[i],calificaciones[i+1]=calificaciones[i+1],calificaciones[i]
            swapped = True
print("Orden Ascendente: ", calificaciones)

calificacionesD =[9,10,7,8,10,5,9,8,8,10,9,8,7,10,9]
d = len(calificacionesD)
swapped = True
while swapped:
    swapped = False
    for i in range(d-1):
        if calificacionesD[i]<calificacionesD[i+1]:
            calificacionesD[i],calificacionesD[i+1]=calificacionesD[i+1],calificacionesD[i]
            swapped = True
print("Orden Descendente: ", calificacionesD)


