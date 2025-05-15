#2. Implemente em Python um algoritmo recursivo para o c´alculo da exponencial an, com a sendo um n´umero qualquer (positivo, negativo ou zero) e com expoente inteiro n ≥ 0. Observe com aten¸c˜ao o caso 00 que n˜ao pode ser calculado. 
#Entrada: Uma base a que pode ser qualquer n´umero (inclusive negativo) Um expoente inteiro n ≥ 0 
#Sa´ıda: O valor da exponencial an 
#Exce¸c˜oes: Para o caso 00informe que ´e “imposs´ıvel calcular”. 

def potencia(a,n):
    if n == 0 and a == 0:
        return "impossıvel calcular"
    if n == 0:
        return 1
    if n == 1:
        return a
    return a * potencia(a,n-1)
