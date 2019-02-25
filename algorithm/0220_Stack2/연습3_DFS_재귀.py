def dfs(v):
    global G, visited, V
    s = []

    s.append(v) # while문을 충족시키기 위해 첫번째 값을 넣고 시작
    while len(s) != 0:
        v = s.pop()
        if not visited[v] :# visited[v]==0: 방문안했으면
            visited[v] = 1 # 방문체크
            print(v, end=" ")
            for w in range(1, V+1): # 인접한것중 방문안한걸 push
                if G[v][w] == 1 and visited[w] == 0: # 인접해있고 and 방문안했으면
                    s.append(w) # push
def dfs_recursive(v): # 재귀
    global G, visited, V
    visited[v] = 1
    print(v, end = ' ')

    for w in range(1, V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs_recursive(w)

import sys
sys.stdin = open("연습3_input.txt")
V, E = map(int, input().split()) # V = 7, E = 8
temp = list(map(int,input().split())) # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

G = [[0 for i in range(V+1)] for j in range(V+1)] # 2차원 초기화 0, 0 ~ 7, 7
visited = [0 for i in range(V+1)] # [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(E):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1
#
# for i in range(0, E*2, 2): # 입력
#     G[temp[i][temp[i+1]] = 1
#     G[temp[i+1]][temp[i]] = 1


for i in range(1, V+1):
    print("{} {}".format(i, G[i]))
dfs_recursive(1)