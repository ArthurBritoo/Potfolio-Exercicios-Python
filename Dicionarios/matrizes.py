#✅ Criar uma matriz 3x3 de números inteiros e imprimir:
#A matriz completa
#A soma dos números ímpares
#A soma dos números pares
pares = []
impares = []
matriz = {
    1: {1: 1, 2: 2, 3: 3},
    2: {1: 4, 2: 5, 3: 6},
    3: {1: 7, 2: 8, 3: 9}
}
print(matriz)
for i in matriz:
  for j in matriz[i]:
    if matriz[i][j] % 2 == 0:
      pares.append(matriz[i][j])
    else:
      impares.append(matriz[i][j])
print(sum(pares))
print(sum(impares))

#✅ Multiplicação de matrizes:
#Solicitar as dimensões das matrizes (linhas e colunas).
#Gerar valores aleatórios para as matrizes.
#Multiplicar as matrizes e imprimir o resultado.
import random
nmrlinha_A = int(input("Qual o número de linhas da Matriz A: "))
nmrcoluna_A = int(input("Qual o número de colunas da Matriz A: "))
nmrlinha_B = nmrcoluna_A
nmrcoluna_B = int(input("Qual o número de colunas da Matriz B: "))
matriz_A = {}
for i in range(nmrlinha_A):
    matriz_A[f"linha{i}"] = {}
    for j in range(nmrcoluna_A):
        matriz_A[f"linha{i}"][f"coluna{j}"] = random.randint(1, 10)
matriz_B = {}
for i in range(nmrlinha_B):
    matriz_B[f"linha{i}"] = {}
    for j in range(nmrcoluna_B):
        matriz_B[f"linha{i}"][f"coluna{j}"] = random.randint(1, 10)
matriz_C = {}
for i in range(nmrlinha_A):
    matriz_C[f"linha{i}"] = {}
    for j in range(nmrcoluna_B):
        matriz_C[f"linha{i}"][f"coluna{j}"] = 0
for i in range(nmrlinha_A):
    for j in range(nmrcoluna_B):
        for k in range(nmrcoluna_A):
            matriz_C[f"linha{i}"][f"coluna{j}"] += matriz_A[f"linha{i}"][f"coluna{k}"] * matriz_B[f"linha{k}"][f"coluna{j}"]
print("\nMatriz A:")
for i in range(nmrlinha_A):
    print([matriz_A[f"linha{i}"][f"coluna{j}"] for j in range(nmrcoluna_A)])
print("\nMatriz B:")
for i in range(nmrlinha_B):
    print([matriz_B[f"linha{i}"][f"coluna{j}"] for j in range(nmrcoluna_B)])
print("\nMatriz Resultado (C = A * B):")
for i in range(nmrlinha_A):
    print([matriz_C[f"linha{i}"][f"coluna{j}"] for j in range(nmrcoluna_B)])


#✅ Manipulação de uma matriz 4x4:
#Trocar a segunda linha pela terceira.
#Trocar a primeira coluna pela quarta.
#Imprimir antes e depois das trocas.
matriz = {
    1: {1: 1, 2: 2, 3: 3,4: 7},
    2: {1: 4, 2: 5, 3: 6,4: 9},
    3: {1: 7, 2: 8, 3: 9,4: 3},
    4: {1: 9, 2: 2, 3: 8,4: 1}
    }
for i in range(1,5):
    print([matriz[i][j] for j in range(1,5)])
matriz[2], matriz[3] = matriz[3], matriz[2]
for i in matriz:
    matriz[i][1], matriz[i][4] = matriz[i][4], matriz[i][1]
print()
for i in range(1,5):
    print([matriz[i][j] for j in range(1,5)])



#✅ Média aritmética das linhas de uma matriz 4x4:
#Gerar a matriz.
#Calcular a média de cada linha.
#Imprimir a matriz completa e as médias.
medias = []
matriz = {
    1: {1: 1, 2: 2, 3: 3,4: 7},
    2: {1: 4, 2: 5, 3: 6,4: 9},
    3: {1: 7, 2: 8, 3: 9,4: 3},
    4: {1: 9, 2: 2, 3: 8,4: 1}
    }
for i in range(1,5):
    print([matriz[i][j] for j in range(1,5)])
print()
for i in matriz:
    medias.append((sum(matriz[i].values()))/4)
for i in medias:
    print(i)
