Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande número de organizações: 
# “Qual o melhor Sistema Operacional para uso em servidores?” As possíveis respostas são:
# - 1- Windows XP
# - 2- Unix
# - 3- Linux
# - 4- Netware
# - 5- Mac OS
# - 6- Outro

#  Você deve desenvolver um programa em Python que leia as respostas da enquete e informe ao final o resultado da mesma. 
# O programa deverá ler os valores até ser informado o valor 0 (zero), que encerra a entrada dos dados. 
# Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). 
# Os valores referentes a cada uma das opções devem ser armazenados em uma lista. 
# Após os dados terem sido completamente informados, o programa deverá calcular o percentual de cada uma das respostas e informar o vencedor da enquete.

print("\n\nEnquete: Qual o melhor Sistema Operacional para uso em servidores?")
print("1- Windows XP\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\n0- Encerrar votação\n")

votos = [0, 0, 0, 0, 0, 0]

while True:
    try:
        resposta = int(input("Digite sua opção (0-6): "))
        if resposta == 0:
            break
        if 1 <= resposta <= 6:
            votos[resposta - 1] += 1
        else:
            print("Opção inválida. Digite um valor entre 0 e 6.")
    except ValueError:
        print("Entrada inválida. Digite apenas números.")

total_votos = sum(votos)

if total_votos > 0:
    print("\nSistemas Operacionais - Votos %")
    print("-----------------------------")
    nomes_sistemas = ["Windows XP", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
    for i in range(6):
        percentual = (votos[i] / total_votos) * 100
        print(f"{nomes_sistemas[i]:<12} {votos[i]:<6} {percentual:>5.1f}%")
    
    print(f"\nTotal de {total_votos} votos")
    
    vencedor_index = votos.index(max(votos))
    vencedor = nomes_sistemas[vencedor_index]
    votos_vencedor = votos[vencedor_index]
    percentual_vencedor = (votos_vencedor / total_votos) * 100
    
    print(f"\nO Sistema Operacional mais votado foi o {vencedor}, com {votos_vencedor} votos, correspondendo a {percentual_vencedor:.1f}% dos votos.")
else:
    print("\nNenhum voto foi registrado.")
