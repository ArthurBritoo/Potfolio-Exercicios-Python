# 5. Ler três números e mostrá-los em ordem decrescente
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Encontra o maior, médio e menor
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
medio = (num1 + num2 + num3) - maior - menor

print(f"Ordem decrescente: {maior}, {medio}, {menor}")
