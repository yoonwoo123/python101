import sys, collections
sys.stdin = open("장기_input.txt")

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def BFS(x, y, cnt):
    global res
    que = []
    que.append([x, y, cnt])
    arr[x][y] = 1 # 방문체크
    while que:
        x, y, cnt = que.pop(0)
        cnt += 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if arr[nx][ny] == 1: continue
            if arr[nx][ny] == 2:
                res = cnt
                return
            arr[nx][ny] = 1 # 방문처리
            que.append([nx, ny, cnt])

N, M = map(int, input().split())
HX, HY, X, Y = map(int, input().split())
HX -= 1
HY -= 1
X -= 1
Y -= 1
arr = [[0 for _ in range(M)] for _ in range(N)]
arr[HX][HY] = 1 # 말
arr[X][Y] = 2 # 졸병
res = 0
BFS(HX, HY, 0)
print(res)