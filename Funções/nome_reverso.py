def reversoNome(nome):
    return ((nome)[::-1]).upper()

if __name__ == "__main__":
    nome = input("Digite um nome que deseje retornar ao contrario: ")
    nomeReverso = reversoNome(nome)
    print(f"O nome ao contrario ficou: {nomeReverso}")
