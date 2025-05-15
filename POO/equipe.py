#Classe Aluno e Equipe:
#Crie uma classe Aluno, que possui como atributo um nome e cpf. Crie outra classe chamada Equipe, que possui como atributo uma lista de participantes do tipo Aluno e outro atributo chamado projeto.
#• Crie uma terceira classe chamada GerenciadorEquipes. Essa classe possui como atributo uma lista de todas as equipes formadas. Ela deverá possuir o método criarEquipe, que recebe uma lista de alunos de uma equipe e diz se a equipe pode ser formada ou não. Caso não haja nenhum aluno da equipe a ser formada em uma outra equipe com o mesmo projeto, então a equipe é criada e acrescentada à lista. Caso contrário, é informada que a equipe não pode ser criada.
class Aluno:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf


class Equipe:
    def __init__(self,projeto):
        self.projeto = projeto
        self.participantes = []
    def adicionar_participante(self, aluno):
        self.participantes.append(aluno)
    def __str__(self):
        participantes_str = '\n'.join([str(aluno) for aluno in self.participantes])
        return f"Projeto: {self.projeto}\nParticipantes:\n{participantes_str}"
class Gerenciador:
    def __init__(self):
        self.equipes = []
    def criarEquipe(self, alunos, projeto):
        for equipe in self.equipes:
            if equipe.projeto == projeto:
                for aluno in alunos:
                    for participante in equipe.participantes:
                        if participante.cpf == aluno.cpf:
                            print(f"A equipe não pode ser criada. O aluno {aluno.nome} já está em uma equipe com o projeto {projeto}.")
                            return
        nova_equipe = Equipe(projeto)
        for aluno in alunos:
            nova_equipe.adicionar_participante(aluno)
       
        self.equipes.append(nova_equipe)
        print(f"Equipe do projeto '{projeto}' criada com sucesso!")
        print(nova_equipe)
