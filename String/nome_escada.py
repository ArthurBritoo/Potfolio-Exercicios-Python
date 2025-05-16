# 4. Programa que solicita o nome do usuário e imprime-o em formato de escada
nome = input('Digite seu nome: ')
print("\nNome em escada:")
for i in range(1, len(nome) + 1):
    print(nome[:i])
