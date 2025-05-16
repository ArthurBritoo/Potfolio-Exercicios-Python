#Programa que pede 5 valores positivos e termina se houver número negativo
for i in range(1, 6):
    numero = int(input("Digite o %dº número inteiro: " % (i)))
    if numero < 0:
        print("O número é negativo")
        break
else:
    print("Os dados foram inseridos com sucesso")
