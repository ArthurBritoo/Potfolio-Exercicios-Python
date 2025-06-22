import random

roleta = []
for i in range(100):
    roleta.append(random.randint(1,10))
roleta.sort()
chance= []

for j in range(1,11):
    qtd = roleta.count(j)
    chance.append(qtd)

print("escolha um numero de 1 a 10 sabendo que:")
for i in range(0,10):
    print(f"{i+1} tem {chance[i]}% de chance de aparecer")
entrada = int(input("Qual o numero escolhido? "))

indice_sorteado = random.randint(0,99)

if entrada == roleta[indice_sorteado]:
    print("acertou!!!")
else:
    print(f"errou!!! o numero era {roleta[indice_sorteado]}")
