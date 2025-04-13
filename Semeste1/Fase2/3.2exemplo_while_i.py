#criação da variável com um valor inicial
i = 0
resposta = "0"
#enquanto a variável contadora não chegar ao limite
while (i<10) and (resposta != "42"):
    #para cada uma das repetições uma mensagem é exibida
    resposta = input("Qual a resposta para a vida, o universo e tudo mais?")
    print("Mais uma mensagem, com i valendo: {}".format(i))
    i = i + 1

#mistura dos dois exemplos
