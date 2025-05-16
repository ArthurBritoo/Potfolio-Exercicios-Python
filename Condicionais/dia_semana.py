# 9. Ler um número e exibir o dia correspondente da semana
# (1-Domingo, 2-Segunda, etc.), se digitar outro valor deve aparecer valor inválido
dia = int(input("Digite o número do dia da semana (1-7): "))

if dia == 1:
    print("Esse dia é Domingo")
elif dia == 2:
    print("Esse dia é Segunda")
elif dia == 3:
    print("Esse dia é Terça")
elif dia == 4:
    print("Esse dia é Quarta")
elif dia == 5:
    print("Esse dia é Quinta")
elif dia == 6:
    print("Esse dia é Sexta")
elif dia == 7:
    print("Esse dia é Sábado")
else:
    print("Esse dia não existe")
