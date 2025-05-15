#Drone de Entrega
#Nome do arquivo: “drone.py”
#A loja do Pará, especializada em vendas pela internet, está desenvolvendo drones para entrega de caixas com as compras dos clientes. Cada caixa tem a forma de um paralelepípedo reto retângulo (ou seja, no formato de um tijolo). O drone entregará uma caixa de cada vez, e colocará a caixa diretamente dentro da casa do cliente, através de uma janela. Todas as janelas dos clientes têm o formato retangular e estão sempre totalmente abertas. O drone tem um aplicativo de visão computacional que calcula exatamente as dimensões H e L da janela. O drone consegue colocar a caixa através da janela somente quando uma das faces da caixa está paralela à janela, mas consegue virar e rotacionar a caixa antes de passá-la pela janela.
#Neste problema, será dada a dimensão da maior janela do cliente e as dimensões da caixa que deve ser entregue, seu programa deve determinar se o drone vai ser capaz de entregar a compra (pela janela) ou se a compra terá que ser entregue por meios normais.
#Entrada A entrada é composta por cinco linhas, cada uma contendo um número inteiro. As três primeiras linhas contêm os valores A, B, C, indicando as três dimensões da caixa, em centímetros. As duas últimas linhas contêm os valores H e L, indicando a altura e a largura da janela, em centímetros.
#Saída Seu programa deve escrever uma única linha, contendo apenas a letra S se a caixa passa pela janela e apenas a letra N em caso contrário.
#Exemplo de entrada 1 30 50 80 80 60
#Exemplo de saída 1 S
#Exemplo de entrada 2 75 100 50 100 30
#Exemplo de saída 2 N


def drones(caixaA, caixaB, caixaC, janelaA, janelaB):
    if caixaA <= caixaB and caixaA <= caixaC:
        maioresCaixa = caixaB + caixaC
    elif caixaB <= caixaA and caixaC <= caixaC:
        maioresCaixa = caixaA + caixaC
    else:
        maioresCaixa = caixaA + caixaB
    if janelaA + janelaB < maioresCaixa:
        return "S"
    else:
        return "N"
