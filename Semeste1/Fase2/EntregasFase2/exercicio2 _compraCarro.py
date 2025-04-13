ValorCarro = float(input("Digite o preço do carro: "))

# À vista
print(f"O preço final à vista com desconto de 20% é: R$ {ValorCarro * 0.80:.2f}")

# Parcelado
for i in range (6, 61, 6):
    valor_total = ValorCarro + (ValorCarro * i * 0.005) 
    parcela = (valor_total / i)
    print(
        f"O preço final parcelado em {i} X é de: R$ {valor_total:.2f} com parcelas de R$ {parcela:.2f}".replace(".", ",")
    )