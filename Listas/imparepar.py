#20 números aleatórios: separar pares e ímpares:
import random
par = []
impar = []
for i in range(20):
    numero = random.randint(1, 20)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print("pares: ", par)
print("impares: ", impar)
