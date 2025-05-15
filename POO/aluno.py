#4. Classe Aluno:
#Implemente uma classe Aluno, que deve ter os seguintes atributos: nome, curso, tempoSemDormir (em horas). Essa classe deverá ter os seguintes métodos:
#– estudar (que recebe como parâmetro a qtd de horas de estudo e acrescenta tempoSemDormir)
#– Dormir (que recebe como parâmetro a qtd de horas de sono e reduz tempoSemDormir)
#• Crie um código de teste da classe, criando um objeto da classe aluno e usando os métodos estudar e dormir. Ao final imprima quanto tempo o aluno está sem dormir.
class Aluno:
    def __init__(self,nome,curso,tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir
    def estudar(self, tempoEstudo):
        self.tempoSemDormir += tempoEstudo
        return self.tempoSemDormir
    def dormir(self, tempoDormindo):
        self.tempoSemDormir -= tempoDormindo
        if self.tempoSemDormir < 0:
            self.tempoSemDormir = 0
def main():
    a = input("Qual o nome do aluno? ")
    b = input("Qual o curso do aluno? ")
    c = 0
    aluno = Aluno(a,b,c)
    estudando = int(input("Quanto tempo em horas seu aluno estuda? "))
    dormindo = int(input("Quanto tempo seu aluno Dormiu? "))
    aluno.estudar(estudando)
    aluno.dormir(dormindo)
    print(f"\no Aluno {a} do curso {b} esta a {aluno.tempoSemDormir} horas sem dormir")
main()
