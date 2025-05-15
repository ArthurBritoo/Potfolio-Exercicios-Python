#1. Classe Triangulo:
#Crie uma classe que modele um triangulo:
#– Atributos: LadoA, LadoB, LadoC
#– Métodos: calcular Perímetro, getMaiorLado;
#• Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um triangulo. Depois, deve criar um objeto com as medidas e imprimir sua área e maior lado.
class Triangulo:
    def __init__(self,LadoA, LadoB, LadoC):
        self.LadoA = LadoA
        self.LadoB = LadoB
        self.LadoC = LadoC
    def calcPerimetro(self):
        return self.LadoA + self.LadoB + self.LadoC
    def getMaiorLado(self):
       return max(self.LadoA , self.LadoB , self.LadoC)
def main():
    listaTriangulo = []
    a = int(input("digite o primeiro lado do Triangulo: "))
    b = int(input("digite o segundo lado do Triangulo: "))
    c = int(input("digite o terceiro lado do Triangulo: "))
    triangulo = Triangulo(a,b,c)
    clcPerimetro = triangulo.calcPerimetro()
    d = triangulo.getMaiorLado()
    print("O maior lado é", d)
    print("O Perimetro do Triangulo é",clcPerimetro)
main()
