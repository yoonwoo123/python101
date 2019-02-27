def bfs(v):
    global G, V
    queue = []
    queue.append(v)
    visited[v] = True # enQueue 할때 방문체크하고 프린트도 해야 수월하다.
    print(v, end=" ")
    while queue != 0:
        t = queue.pop(0)
        for w in range(1, V+1):
            if G[t][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1
                print(w, end=" ")

# def dfs_recursive(v): # 재귀
#     global G, visited, V
#     visited[v] = 1
#     print(v, end = ' ')
#
#     for w in range(1, V+1):
#         if G[v][w] == 1 and visited[w] == 0:
#             dfs_recursive(w)

import sys
sys.stdin = open("연습문제3_input.txt")

V, E = map(int, input().split()) # V = 7, E = 8
temp = list(map(int,input().split())) # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

# 인접행렬
G = [[0 for i in range(V+1)] for j in range(V+1)] # 2차원 초기화 0, 0 ~ 7, 7
visited = [0 for i in range(V+1)] # [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(E):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1

# for i in range(1, V+1):
#     print("{} {}".format(i, G[i]))
bfs(1)
# print(visited)