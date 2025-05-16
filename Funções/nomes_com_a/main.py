from arquivo import ler_nomes_do_arquivo
from lista import filtrar_nomes_com_a
from impressao import imprimir_maior_nome

nomes = ler_nomes_do_arquivo('nomes.txt')
nomes_com_a = filtrar_nomes_com_a(nomes)
imprimir_maior_nome(nomes_com_a)
