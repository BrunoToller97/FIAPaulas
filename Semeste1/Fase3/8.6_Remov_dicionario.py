dicionario = {
    "Yoda":"Mestre Jedi", 
    "Mace Windu": "Mestre Jedi", 
    "Anakin Skywalker":"Cavaleiro Jedi", 
    "R2-D2":"Dróide", 
    "Dex":"Balconista",
    "Droids" : ["grego", "troiano", "nadson", "abacaxi", "urubu"]
}

print(dicionario)


#Primeira forma
dicionario.pop("Yoda")

print(dicionario)

#segunda forma (tira o ultimo item)
dicionario.popitem()

print(dicionario)

#terceira (limpar tudo)
dicionario.clear()

print(dicionario)