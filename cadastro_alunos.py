cadastros = []
for _ in range(10):
    aluno = {
        "matricula": input("Matrícula: "),
        "nome": input("Nome: "),
        "endereco": {
            "rua": input("Rua: "),
            "numero": input("Número: "),
            "bairro": input("Bairro: "),
            "cidade": input("Cidade: "),
            "cep": input("CEP: ")
        }
    }
    cadastros.append(aluno)

for aluno in cadastros:
    print("-" * 20)
    print(f"Matrícula: {aluno['matricula']}")
    print(f"Nome: {aluno['nome']}")
    print("Endereço:")
    for chave, valor in aluno["endereco"].items():
        print(f"  {chave.capitalize()}: {valor}")

matricula = input("Digite a matrícula do aluno a ser alterado: ")
for aluno in cadastros:
    if aluno["matricula"] == matricula:
        aluno["nome"] = input("Novo nome: ")
        aluno["endereco"]["rua"] = input("Nova rua: ")
        aluno["endereco"]["numero"] = input("Novo número: ")
        aluno["endereco"]["bairro"] = input("Novo bairro: ")
        aluno["endereco"]["cidade"] = input("Nova cidade: ")
        aluno["endereco"]["cep"] = input("Novo CEP: ")
        print("Cadastro alterado com sucesso.")
        break
else:
    print("Matrícula não encontrada.")