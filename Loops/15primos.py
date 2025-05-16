#Programa que identifica os 15 primeiros números primos
contador = 0
numero = 2

while contador < 15:
    e_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            e_primo = False
            break
    if e_primo:
        print(numero)
        contador += 1
    numero += 1
