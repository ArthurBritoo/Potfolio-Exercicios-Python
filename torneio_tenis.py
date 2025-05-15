a, b, c = map(int, input().split())
print("Empate" if a == b == c else ("Carlos" if a > b and a > c else "Paula" if b > a and b > c else "Pedro"))