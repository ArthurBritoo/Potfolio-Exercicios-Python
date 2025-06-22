import random

tamanho_cromossomo = 8
tamanho_populacao = 10
taxa_mutacao = 0.1
numero_geracoes = 20
alvo = [1] * tamanho_cromossomo

def criar_individuo():
    return [random.randint(0, 1) for _ in range(tamanho_cromossomo)]

def criar_populacao():
    return [criar_individuo() for _ in range(tamanho_populacao)]

def fitness(individuo):
    return sum(individuo[i] == alvo[i] for i in range(tamanho_cromossomo))

def selecao(populacao):
    return sorted(populacao, key=fitness, reverse=True)

def crossover(pai1, pai2):
    ponto = random.randint(1, tamanho_cromossomo - 1)
    return pai1[:ponto] + pai2[ponto:]

def mutacao(individuo):
    return [
        bit if random.random() > taxa_mutacao else 1 - bit
        for bit in individuo
    ]

def algoritmo_genetico():
    populacao = criar_populacao()

    for geracao in range(numero_geracoes):
        populacao = selecao(populacao)
        melhor = populacao[0]
        print(f"Geração {geracao}: melhor = {melhor}, fitness = {fitness(melhor)}")

        nova_geracao = []

        while len(nova_geracao) < tamanho_populacao:
            pai1, pai2 = random.sample(populacao[:5], 2)
            filho = crossover(pai1, pai2)
            filho = mutacao(filho)
            nova_geracao.append(filho)

        populacao = nova_geracao

    melhor = selecao(populacao)[0]
    print(f"\nMelhor solução encontrada: {melhor}, fitness = {fitness(melhor)}")

algoritmo_genetico()
