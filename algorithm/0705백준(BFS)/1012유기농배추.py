'''

'''

import collections

def BFS(x, y):
    q = collections.deque()
    q.append([x, y])
    arr[x][y] = 0 # 방문체크
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= H or ny >= W: continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0 # 방문체크
                q.append([nx, ny])


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

tc = int(input())
for T in range(1, tc+1):
    W, H, K = map(int, input().split())
    arr = [[0 for y in range(W)] for x in range(H)]
    for _ in range(K):
        tmp = list(map(int, input().split()))
        arr[tmp[1]][tmp[0]] = 1
    cnt = 0
    for x in range(H):
        for y in range(W):
            if arr[x][y] == 1:
                cnt += 1
                BFS(x, y)


                # for g in arr:
                #     print(g)
                # print()
                # print(cnt)

    print(cnt)