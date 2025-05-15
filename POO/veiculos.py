#### Q.5 (2.00) - Em Python:
#Crie uma classe **Veiculo** com os atributos `chassi`, `modelo` e `placa`. Crie uma classe **Concessionaria** com os atributos `nome`, `telefone`, `endereco` e uma lista de veículos. Crie também a classe **Fabricante**, que armazena uma lista de concessionárias. Para testar, crie 4 veículos, adicione-os em 2 concessionárias, e crie um objeto da classe **Fabricante**.
class Veiculo():
    def __init__(self, chassi, modelo, placa):
        self.chassi = chassi
        self.modelo = modelo
        self.placa = placa
    def __str__(self):
        return f"Chassi: {self.chassi}, Modelo: {self.modelo}, Placa: {self.placa}"


class Concessionaria():
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.listaVeiculos = []
    def adicionarVeiculos(self, chassi, modelo, placa):
        veiculo = Veiculo(chassi, modelo, placa)
        self.listaVeiculos.append(veiculo)
    def listarVeiculos(self):
        if not self.listaVeiculos:
            print("Nenhum veículo cadastrado ainda.")
        else:
            for idx, veiculo in enumerate(self.listaVeiculos, start=1):
                print(f"{idx}. {veiculo}")
    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Endereço: {self.endereco}"


class Fabricante():
    def __init__(self, nome):
        self.nome = nome
        self.listaConcessionaria = []
    def adicionarConcessionaria(self, nome, telefone, endereco):
        concessionaria = Concessionaria(nome, telefone, endereco)
        self.listaConcessionaria.append(concessionaria)
    def listarConcessionarias(self):
        if not self.listaConcessionaria:
            print("Nenhuma concessionária cadastrada ainda.")
        else:
            for idx, concessionaria in enumerate(self.listaConcessionaria, start=1):
                print(f"{idx}. {concessionaria}")


def main():
    fabricantes = []
    while True:
        print("\n(1) Fabricantes \n(2) Concessionárias \n(3) Veículos \n(4) Sair")
        resposta1 = input("O que desejas acessar? (1-4): ")


        if resposta1 == "1":
            print("\n(1) Adicionar Fabricante\n(2) Listar Fabricantes\n(3) Voltar")
            respostaFabricante = input("Escolha uma opção (1-3): ")


            if respostaFabricante == "1":
                f_nome = input("Nome do Fabricante: ")
                fabricante = Fabricante(f_nome)
                fabricantes.append(fabricante)
                print(f"Fabricante '{f_nome}' adicionado com sucesso.")


            elif respostaFabricante == "2":
                if not fabricantes:
                    print("Nenhum fabricante cadastrado ainda.")
                else:
                    for idx, fab in enumerate(fabricantes, start=1):
                        print(f"{idx}. {fab.nome}")


            elif respostaFabricante == "3":
                continue


        elif resposta1 == "2":
            if not fabricantes:
                print("Nenhum fabricante disponível. Adicione um fabricante primeiro.")
                continue


            print("\nFabricantes Disponíveis:")
            for idx, fab in enumerate(fabricantes, start=1):
                print(f"{idx}. {fab.nome}")


            try:
                escolha_fab = int(input("Escolha o número do fabricante: ")) - 1
                fabricante = fabricantes[escolha_fab]
            except (ValueError, IndexError):
                print("Escolha inválida.")
                continue


            print("\n(1) Adicionar Concessionária\n(2) Listar Concessionárias\n(3) Voltar")
            respostaConcessionaria = input("Escolha uma opção (1-3): ")


            if respostaConcessionaria == "1":
                c_nome = input("Nome da Concessionária: ")
                c_telefone = input("Telefone: ")
                c_endereco = input("Endereço: ")
                fabricante.adicionarConcessionaria(c_nome, c_telefone, c_endereco)
                print(f"Concessionária '{c_nome}' adicionada com sucesso.")


            elif respostaConcessionaria == "2":
                fabricante.listarConcessionarias()


            elif respostaConcessionaria == "3":
                continue


        elif resposta1 == "3":
            if not fabricantes:
                print("Nenhum fabricante disponível. Adicione um fabricante primeiro.")
                continue


            print("\nFabricantes Disponíveis:")
            for idx, fab in enumerate(fabricantes, start=1):
                print(f"{idx}. {fab.nome}")


            try:
                escolha_fab = int(input("Escolha o número do fabricante: ")) - 1
                fabricante = fabricantes[escolha_fab]
            except (ValueError, IndexError):
                print("Escolha inválida.")
                continue


            if not fabricante.listaConcessionaria:
                print("Nenhuma concessionária disponível nesse fabricante.")
                continue


            print("\nConcessionárias Disponíveis:")
            for idx, conc in enumerate(fabricante.listaConcessionaria, start=1):
                print(f"{idx}. {conc}")


            try:
                escolha_conc = int(input("Escolha o número da concessionária: ")) - 1
                concessionaria = fabricante.listaConcessionaria[escolha_conc]
            except (ValueError, IndexError):
                print("Escolha inválida.")
                continue


            print("\n(1) Adicionar Veículo\n(2) Listar Veículos\n(3) Voltar")
            respostaVeiculo = input("Escolha uma opção (1-3): ")


            if respostaVeiculo == "1":
                v_chassi = input("Chassi do Veículo: ")
                v_modelo = input("Modelo do Veículo: ")
                v_placa = input("Placa do Veículo: ")
                concessionaria.adicionarVeiculos(v_chassi, v_modelo, v_placa)
                print("Veículo adicionado com sucesso!")


            elif respostaVeiculo == "2":
                concessionaria.listarVeiculos()


            elif respostaVeiculo == "3":
                continue


        elif resposta1 == "4":
            print("Saindo do programa...")
            break


        else:
            print("Opção inválida. Tente novamente.")


main()


