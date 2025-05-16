# Ler número indeterminado de notas, várias análises:
notas = []
notasMedia = []

qtdenotas = int(input("quantas Notas você quer digitar? "))
for i in range(qtdenotas):
    notas.append(float(input(f"Digite a {i+1}.a Nota: ")))

print(f"Você digitou {qtdenotas} Notas")
print(f"As Notas: {notas}")
print("As Notas na ordem invertida: ")
for nota in reversed(notas):
    print(nota)

print(f"Soma das Notas: {sum(notas)}")
media = (sum(notas)) / qtdenotas
print(f"Média das Notas: {media:.2f}")

for j in notas:
    if j > media:
        notasMedia.append(j)

print(f"Notas acima da Média: {notasMedia}")
