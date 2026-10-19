estudiantes = ["Ana", "Carlos", "Diana"]
print(f"1.Lista inicial: {estudiantes}")

estudiantes.append("Elena")
estudiantes.insert(1,"Beatriz")
print(f"2.Lista tras inserciones: {estudiantes}")
print(f"3.Búsqueda por indice: ")

#print(f"Lista actualizada: {estudiantes}")

print(f"Estudiante en el índice 0: {estudiantes[0]}")
print(f"Estudiante en el índice 2: {estudiantes[2]}")

print(f"Diana se encuentra en el indice: {estudiantes.index("Diana")}")

print(f"4.Resultados de Slicing: ")

#estudiantes.Slicing([0:3:0])
#print(estudiantes)
print(f" segundo punto: {estudiantes[:3]}")
print(f"Lista totalmente invertida: {estudiantes[::-1]}")