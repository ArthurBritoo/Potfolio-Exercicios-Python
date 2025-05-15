#Idade de Camila
#Nome do arquivo: “idade.py”
#Cibele, Camila e Celeste são três irmãs inseparáveis. Estão sempre juntas e adoram fazer esportes, ler, cozinhar, jogar no computador... Agora estão aprendendo a programar computadores para desenvolverem seus próprios jogos. Mas nada disso interessa para esta tarefa: estamos interessados apenas nas suas idades. Sabemos que Cibele nasceu antes de Camila e Celeste nasceu depois de Camila. Dados três números inteiros indicando as idades das irmãs, escreva um programa para determinar a idade de Camila.
#Entrada A entrada é composta por três linhas, cada linha contendo um número inteiro N, a idade de uma das irmãs.
#Saída Seu programa deve produzir uma única linha, contendo um único número inteiro, a idade de Camila.
#Exemplo de entrada 1 6 9 7
#Exemplo de saída 1 7
#Exemplo de entrada 2 34 36 38
#Exemplo de saída 2 36
#Exemplo de entrada 3 22 25 22
#Exemplo de saída 3 22
#Exemplo de entrada 4 91 91 91
#Exemplo de saída 4 91


def idadecamila(a,b,c):
    if a < b > c:
        return b
    elif a < c > b:
        return c
    else:
        return a
