minutos_atuais = int(input("Escreva os minutos neste momento: "))
i = minutos_atuais

while (i > 1):
    i = i - 1
    minutos_atuais = minutos_atuais * i
    print(minutos_atuais)

print(f"A senha é LIBERDADE{minutos_atuais}")