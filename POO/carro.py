#Classe Carro:
#Implemente uma classe chamada Carro com as seguintes propriedades:
#• Um veículo tem um certo consumo de combustível (medidos em km/litro) e uma certa quantidade de combustível no tanque.
#• O consumo é especificado no construtor e o nível de combustível inicial é 0.
#• Forneça um método andar() que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina. Esse método recebe como parâmetro a distância em km.
#• Forneça um método obterGasolina(), que retorna o nível atual de combustível.
#• Forneça um método adicionarGasolina(), para abastecer o tanque.
#• Faça um programa para testar a classe Carro. Exemplo de uso:
#meuFusca = Carro(15); # 15 quilômetros por litro de combustível.
#meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
#meuFusca.andar(100); # anda 100 quilômetros.
#meuFusca.obterGasolina() # Imprime o combustível que resta no tanque.
class Carro:
    def __init__(self, gasolina, quilometros_por_litro):
        self.gasolina = gasolina
        self.quilometros_por_litro = quilometros_por_litro  
    def andar(self, distancia):
        gasolina_gasta = distancia / self.quilometros_por_litro
        if gasolina_gasta <= self.gasolina:
            self.gasolina -= gasolina_gasta
        else:
            print("Não há gasolina suficiente para percorrer essa distância!")
            self.gasolina = 0
    def obterGasolina(self):
        return self.gasolina
    def adicionarGasolina(self,adicao):
        self.gasolina += adicao
def main():
    a = 0
    b = int(input("Quantos quilometros por litro seu carro faz? "))
    carro = Carro(a,b)
    resposta = input("deseja viajar de carro? ")
    if resposta.upper().startswith("S"):
        while True:
            print(f"\nQuilometros por Litro: {b}\n")
            acao = int(input("\n(1)obter a gasolina atual\n(2)abastecer o carro\n(3)viajar com o carro\n(4)sair do programa\n\nOque deseja fazer? "))
            if acao == 1:
                print(carro.obterGasolina())
                continue
            if acao == 2:
                abastecer = int(input("Quantos litros de gasolina voce quer botar? "))
                carro.adicionarGasolina(abastecer)
            if acao == 3:
                km = int(input("Qual a distancia que voce vai viajar? "))
                carro.andar(km)    
                continue
            if acao == 4:
                print("Programa finalizado!")
                break
            else:
                print("numero invalido digite novamente!\n")
    else:
       print("Programa finalizado!")
main()
