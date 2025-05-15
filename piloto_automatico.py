X = int(input())
total = 0
for _ in range(X):
    graus = int(input())
    total += graus
    if total >= 360:
        total -= 360
print(total)