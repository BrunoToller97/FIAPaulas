quantidade_de_transacoes = int(input("Quantos transações voce fez hoje? "))
valor_total_transacoes = 0
i = 0

while (i != quantidade_de_transacoes):
    i = i + 1
    valor_da_transacao = float(input(f"Informe o valor da transacao número {i}: "))
    valor_total_transacoes = valor_total_transacoes + valor_da_transacao

media_transacoes = valor_total_transacoes / i

print(f"O valor total de transacoes no dia foi de {valor_total_transacoes:.2f}")
print(f"O valor médio das transacoes no dia foi de {media_transacoes:.2f}")