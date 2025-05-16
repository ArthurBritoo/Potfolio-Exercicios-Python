#Programa que lê idades e alturas
altura = 1000
idade = 0
contador = 0

while altura != 0:
    altura = float(input("Digite a altura do Aluno (quando quiser parar digite 0): "))
    if altura == 0:
        break
    idade = int(input("Digite a idade do Aluno: "))
    if idade > 13 and altura < 1.5:
        contador += 1

print("Você tem %d alunos com mais de 13 anos e que possuem altura inferior à 1.5" % (contador))
