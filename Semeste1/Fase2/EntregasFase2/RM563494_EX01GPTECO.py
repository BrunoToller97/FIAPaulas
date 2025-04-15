numeroDeColabs = int(input("Informe o número de colaboradores: "))

contagem_dias = {
    "segunda-feira": 0,
    "terça-feira": 0,
    "quarta-feira": 0,
    "quinta-feira": 0,
    "sexta-feira": 0
}

for i in range (numeroDeColabs):
    dia = (input("\nInforme o dia da sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): ")).lower()
    contagem_dias[dia] += 1

max_votos = max(contagem_dias.values())
dias_vencedores = [dia for dia, votos in contagem_dias.items() if votos == max_votos]

if len(dias_vencedores) > 1:
    print("\nHouve um empate entre os seguintes dias:")
    for dia in dias_vencedores:
        print(f"- {dia}")
else:
    print(f"\nO dia escolhido pelos colaboradores foi: {dias_vencedores[0]}")
