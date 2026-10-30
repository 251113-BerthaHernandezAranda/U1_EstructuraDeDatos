def factorial(n):
    # Caso base: cuando n es 0 o 1, la recursión se detiene
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: el número multiplicado por el factorial del anterior
    else:
        return n * factorial(n - 1)

# Probar la función
resultado = factorial(5)
print(f"El factorial de 5 es: {resultado}")  # Salida: 120
