inimigos = [(10, 5), (8, 9), (3, 3)]

while len(inimigos) > 0:
    x = int(input("Informe o valor do eixo X: "))
    y = int(input("Informe o valor do eixo Y: "))
    if (x, y) in inimigos:
        print("Você acertou o inimigo!")
        inimigos.remove((x, y))

    else:
        print("Você errou o inimigo!")

    print(f"Agora restam {len(inimigos)}") 