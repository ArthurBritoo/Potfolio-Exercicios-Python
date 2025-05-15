#Enunciado:
 #Os administradores da Fazenda Fartura planejam criar uma nova plantação de morangos, no formato retangular. Eles têm vários locais possíveis para a nova plantação, com diferentes dimensões de comprimento e largura. Para os administradores, o melhor local é aquele que tem a maior área.
#Entrada:
 #Quatro números inteiros representando as dimensões dos dois terrenos.
#Saída:
# Área do melhor local.
#Resolução correta:

def checarMaiorArea(la, ca, lb, cb):
    a, b = la * ca, lb * cb
    return max(a, b)
