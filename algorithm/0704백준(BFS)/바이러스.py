'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''

# N = int(input())
# M = int(input())
# table = [[0 for _ in range(N+1)] for _ in range(N+1)]
# arr = []
# chk = [0] * (N+1)
# chk[1] = 1
# for i in range(M):
#     arr.append(list(map(int, input().split())))
# for x in range(M):
#     table[arr[x][0]][arr[x][1]] = 1
#
# for g in table:
#     print(g)

import collections

def bfs(v):
    q = collections.deque()
    q.append(v)
    visited[v] = True
    cnt = 0

    while q:
        v = q.popleft()
        for e in adj[v]:
            if not visited[e]:
                visited[e] = True
                q.append(e)
                cnt += 1

    return cnt

V = int(input())
E = int(input())

adj = [[] for _ in range(V+1)]
visited = [False for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
print(bfs(1))