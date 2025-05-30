#criando um dicionario com dados
dicionario = {
    "Yoda":"Mestre Jedi", 
    "Mace Windu": "Mestre Jedi", 
    "Anakin Skywalker":"Cavaleiro Jedi", 
    "R2-D2":"Dróide", 
    "Dex":"Balconista",
    "Droids" : ["grego", "troiano", "nadson", "abacaxi", "urubu"]
}


#método que dá erro quando nao ha a chave
print(dicionario["Droids"])

#previnir isso
print(dicionario.get("André"))

#ve todas as chaves em lista
print(dicionario.keys())

#ve todas os valores em lista
print(dicionario.values())

#exibir por lista chabes
for chave in dicionario.keys():
    print(chave)

#exibir valores
for chave in dicionario.keys():
    print(dicionario[chave])

#exibir chave e valor
print(dicionario.items())

#exibir chave e valor
print(dicionario.items())

#desempacotar
for item in dicionario.items():
    nome, categoria = item
    print(f"Meu personagem é o {nome} de categoria {categoria}")

#ou mais simples

for nome, categoria in dicionario.items():
    print(f"Meu personagem é o {nome} de categoria {categoria}")