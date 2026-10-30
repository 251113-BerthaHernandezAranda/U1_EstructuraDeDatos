import numpy as np
#CON NUMPY
A=np.array([[10,15],[20,5]])
B=np.array([[5,12],[15,8]])

suma = A + B
print("=====================CON NUMPY=====================")
print("Total de productos vendidos (Sábado + Domingo):")
print(suma)
ingreso = 50 * suma
print("Ingreso total en pesos (a 50 pesos por producto):")
print(ingreso)

#PYTHON NATIVO
A_nativa=([[10,15],[20,5]])
B_nativa=([[5,12],[15,8]])

suma_nativa = [[A_nativa[i][j]+B_nativa[i][j] for j in range(len(A_nativa[0]))] for i in range(len(A_nativa))]
print("=====================NATIVO=====================")
print("Total de productos vendidos (Sábado + Domingo):")
print(suma_nativa)
ingreso_nativo = [[A_nativa[i][j] * 50 + B_nativa[i][j] * 50 for j in range(len(A_nativa[0]))] for i in range(len(A_nativa))]
print("Ingreso total en pesos (a 50 pesos por producto):")
print(ingreso_nativo)
