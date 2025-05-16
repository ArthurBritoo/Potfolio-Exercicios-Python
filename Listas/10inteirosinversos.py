#Lista de 10 números reais, mostrar na ordem inversa:
lista = []
for i in range(10):
    lista.append(int(input(f"coloque o {1+i}.o numero: ")))
print(lista)
print(list(reversed(lista)))
