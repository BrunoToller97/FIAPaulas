rm = input("Insira seu RM ")
idade = int(input("Insira sua idade "))
if idade >= 18:
    print("Sua participação foi autorizada, aluno de RM {}!".format(rm))
    print("Mais informações serão enviadas para seu e-mail cadastrado!")
else:
    print("Voce é menor de idade! Saia daqui!")