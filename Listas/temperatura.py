#Temperatura de cada mês, média e meses acima da média:
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
temperatura = []
mesesmedia = []

for i in meses:
    temp = float(input(f"Digite a temperatura em graus celsius do mês de {i}: "))
    temperatura.append(temp)

media = sum(temperatura) / 12

for i, temp in enumerate(temperatura):
    if temp > media:
        mesesmedia.append(meses[i])

print(f"A média das temperaturas dos meses é: {media:.2f} graus celsius")
print(f"Os meses acima da média são: {' '.join(mesesmedia)}")
