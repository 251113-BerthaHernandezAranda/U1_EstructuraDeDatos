def calcular_saldo_final(depositos: list, tasa_interes: float) -> float:
    # Caso base: si no hay depósitos, el saldo inicial es 0.0
    if not depositos:
        return 0.0

    # Caso recursivo: calcular el saldo de los años anteriores, sumar el depósito actual y aplicar interés
    saldo_anterior = calcular_saldo_final(depositos[:-1], tasa_interes)
    return (saldo_anterior + depositos[-1]) * (1 + tasa_interes)

depositos_anuales = [1000, 2000, 1500]
tasa = 0.05
print(calcular_saldo_final(depositos_anuales, tasa))