# Pode-se calcular o resto da divisão, MOD, de x por y, dois números inteiros positivos, usando-se a definição abaixo. Implemente este algoritmo.
#MOD(x,y) = MOD(x - y, y) se x > y
#MOD(x,y) = x se x < y
#MOD(x,y) = 0 se x = y
def MOD(x,y):
    if x > y:
        return MOD(x-y,y)
    if y > x:
        return x
    return 0
