#1. Implemente em Python um algoritmo recursivo para o c´alculo do fatorial n!, com n sendo um n´umero inteiro. Fatoriais de n´umeros negativos s˜ao nulos. 
#Entrada: Um n´umero inteiro n 
#Sa´ıda: O valor do fatorial n! 
#Exce¸c˜oes: Para n < 0, retorne n! = 0 

def fatorial(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n * fatorial(n-1)
