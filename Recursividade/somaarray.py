#Usando recursividade, calcule a soma de todos os valores de um array de reais.

def somaarray(listanumero):
    if len(listanumero) == 0:
        return 0
    return listanumero[0] + somaarray(listanumero[1:])
