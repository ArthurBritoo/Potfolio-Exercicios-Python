#Um problema típico em ciência da computação consiste em converter um número da sua forma decimal para a forma binária. Implemente este algoritmo.
def binario(n):
    if n == 0:
        return ""
    return binario(n//2) + str(n % 2)
