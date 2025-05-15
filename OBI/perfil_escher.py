#Questão: Perfil Escher
#Enunciado:
# Verificar se uma sequência de alturas forma um perfil Escher (auto-simétrico).
#Entrada:
# Um inteiro N seguido de N inteiros.
#Saída:
# 'S' se for perfil Escher, 'N' se não for.
#Resolução correta:
def escher(n, lista):
    for i in range(n // 2):
        if lista[i] + lista[-(i+1)] != lista[0] + lista[-1]:
            return "N"
    return "S"
