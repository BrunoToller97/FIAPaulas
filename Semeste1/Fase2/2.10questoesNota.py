nota = int(input("coloque uma nota:"))


if nota >= 0 and nota <= 10 :
    print("essa nota é válida!!")
    print(str(bool(nota)))
else:
    print("essa nota não é válida")