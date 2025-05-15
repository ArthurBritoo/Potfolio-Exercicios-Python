# Trabalhando com Listas de Objetos
#Coloque cada objeto Ponto em uma lista.
#Imprima cada elemento da lista.

class Ponto:
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y


    def __str__(self):
        return f"{self.nome}: ({self.x}, {self.y})"


lista_pontos = []


with open("pontos.txt", "r") as arquivo:  
    linhas = arquivo.readlines()


i = 0
while i < len(linhas):
    nome = linhas[i].strip()  
    if i + 1 < len(linhas):
        x, y = map(int, linhas[i + 1].strip().split())  
        lista_pontos.append(Ponto(nome, x, y))  
    i += 2  


for ponto in lista_pontos:
    print(ponto)
