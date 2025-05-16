# 4. Determinar se um ano (inteiro com 4 dígitos) é bissexto (divisível por 4)
ano = int(input("Digite um ano: "))
if ano % 4 == 0:
    print("Esse ano é bissexto")
else:
    print("Esse ano não é bissexto")
