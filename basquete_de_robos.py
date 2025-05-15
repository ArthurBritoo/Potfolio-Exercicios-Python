N = int(input())
for _ in range(N):
    dist, altura = map(float, input().split())
    if 12 <= dist <= 18 and altura <= 1.5:
        print("DUCK")
    else:
        print("NAO DUCK")