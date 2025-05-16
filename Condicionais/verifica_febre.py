# 2. Ler a temperatura de uma pessoa e exibir a mensagem:
# "Febre Alta" (temp ≥ 39), "Febril" (39 > temp ≥ 37) ou "Sem Febre" (temp < 37)
temperatura = float(input("Digite a temperatura da pessoa: "))
if temperatura >= 39:
    print("Febre Alta")
elif temperatura >= 37:
    print("Febril")
else:
    print("Sem Febre")
