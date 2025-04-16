valores = [1, 2, 3, 4, 33, 100, 88]

print(f"A lista foi criada assim: {valores}")

# contar os elementos de uma lista (método .count) // passa o valor do elemento para ver quantas vezes ele se repete

contagem = valores.count(1)

print(f"A contagem de números 1 foi de {contagem}")

# inverter a ordem dos index (método .reverse)

valores.reverse()

print(f"A lista inverida ficou assim: {valores}")

# ordenando a lista (método .sort) // para o crescente e passando o parametro (reverse=True) decrescente

valores.sort()

print(f"A lista crescente ficou assim: {valores}")

valores.sort(reverse=True)

print(f"A lista decrescente ficou assim: {valores}")

# tamanho da lista (método len())

quantidade = len(valores)
print(f"A quantidade de elementos na lista é de {quantidade}")

# soma dos valores de uma lista (método sum())

soma = sum(valores)
print(f"A soma dos valores é {soma}")



