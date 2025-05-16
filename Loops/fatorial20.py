#Programa que imprime o fatorial de um número até 20
while True:
    numero = int(input("Coloque um número até 20: "))
    if numero > 20:
        print("Número maior que vinte. Digite novamente.")
        continue
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print("O fatorial de %d é %d" % (numero , fatorial))
    break
