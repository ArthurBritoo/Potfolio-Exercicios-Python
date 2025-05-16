#Criar matriz com valores do usuário e mostrar dobro dos valores:
matriz = []
lc = int(input("digite o numero de linhas e colunas: "))
for i in range(lc):
    linha = []
    for j in range(lc):
        numero = int(input(f"Digite o número para a posição ({i+1}, {j+1}): "))
        linha.append(numero)
    matriz.append(linha)

print("\nMatriz original:")
for linha in matriz:
    for num in linha:
        print("{:3d}".format(num), end=" ")
    print()

print("\nMatriz dobrada:")
for linha in matriz:
    for num in linha:
        print("{:3d}".format(num*2), end=" ")
    print()
