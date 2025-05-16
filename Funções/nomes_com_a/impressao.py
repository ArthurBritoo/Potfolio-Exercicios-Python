def imprimir_maior_nome(nomes):
    if not nomes:
        print("Nenhum nome começando com 'a' encontrado.")
    else:
        maior_nome = max(nomes, key=len)
        print(f"Maior nome começando com 'a': {maior_nome}")
