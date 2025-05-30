conteudo = "Há muito tempo atrás, em um lugar muito distante"

#criando arquivo
arquivo = open("T:\\Desktop\\USP\\FIAP\\Aulas\\FIAPaulas\\Semeste1\\Fase3\\Texto\\Nadson.txt", "w", encoding="UTF-8")

#escrevendo conteudo lá dentro
arquivo.write(conteudo)

#fechando
arquivo.close()