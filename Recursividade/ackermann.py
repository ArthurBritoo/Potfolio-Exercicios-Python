# Dada a definição da função de Ackerman:
#válida para valores inteiros não negativos de m e n, implemente uma versão recursiva do algoritmo e faça o diagrama de execução de A(1, 2).
def ackerman(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ackerman(m-1,1)
    elif m>0 and n > 0:
        return ackerman(m-1, ackerman(m, n-1))
print(ackerman(1,2))
