def cadastrarAlunos():
    alunos = []
    qtdAlunos = int(input("Quantos alunos voce vai cadastrar? "))
    for i in range(qtdAlunos):
        aluno = input(f"Digite o {i+1}.o Aluno: ")
        alunos.append(aluno)
    return alunos
