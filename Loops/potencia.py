 #Programa que calcula a potência sem usar operador de potência
base = int(input("Digite a base: "))
expoente = int(input("Digite a expoente: "))
resultado = 1

for i in range(expoente):
    resultado *= base

print("Sua base %d na potência %d da %d" % (base, expoente, resultado))
