def expomod(a, n, m):
    if a == 0 and n == 0:
        return "impossível calcular"
    if m <= 1:
        return "impossível calcular"
    if n == 0:
        return 1
    if n % 2 == 0:
        half = expomod(a, n // 2, m)
        return (half * half) % m
    else:
        return (a * expomod(a, n - 1, m)) % m