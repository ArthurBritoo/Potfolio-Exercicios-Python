# 8. Perguntar em que turno a pessoa estuda e mostrar mensagem de saudação apropriada
while True:
    turno = input("Digite o turno do aluno (M-matutino, V-Vespertino, N-Noturno): ").upper()
    if turno == "M":
        print("Bom Dia!")
        break
    elif turno == "V":
        print("Boa Tarde!")
        break
    elif turno == "N":
        print("Boa Noite!")
        break
    else:
        print("Valor Inválido! Digite novamente")
