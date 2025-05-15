#Domino
#Nome do arquivo: “domino.py”
#O jogo de dominó tradicional é composto por 28 peças, com valores de 0 a 6 em cada lado. Quando as peças são dispostas na mesa de forma contínua, o número de combinações possíveis de peças pode ser calculado usando a fórmula:
#(n+1)*(n+2)/2
#Este problema pede para você escrever um programa que calcule o número de peças de um jogo de dominó, dado o número máximo de pontos que uma peça pode ter.
#Entrada A entrada consiste de um número inteiro N, que representa o maior número de pontos de uma peça de dominó. O valor de N é sempre um número entre 0 e 12.
#Saída Seu programa deve imprimir um único número inteiro, representando o número de peças no jogo de dominó.
#Exemplo de entrada 1 6
#Exemplo de saída 1 28
#Exemplo de entrada 2 12
#Exemplo de saída 2 91

def domino(n):
    return ((n + 1) * (n + 2)) // 2
