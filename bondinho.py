#Bondinho
#Nome do arquivo: “bondinho.py”
#O sistema de transporte de bondinhos de uma cidade utiliza um mecanismo simples de movimentação. Cada bondinho possui um número de lugares e, ao longo do dia, ele deve fazer diversas viagens entre dois pontos. O objetivo do problema é determinar o número de pessoas que ficam em cada ponto da cidade, para que o sistema possa otimizar suas viagens.
#Entrada A entrada consiste de vários casos de teste. Cada caso de teste inicia com dois números inteiros N (o número de pessoas em cada bondinho) e M (o número de viagens). Em seguida, há M linhas com dois números inteiros, A e B, indicando que um número A de pessoas entrou no bondinho na viagem A, e um número B de pessoas saiu na viagem B. O número de pessoas no bondinho após a viagem B deve ser calculado.
#Saída Para cada caso de teste, seu programa deve imprimir um número inteiro, indicando o número de pessoas no bondinho após a última viagem.


n, m = map(int, input().split())
pessoas = n
for _ in range(m):
    a, b = map(int, input().split())
    pessoas += a - b
print(pessoas)
