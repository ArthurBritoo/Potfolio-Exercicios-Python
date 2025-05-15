matriz = [["_","_","_"],["_","_","_"],["_","_","_"]]
vencedor = None
def velhax():
     while True:
        x = int(input("Digite a linha que você vai colocar o X: "))
        xx = int(input("Digite a coluna que você vai colocar o X: "))
        if 1 <= x <= 3 and 1 <= xx <= 3 and matriz[x-1][xx-1] == "_":
            matriz[x-1][xx-1] = "X"
            break
        else:
            print("Escolha outro local ou digite uma posição válida (1-3).")
def velhao():
    while True:
        x = int(input("Digite a linha que você vai colocar o O: "))
        xx = int(input("Digite a coluna que você vai colocar o O: "))
        if 1 <= x <= 3 and 1 <= xx <= 3 and matriz[x-1][xx-1] == "_":
            matriz[x-1][xx-1] = "O"
            break
        else:
            print("Escolha outro local ou digite uma posição válida (1-3).")
def checkvitoria():
    for linha in matriz:
        if linha[0] == linha[1] == linha[2] and linha[0] != '_':
            return linha[0]  
    for i in range(3):
        if matriz[0][i] == matriz[1][i] == matriz[2][i] and matriz[0][i] != '_':
            return matriz[0][i]
    if matriz[0][0] == matriz[1][1] == matriz[2][2] and matriz[0][0] != '_':
        return matriz[0][0]
    if matriz[0][2] == matriz[1][1] == matriz[2][0] and matriz[0][2] != '_':
        return matriz[0][2]


    return None
while vencedor is None:
    for i in range(len(matriz)):
        print(matriz[i])
    velhax()
    vencedor = checkvitoria()
    if vencedor:
        for i in range(len(matriz)):
            print(matriz[i])
        print(f"Jogador {vencedor} venceu!")
        break
    for i in range(len(matriz)):
        print(matriz[i])
    velhao()
    vencedor = checkvitoria()
    if vencedor:
        for i in range(len(matriz)):
            print(matriz[i])
        print(f"Jogador {vencedor} venceu!")
        break
