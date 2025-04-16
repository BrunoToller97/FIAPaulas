#importação de funções específica do módulo calc.py
from calc import somar, subtrair
#solicitando valores ao usuário
valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")
#armazenando a soma
soma = somar(valor1, valor2)
#exibindo a soma
subtração = subtrair
print("A soma é {}".format(soma))
print(f"A subtração é de {subtração}")