def salvarAlunosEmArquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'a') as arquivo:
        for aluno in lista:
            arquivo.write(aluno + '\n')
