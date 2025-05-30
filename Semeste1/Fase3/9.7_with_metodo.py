conteudo = "\nCrise de meia idade"

#criando arquivo
with open("T:\\Desktop\\USP\\FIAP\\Aulas\\FIAPaulas\\Semeste1\\Fase3\\Texto\\Nadson.txt", "a", encoding="UTF-8") as arquivo:

    #escrevendo conteudo lá dentro
    arquivo.write(conteudo)

    #fechando
    arquivo.close()