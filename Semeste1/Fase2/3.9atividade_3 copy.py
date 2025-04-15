numero_escolhido = int(input("Escolha um número que esteja na sequencia de Fibonacci: "))
i = 1
j = 0
encontrado = False

while i <= numero_escolhido:
    if numero_escolhido == i:
        encontrado = True
    j, i = i, j + i

if encontrado:
    print("Ação bem sucedida!")  
else:
    print("A ação falhou...")
