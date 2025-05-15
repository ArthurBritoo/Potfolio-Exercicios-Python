def expo(a, n):
    if a == 0 and n == 0:
        return "indefinido"
    if n == 0:
        return 1
    return a * expo(a, n - 1)