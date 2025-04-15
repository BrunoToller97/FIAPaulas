quantidade_alimentos = int(input("Quantos alimentos você comeu hoje?"))
numero_de_caloria = 0
i = 0

while (i != quantidade_alimentos):
    i = i + 1
    input("Informe o nome do alimento consumido: ")
    calorias_do_alimento = int(input("Informe a quantidade de calorias do referido alimento:"))
    numero_de_caloria = numero_de_caloria + calorias_do_alimento

print(f"A quantidade de calorias consumida no dia foi de {numero_de_caloria}")