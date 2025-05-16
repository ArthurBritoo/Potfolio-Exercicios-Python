#Criar matriz aleatória com tamanho informado:
import random
matriz = []
lc = int(input("digite o numero de linhas e colunas: "))
for i in range(lc):
    linha = []
    for j in range(lc):
        linha.append(random.randint(1, 999))
    matriz.append(linha)

print("Matriz Gerada:")
for linha in matriz:
    for num in linha:
        print("{:3d}".format(num), end=" ")
    print()
