arquivo = open("T:\\Desktop\\USP\\FIAP\\Aulas\\FIAPaulas\\Semeste1\\Fase3\\Texto\\Creme.txt", "r", encoding="UTF-8")

print(type(arquivo))

print(arquivo)

#printar conteudo

#print(arquivo.read())

#ver só uma linha
#print(arquivo.readline())

#ver só uma linha Segunda
#print(arquivo.readline())

#ver só uma linha Terceira (já separa em linhas em branco)
#print(arquivo.readline())

#passando conteudo para uma lista

lista_linha = arquivo.readlines()

print(type(lista_linha))

print(lista_linha)

#devolve uma lista, logo é possivel manipulá-la como tal

lista_linha.sort()

print(lista_linha)

#loop

for linha in lista_linha:
    print(linha)


#IMPORTANTE: fechar arquivo
arquivo.close()