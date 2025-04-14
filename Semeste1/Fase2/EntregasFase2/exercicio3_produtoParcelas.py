valorDivida = float(input("Digite o valor da dívida: R$ "))
e = 0

for i in [0, 10, 15, 20, 25]:
    if i == 0:
        print(f"Total:R$ {valorDivida:.2f} Juros:R$ 0.00 Número de parcelas:1 Valor da parcela:R$ {valorDivida:.2f}")
    else:
        e = e + 3
        juros = valorDivida * i / 100
        valorFinal = valorDivida + juros
        parcela = (valorFinal / e)
        print(f"Total:R$ {valorFinal:.2f} Juros:R$ {juros:.2f} Número de parcelas:{e} Valor da parcela:R$ {parcela:.2f}")