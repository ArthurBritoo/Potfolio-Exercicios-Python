# 2. Programa que permite ao usuário digitar seu nome e mostra
# o nome de trás para frente em letras maiúsculas
nome = input('Digite seu nome: ')
nome_reverso = nome[::-1].upper()
print(f"Nome ao contrário em maiúsculas: {nome_reverso}")
