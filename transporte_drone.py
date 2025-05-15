N = int(input())
peso = 0
for _ in range(N):
    peso += int(input())
print("S" if peso <= 50 else "N")