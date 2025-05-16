#Lista com 4 notas e média:
nota = []
for i in range(4):
    nota.append(int(input(f"coloque o {1+i}.a nota: ")))
print("as notas são: ", nota)
print("e a media é: ", (sum(nota)/4))
