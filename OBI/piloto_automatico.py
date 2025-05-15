#Questão: Piloto automático
#Enunciado:
# Dados as posições dos carros A, B e C, determine se o carro B deve acelerar, manter ou desacelerar.
#Entrada:
# Três inteiros A, B, C.
#Saída:
 #1 para acelerar, 0 para manter, -1 para desacelerar.
#Resolução correta:
def distanciaCarros(A, B, C):
    if (B - A) < (C - B):
        return 1
    elif (B - A) > (C - B):
        return -1
    else:
        return 0
