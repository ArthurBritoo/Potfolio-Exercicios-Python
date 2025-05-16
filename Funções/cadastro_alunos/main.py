from interface import cadastrarAlunos
from bd import salvarAlunosEmArquivo

alunos = cadastrarAlunos()
nome_arquivo = "alunos.txt"
salvarAlunosEmArquivo(alunos, nome_arquivo)
print(f"Alunos cadastrados e salvos no arquivo {nome_arquivo}.")
