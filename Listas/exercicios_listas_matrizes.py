
# 1. Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.
lista = []
for i in range(5):
    lista.append(int(input(f"Coloque o {i+1}º número: ")))
for i, num in enumerate(lista):
    print(f"Posição {i}: {num}")

# 2. Ler uma lista de 10 números reais e mostre-os na ordem inversa.
lista = []
for i in range(10):
    lista.append(float(input(f"Coloque o {i+1}º número: ")))
print("Lista original:", lista)
print("Lista invertida:", list(reversed(lista)))

# 3. Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média.
nota = []
for i in range(4):
    nota.append(float(input(f"Coloque o {i+1}º nota: ")))
print("As notas são:", nota)
print("A média é:", sum(nota)/4)

# 4. Ler um vetor com 20 idades e exibir a maior e menor.
idade = []
for i in range(20):
    idade.append(int(input(f"Coloque o {i+1}º idade: ")))
print(f"A maior idade é {max(idade)} e a menor idade é {min(idade)}")

# 5. Inicialize uma lista de 20 números inteiros. Armazene os números pares em uma lista PAR e os ímpares em IMPAR. Imprima as listas.
import random
par = []
impar = []
for i in range(20):
    numero = random.randint(1, 20)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print("Pares:", par)
print("Ímpares:", impar)

# 6. Receba a temperatura média de cada mês e mostre as que ficaram acima da média anual.
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
temperatura = []
mesesmedia = []
for i in meses:
    temp = float(input(f"Digite a temperatura em graus Celsius do mês de {i}: "))
    temperatura.append(temp)
media = sum(temperatura) / 12
for i, temp in enumerate(temperatura):
    if temp > media:
        mesesmedia.append(meses[i])
print(f"A média das temperaturas dos meses é: {media:.2f} graus Celsius")
print(f"Os meses acima da média são: {', '.join(mesesmedia)}")

# 7. Crie uma matriz aleatoriamente. O tamanho da matriz deve ser informado pelo usuário.
import random
matriz = []
lc = int(input("Digite o número de linhas e colunas: "))
for i in range(lc):
    linha = []
    for j in range(lc):
        linha.append(random.randint(1, 999))
    matriz.append(linha)
print("Matriz Gerada:")
for linha in matriz:
    for num in linha:
        print("{:3d}".format(num), end=" ")
    print()

# 8. Crie uma matriz M (valores informados pelo usuário) e mostre a matriz com o dobro dos valores lidos.
matriz = []
lc = int(input("Digite o número de linhas e colunas: "))
for i in range(lc):
    linha = []
    for j in range(lc):
        numero = int(input(f"Digite o número para a posição ({i+1}, {j+1}): "))
        linha.append(numero)
    matriz.append(linha)
print("\nMatriz Original:")
for linha in matriz:
    for num in linha:
        print("{:3d}".format(num), end=" ")
    print()
print("\nMatriz Dobrada:")
for linha in matriz:
    for num in linha:
        print("{:3d}".format(num*2), end=" ")
    print()

# 13. Leia um número indeterminado de notas e realize diversas operações.
notas = []
notasMedia = []
qtdenotas = int(input("Quantas notas você quer digitar? "))
for i in range(qtdenotas):
    notas.append(float(input(f"Digite a {i+1}ª nota: ")))
print(f"Você digitou {qtdenotas} notas")
print(f"As notas: {notas}")
print("As notas na ordem invertida:")
for nota in reversed(notas):
    print(nota)
print(f"Soma das notas: {sum(notas)}")
media = sum(notas) / qtdenotas
print(f"Média das notas: {media:.2f}")
for j in notas:
    if j > media:
        notasMedia.append(j)
print(f"Notas acima da média: {notasMedia}")
