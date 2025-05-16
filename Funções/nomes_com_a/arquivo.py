def ler_nomes_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return [linha.strip() for linha in arquivo]
