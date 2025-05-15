# Classe Produto
#Construa uma classe Produto, que deve ter os atributos codigo e preco (privados).
#Adicione também um atributo estático qtdProd, que deverá ser incrementado toda vez que um novo objeto for criado.
#Crie os métodos getters e setters e teste a classe.
class Produto:
    qtdProd = 0  


    def __init__(self, codigo, preco):
        self.__codigo = codigo  
        self.__preco = preco  
        Produto.qtdProd += 1
    def getPreco(self):
        return self.__preco
    def getCodigo(self):
        return self.__codigo
    def setPreco(self,novoPreco):
        self.__preco = novoPreco
    def setCodigo(self,novoCodigo):
        self.__codigo = novoCodigo


p1 = Produto(101, 29.90)
p2 = Produto(102, 45.50)
p3 = Produto(103, 99.99)


# Exibindo a quantidade total de produtos criados (atributo estático)
print("Quantidade de produtos criados:", Produto.qtdProd)
