numeroDeColabs = int(input("Informe o número de colaboradores: "))


a = 0
b = 0
c = 0
d = 0
e = 0


for i in range (numeroDeColabs):
    dia_escolhido = (input("\nInforme o dia da sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): ")).lower()
    if dia_escolhido == "segunda-feira":
        a = a + 1
    elif dia_escolhido == "terça-feira":
        b = b + 1
    elif dia_escolhido == "quarta-feira":
        c = c + 1
    elif dia_escolhido == "quinta-feira":
        d = d + 1
    elif dia_escolhido == "sexta-feira":
        e = e + 1
    else:
        print("Dia inválido! Voce perdeu o seu direito de escolher o dia...")
    

if a > b and a > c and a > d and a > e:
    a = "segunda-feira"
    print(f"\nO dia escolhido pelos colaboradores foi: {a}")

elif b > a and b > c and b > d and b > e:
    b = "terça-feira"
    print(f"\nO dia escolhido pelos colaboradores foi: {b}")

elif c > a and c > b and c > d and c > e:
    c = "quarta-feira"
    print(f"\nO dia escolhido pelos colaboradores foi: {c}")

elif d > a and d > b and d > c and d > e:
    d = "quinta-feira"
    print(f"\nO dia escolhido pelos colaboradores foi: {d}")

elif e > a and e > b and e > c and e > d:
    e = "sexta-feira"
    print(f"\nO dia escolhido pelos colaboradores foi: {e}")

else:
    print("Houve empate e uma nova votação deverá ser realizada com os dias vencedores.")