V, E = map(int, input().split())
K = int(input())
arr = [[0 for y in range(V+1)] for x in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u][v] = w

for i in range(1, V+1):
    arr[K][i]


print()
for g in arr:
    print(g)
print()