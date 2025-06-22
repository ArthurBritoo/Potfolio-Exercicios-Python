entrada= input().split(" ")
novaentrada = []
for i in entrada:
    i= int(i)
    novaentrada.append(i)
QTDE_CONTAINERS = novaentrada[0]
TAM_CONTAINER = novaentrada[1]
QTDE_INSERCOES = novaentrada[2]
chaves = novaentrada[3:QTDE_INSERCOES+3]
consultas = novaentrada[QTDE_INSERCOES+3:]
TAM_TABELA = QTDE_CONTAINERS * TAM_CONTAINER
tabelahash = [None] * TAM_TABELA

for i in chaves:
    container = i % QTDE_CONTAINERS
    inicio = container * TAM_CONTAINER
    fim = inicio + TAM_CONTAINER
    for j in range(inicio,fim):
        if tabelahash[j] is None:
            tabelahash[j] = i
            break

resultados= []
for i in consultas:
    comparacoes = 0
    container = i % QTDE_CONTAINERS
    inicio = container * TAM_CONTAINER
    fim = inicio + TAM_CONTAINER
    encontrado = False
    for j in range(inicio,fim):
        comparacoes += 1
        if tabelahash[j] == i:
            encontrado = True
            break
        elif tabelahash[j] is None:
            break
    resultados.append(str(comparacoes))
print(" ".join(resultados))
