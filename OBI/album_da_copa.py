#Enunciado:
# Dado o total de figurinhas e uma lista das figurinhas compradas, calcule quantas faltam para completar o álbum.
#Entrada:
 #Número total N, seguido por M figurinhas compradas.
#Saída:
 #Número de figurinhas que faltam.
#Resolução correta:
def figurinhasFaltando(N, compradas):
    return N - len(set(compradas))
