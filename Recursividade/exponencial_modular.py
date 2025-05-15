#3. Implemente em Python um algoritmo recursivo para o c´alculo da exponencial modular an mod m, com a sendo um n´umero inteiro qualquer (positivo, negativo ou zero), com expoente inteiro n ≥ 0 e com m´odulo inteiro m ≥ 2. Observe com aten¸c˜ao o caso 00 mod m que n˜ao pode ser calculado. 
#Entrada: Uma base a que pode ser qualquer n´umero inteiro (inclusive negativo) Um expoente inteiro n ≥ 0 
#Um “m´odulo” inteiro m ≥ 2 
#Sa´ıda: O valor da exponencial modular an mod m 
#Exce¸c˜oes: Para o caso 00 mod m, informe que ´e “impossível calcular”. Para o caso m ≤ 1, informe que ´e “imposs´ıvel calcular”. 
#Sugest˜ao: Pesquise na internet o tema “exponencial modular recursiva” ou, se preferir, “recursive modular exponentiation”. 
def expomod(a,n,m):
    if a == 0 and n == 0:
        return "impossível calcular"
    if m <= 1:
        return "impossível calcular"
    if n == 0:
        return 1
    if n % 2 != 0:
        return (a * expomod(a,n-1,m))% m
    else:
        metade = expomod(a, n // 2, m)
        return( metade * metade) % m
