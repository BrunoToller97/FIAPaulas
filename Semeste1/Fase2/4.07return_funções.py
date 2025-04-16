def velocidade_media(distancia, tempo):
    float(distancia)
    float(tempo)
    vm = distancia / tempo 

    return vm


variavel = velocidade_media(100, 2) + 100
print(f"A velocidade média foir de {variavel}")

velocidades_medias = []

for dia in ["segunda", "terça", "quarta", "quinta", "sexta"]:
    dist = float(input(f"Por favor, informe a distancia percorrida na {dia}: "))
    temp = float(input(f"Informe o tempo da viagem em horas no {dia}: "))
    
    velocidades_medias.append(velocidade_media(dist, temp))

print(velocidades_medias)