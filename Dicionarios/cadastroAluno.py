#Faça um programa que cadastre os alunos da UFRPE. O programa deve receber o nome da pessoa, o curso e o endereço onde ela mora. Insira o endereço de forma que o endereço seja um dicionário dentro do dicionário de alunos. No endereço deve conter a rua, o número e o bairro. O programa deve permitir que o usuário atualize qualquer dado de um aluno.


listaAlunos = []


print("Cadastro de alunos - Você pode cadastrar ou alterar dados de alunos.")


resp = input("Deseja cadastrar os alunos? (S/N) ").strip().upper()
while resp.startswith("S"):
    n = input("Qual o nome do aluno? ").strip()
    c = input("Qual o curso do aluno? ").strip()
    r = input("Qual a rua do endereço? ").strip()
    num = input("Qual o número da casa? ").strip()
    b = input("Qual o bairro? ").strip()


    aluno = {
        'nome': n,
        'curso': c,
        'endereço': {
            'rua': r,
            'número': num,
            'bairro': b
        }
    }


    listaAlunos.append(aluno)
    print("Aluno cadastrado com sucesso!\n")


    resp = input("Deseja continuar cadastrando? (S/N) ").strip().upper()


if listaAlunos:
    busca = input("\nDigite o NOME do aluno que deseja alterar: ").strip()
   
    for aluno in listaAlunos:
        if aluno['nome'].lower() == busca.lower():
            print(f"\nAluno encontrado: {aluno}")
           
            alteracao = input("Qual dado deseja alterar? (nome, curso, endereço) ").strip().lower()
           
            if alteracao == 'endereço':
                novoEndereco = input("Qual campo do endereço deseja alterar? (rua, número, bairro) ").strip().lower()
               
                if novoEndereco in aluno['endereço']:
                    aluno['endereço'][novoEndereco] = input(f"Digite o novo valor para {novoEndereco}: ").strip()
                    print("\nEndereço atualizado com sucesso!")
                else:
                    print("Campo de endereço inválido.")
           
            elif alteracao in ['nome', 'curso']:
                aluno[alteracao] = input(f"Digite o novo valor para {alteracao}: ").strip()
                print(f"\n{alteracao.capitalize()} atualizado com sucesso!")


            else:
                print("Opção inválida.")


            break  


    else:
        print("Aluno não encontrado.")  


else:
    print("\nNenhum aluno cadastrado para alterar.")


