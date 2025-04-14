numeroInvest = 0

while numeroInvest != 1 and numeroInvest != 2 and numeroInvest != 3:
    print(
        "Escolha o tipo de investimento:"
        "\n1. CDB"
        "\n2. LCI"
        "\n3. LCA"
        )

    numeroInvest = int(input("Digite o tipo de investimento (1, 2 ou 3): "))

    if numeroInvest == 1:
        valorResgate = float(input("Digite o valor a ser resgatado: "))
        dias = int(input("Digite o número de dias que o valor permaneceu investido: "))
        if dias < 181:
            valorImposto = valorResgate * 0.225
            print(f"O valor do imposto a ser pago é de: R$ {valorImposto:.2f}")
        elif dias >= 181 and dias <=720:
            valorImposto = valorResgate * 0.175
            print(f"O valor do imposto a ser pago é de: R$ {valorImposto:.2f}")
        else:
            valorImposto = valorResgate * 0.15
            print(f"O valor do imposto a ser pago é de: R$ {valorImposto:.2f}")

    elif numeroInvest == 2 or numeroInvest == 3:
        valorResgate = float(input("Digite o valor a ser resgatado: "))
        dias = int(input("Digite o número de dias que o valor permaneceu investido: "))
        print("Não há imposto a ser pago.")

    else:
        print("Valor inválido.")
