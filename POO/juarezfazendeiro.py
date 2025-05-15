#1. Juarez é um fazendeiro que possui muitos terrenos espalhados pelo estado de Pernambuco, todos eles com formato retangular. 
#Pensando nisso, ele lhe contratou para fazer um programa capaz de lhe auxiliar no gerenciamento das fazendas. a. 
#Desenvolva, utilizando orientação a objetos, um programa que calcule a área total de uma fazenda e de seu perímetro externo, assim como a soma da área dos terrenos de todas as suas terras. 
class Terreno:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    def calcarea(self):
        return self.ladoA * self.ladoB
    def calcperimetro(self):
        return 2*self.ladoA + 2*self.ladoB
class Fazenda:
    def __init__(self):
        self.terrenos = []
    def adicionar_terreno(self, terreno):
        self.terrenos.append(terreno)
    def calcarea_total(self):
        total_area = sum([terreno.calcarea() for terreno in self.terrenos])
        return total_area
    def calcperimetro_externo(self):
        total_perimetro = sum([terreno.calcperimetro() for terreno in self.terrenos])
        return total_perimetro


def main():
    fazenda = Fazenda()
    nmrTerras = int(input("Quantas terras você tem? "))
    for i in range(nmrTerras):
        x = int(input(f"qual o tamanho do primeiro lado da sua {i+1}.a terra? "))
        y = int(input(f"qual o tamanho do segundo lado da sua {i+1}.a terra? "))
        terra = Terreno(x, y)
        fazenda.adicionar_terreno(terra)
        print(f"A area da sua {i+1}.a terra é {terra.calcarea()}")
        print(f"O perimetro da sua {i+1}.a terra é {terra.calcperimetro()}")
    if nmrTerras > 1:
        print("A soma da area da sua fazenda é ", fazenda.calcarea_total())
        print("O perimetro da sua fazenda é ", fazenda.calcperimetro_externo())
main()
