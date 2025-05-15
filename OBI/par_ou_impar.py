#Questão: Jogo de par ou ímpar
#Enunciado:
# Dado quem gritou "par" (0 para Alice, 1 para Bob) e o número de dedos estendidos por cada um, determine quem ganhou.
#Entrada:
# Três números inteiros P, D1 e D2.
#Saída:
# 0 se Alice ganhou, 1 se Bob ganhou.
#Resolução correta:
def checarParImpar(p, d1, d2):
    soma = d1 + d2
    if soma % 2 == 0:
        return p
    else:
        return 1 - p
