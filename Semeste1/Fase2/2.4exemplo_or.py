ValorDaCompra = float(input("Digite o valor da compra: "))
Cupom = input("Digite o cupom: ")

if ValorDaCompra >= 100 or Cupom == "PRIMEIRACOMPRA":
    ValorDoDesconto = ValorDaCompra * 0.1
    ValorDaCompra = ValorDaCompra * 0.9
    print(f"(Desconto de: R$ {ValorDoDesconto})")
else:
    print("(Compra sem desconto)")
print(f"Valor da compra: R$ {ValorDaCompra}.")