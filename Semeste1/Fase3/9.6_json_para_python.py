import json

#Ler arquivo
arquivo = open("T:\\Desktop\\USP\\FIAP\\Aulas\\FIAPaulas\\Semeste1\\Fase3\\Texto\\Cremosa.json", "r", encoding="UTF-8")


#Veio como String, mas precisa ser lido melhoer pelo python
#Assim volta para dicionário
dicionario = json.loads(arquivo.read())

#fechando
arquivo.close()

#consultar ele especificamente
print(dicionario["Clark Kent"])