import json

contatos = {
    "Clark Kent":{
       "Celular":"123456",
       "Email":"super@krypton.com"
    },
    "Bruce Wayne":{
       "Celular":"654321",
       "Email":"bat@caverna.com.br"
    }
 }


#convertendo em e string para json / argumento identitaçao / tirar a prevençao de simbolos, acentos, etc
texto_contatos = json.dumps(contatos, indent=4, ensure_ascii=False)



#criando arquivo
arquivo = open("T:\\Desktop\\USP\\FIAP\\Aulas\\FIAPaulas\\Semeste1\\Fase3\\Texto\\Cremosa.json", "w", encoding="UTF-8")

#escrevendo conteudo lá dentro
arquivo.write(texto_contatos)

#funciona a base de dicionários

#fechando
arquivo.close()