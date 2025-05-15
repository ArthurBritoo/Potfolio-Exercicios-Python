#✅ Criar um dicionário representando uma agenda com CPF como chave e valores contendo nome, idade e telefone.
#✅ Permitir que o usuário insira múltiplos contatos e, ao final, imprimir todos os itens no formato:
#CPF: Nome - Idade - Telefone

listaPessoas = []
resp = int(input("Quantas pessoas você deseja cadastrar? "))


for i in range(resp):
    c = int(input(f'Qual o CPF da {i+1}ª pessoa: '))
    n = input(f'Qual o nome da {i+1}ª pessoa: ')
    idade = int(input(f'Qual a idade da {i+1}ª pessoa: '))
    t = input(f'Qual o telefone da {i+1}ª pessoa: ')


    dados = {'cpf': c, 'nome': n, 'idade': idade, 'telefone': t}
    listaPessoas.append(dados)


print("\nLista de Pessoas Cadastradas:\n")
for pessoa in listaPessoas:
    print(f"{pessoa['cpf']}: {pessoa['nome']} - {pessoa['idade']} - {pessoa['telefone']}\n")


#✅ Criar um programa que cadastre várias pessoas (nome, idade e CPF) em um dicionário.
#✅ Remover todas as pessoas menores de 18 anos e colocá-las em um novo dicionário.
listaPessoas = {}
dados_menores_18 = {}


for _ in range(int(input("Quantas pessoas deseja cadastrar? "))):
    cpf = input("CPF: ")
    nome = input("Nome: ")
    idade = int(input("Idade: "))


    if idade < 18:
        dados_menores_18[cpf] = {"nome": nome, "idade": idade}
    else:
        listaPessoas[cpf] = {"nome": nome, "idade": idade}


print("\nMaiores de 18 anos:")
for cpf, dados in listaPessoas.items():
    print(f"{cpf}: {dados['nome']} - {dados['idade']} anos")


print("\nMenores de 18 anos:")
for cpf, dados in dados_menores_18.items():
    print(f"{cpf}: {dados['nome']} - {dados['idade']} anos")


     

#✅ Criar um sistema com um dicionário principal e um de backup.
#✅ Quando o dicionário principal atingir 5 itens, ele imprime os dados, transfere para o backup e apaga os dados do principal.
dados = {}
backup = {}
contador = 0
while True:
    chave = contador + 1
    valor = input(f"Adicione um valor para a chave {chave}: ")
    dados[chave] = valor
    contador += 1


    if contador == 5:
        print("\nDicionário principal atingiu 5 itens. Transferindo para backup...\n")
        print(dados.items())
        backup.update(dados)
        dados.clear()
        contador = 0


    continuar = input("\nDeseja continuar adicionando dados? (S/N): ").strip().upper()
    if continuar != "S":
        break
print("\nBackup Final:", backup)
