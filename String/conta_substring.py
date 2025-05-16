# 5. Programa que lê uma string e conta quantas vezes o substring "ado" aparece
frase = input("Escreva uma frase: ").lower()
contador = 0
posicao = frase.find("ado")

while posicao != -1:
    contador += 1
    posicao = frase.find("ado", posicao + 1)

print(f"'ado' apareceu {contador} vezes na frase.")
