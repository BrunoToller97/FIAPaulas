arquivo = open("T:\\Desktop\\USP\\FIAP\\Aulas\\FIAPaulas\\Semeste1\\Fase3\\Texto\\Creme.txt", "r", encoding="UTF-8")

print(type(arquivo))

print(arquivo)

#printar conteudo

print(arquivo.read())

#IMPORTANTE: fechar arquivo
arquivo.close()