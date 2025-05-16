def somaImposto(taxaImposto, custo):
    impostoVenda = custo + (custo * taxaImposto/100)
    return impostoVenda

# Exemplo de uso:
if __name__ == "__main__":
    print(somaImposto(10, 100))  # 110.0
