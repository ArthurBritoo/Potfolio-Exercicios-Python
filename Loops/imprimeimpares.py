#Programa que escreve apenas ímpares positivos até 99
x = 1
while x < 100:
    print(x)
    resposta = input("Deseja continuar? (s/n) ").lower()
    if resposta == 's':
        x += 2
        continue
    elif resposta == 'n':
        print("Você escolheu parar.")
        break
    else:
        print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")
