#  Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# - "Telefonou para a vítima?"
# - "Esteve no local do crime?"
# - "Mora perto da vítima?"
# - "Tinha dívidas com a vítima?"
# - "Já trabalhou com a vítima?"

respostas = []

respostas.append(input("Telefonou para a vítima? (Sim/Não): ").lower())
respostas.append(input("Esteve no local do crime? (Sim/Não): ").lower())
respostas.append(input("Mora perto da vítima? (Sim/Não): ").lower())
respostas.append(input("Tinha dívidas com a vítima? (Sim/Não): ").lower())
respostas.append(input("Já trabalhou com a vítima? (Sim/Não): ").lower())

#  O programa deve, ao final, emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões, ela deve ser classificada como "Suspeita"; 
# entre 3 e 4 como "Cúmplice" e, 5 como "Assassino".

positivas = respostas.count('sim')

if positivas == 2:
    print("\nClassificação: Suspeita")
elif 3 <= positivas <= 4:
    print("\nClassificação: Cúmplice")
elif positivas == 5:
    print("\nClassificação: Assassino")
else:
    print("\nClassificação: Inocente")
