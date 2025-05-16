# 1. Programa que lê 2 strings e informa:
# - Conteúdo delas e seu comprimento
# - Se possuem o mesmo comprimento
# - Se são iguais ou diferentes no conteúdo
s = input('Digite uma frase: ')
t = input('Digite outra frase: ')

print(f'Tamanho de "{s}": {len(s)} caracteres')
print(f'Tamanho de "{t}": {len(t)} caracteres')

if len(s) == len(t):
    print("As duas strings são do mesmo tamanho.")
else:
    print("As duas strings são de tamanhos diferentes.")

if s == t:
    print("As duas strings possuem conteúdo igual.")
else:
    print("As duas strings possuem conteúdo diferente.")
