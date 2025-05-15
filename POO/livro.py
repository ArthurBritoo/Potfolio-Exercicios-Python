#3. Classe Livro:
#Crie uma classe Livro que possui os atributos nome, qtdPaginas, autor e preço.
#– Crie os métodos getPreco para obter o valor do preço e o método setPreco para setar um novo valor do preço.
#• Crie um código de teste.
class Livro:
    def __init__(self,autor,qtdPagina,preco):
        self.autor = autor
        self.qtdPagina = qtdPagina
        self.preco = preco
    def getPreco(self):
        return self.preco
    def setPreco(self, z):
        self.preco = z
def main():
    a = input("Qual o nome do autor do livro? ")
    b = int(input("Qual a quantidades de paginas? "))
    c = int(input("Qual o preço do livro? "))
    livro = Livro(a,b,c)
    x = livro.getPreco()
    print(f"\nAutor: {a} \nQuantidades de paginas: {b} \nPreço: {x}\n")
    pergunta = input("Quer mudar o preço do livro? ")
    if pergunta.upper().startswith("S"):    
        d = int(input("Qual o novo preço do livro? "))    
        livro.setPreco(d)
        novoPreco = livro.getPreco()
        print(f"\nAutor: {a} \nQuantidades de paginas: {b} \nnovo Preço: {novoPreco}\n")
    else:
        print(f"\nAutor: {a} \nQuantidades de paginas: {b} \nPreço: {x}\n")
main()
