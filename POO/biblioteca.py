# Sistema de Biblioteca
#Crie as classes Biblioteca e Livro.
#A Biblioteca deverá conter:
#Uma lista de livros disponíveis.
#Uma lista de livros alugados.
#A Biblioteca deverá possuir os seguintes métodos:
#Alugar um livro: Caso o livro já esteja alugado, a pessoa não poderá alugar.
#Devolver um livro.
#Informar qual livro foi mais alugado






class Biblioteca:
    def __init__(self):
        self.listaAlugados = []
        self.listaDisponivel = []


    def AlugarLivro(self, livro):
        if livro not in self.listaDisponivel:
            return "Livro indisponível"
        else:
            self.listaDisponivel.remove(livro)
            self.listaAlugados.append(livro)
            return f"Livro '{livro}' alugado com sucesso"


    def DevolverLivro(self, livro):
        if livro not in self.listaAlugados:
            return "Livro não foi alugado"
        else:
            self.listaAlugados.remove(livro)
            self.listaDisponivel.append(livro)
            return f"Livro '{livro}' devolvido com sucesso"

