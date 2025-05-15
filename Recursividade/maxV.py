#2) Implemente recursivamente uma função Max que retorne o maior valor armazenado em um vetor V contendo n números inteiros. 

def Max(V, n):
    if n == 1:
        return V[0]
    else:
        max_restante = Max(V, n - 1)
        return max(V[n - 1], max_restante)
