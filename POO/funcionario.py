#2. Classe Funcionário:
#Implemente a classe Funcionário. Um funcionário tem um nome e um salário. Escreva um construtor com dois parâmetros (nome e salário) e o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
#Exemplo de uso:
#harry=funcionário("Harry",25000)
#harry.aumentarSalario(10)
#Faça um programa que teste o método da classe.
class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
        self.aumento = aumento
    def aumentarSalario(self,aumento):
        self.salario = self.salario + (self.salario * (aumento/100))
       
def main():
    a = input("Qual o nome do funcionario? ")
    b = int(input("Qual o salario do seu funcionario? "))
    c = int(input("Quantos porcentos voce quer aumentar o salario do funcionario? "))
    funcionario = Funcionario(a,b)
    x = funcionario.aumentarSalario(c)
    print(f"\nfuncionario: {a} \nantigo salario: {b}\n")
    print(f"funcionario: {a} \nnovo salario: {x:.0f}")
main()
