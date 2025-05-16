# 7. Solicitar nome e matrícula do aluno e exibir no formato especificado
nome = input("Digite o nome do aluno: ")
matricula = input("Digite o número de matrícula: ")

# Verifica se a matrícula é numérica antes de converter
if matricula.isdigit():
    matricula = int(matricula)
    print(f'Nome do Aluno: "{nome}", Matrícula: "{matricula}"')
else:
    print("Matrícula inválida! Digite apenas números.")
