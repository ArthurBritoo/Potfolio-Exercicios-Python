# 6. Perguntar o preço de três produtos e informar qual é o mais barato
num1 = float(input("Digite o preço da primeira loja: "))
num2 = float(input("Digite o preço da segunda loja: "))
num3 = float(input("Digite o preço da terceira loja: "))

if num1 <= num2 and num1 <= num3:
    print("Compre na primeira loja")
elif num2 <= num1 and num2 <= num3:
    print("Compre na segunda loja")
elif num3 <= num1 and num3 <= num2:
    print("Compre na terceira loja")
