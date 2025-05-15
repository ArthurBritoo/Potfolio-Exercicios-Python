M, N = map(int, input().split())
plantacao = [list(map(int, input().split())) for _ in range(M)]
max_area = max(sum(linha) for linha in plantacao)
print(max_area)