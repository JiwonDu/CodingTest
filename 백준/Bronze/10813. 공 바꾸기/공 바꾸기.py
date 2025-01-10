N, M = map(int, input().split())
Array = list(range(1, N + 1))

for _ in range(M):
    a, b = map(int, input().split())
    Array[a-1], Array[b-1] = Array[b-1], Array[a-1]

print(*Array)