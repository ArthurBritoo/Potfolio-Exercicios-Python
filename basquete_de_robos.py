#Questão: Basquete de robôs
#Enunciado:
# Dado a distância do robô até o início da quadra, calcule a pontuação do lançamento.
#Entrada:
# Um número inteiro D (0 ≤ D ≤ 2000).
#Saída:
# 1, 2 ou 3 pontos.
#Resolução correta:
def checarLançamento(D):
    if D <= 800:
        return 1
    elif D <= 1400:
        return 2
    else:
        return 3
