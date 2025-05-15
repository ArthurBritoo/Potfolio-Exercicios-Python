N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    print("P" if (A + B) % 2 == 0 else "I")