def checkNumero(numero):
    if numero > 0:
        return "P"
    else:
        return "N"

# Exemplo de uso:
if __name__ == "__main__":
    print(checkNumero(10))   # P
    print(checkNumero(-5))   # N
    print(checkNumero(0))    # N
