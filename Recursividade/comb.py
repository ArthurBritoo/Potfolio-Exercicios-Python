#1) Considere a função Comb(n, k), que representa o número de grupos distintos com k pessoas que podem ser formados a partir de n pessoas. Por exemplo, Comb(4, 3) = 4, pois com 4 pessoas (A, B, C, D), é possível formar 4 diferentes grupos: ABC, ABD, ACD e BCD. Sabe-se que:
#Implemente uma função recursiva para Comb (n, k) e mostre o diagrama de execução para chamada Comb (5, 3). Sabendo-se ainda Comb (n, k) = n! / (k! (n-k)!), implemente uma função não recursiva de Comb (n, k).
def comb(n,k):
    if k == 1:
        return n
    elif k==n:
        return 1
    else:
        return comb(n-1,k-1) + comb(n-1,k)
print (comb(4,3))
