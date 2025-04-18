#importação do módulo calc.py
import rascunho
#solicitando valores ao usuário
valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")
#armazenando a soma
soma = rascunho.somar(valor1, valor2)
#exibindo a soma
print("A soma é {}".format(soma))