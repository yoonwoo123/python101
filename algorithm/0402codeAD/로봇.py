import sys, itertools
sys.stdin = open("로봇_input.txt")

def BFS(sx, sy, sdir, cnt):
    que = []
    que.append([sx, sy, sdir])
    while que:
        x, y, dir = que.pop(0)

        for i in range(1, 5):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= X or ny >= Y: continue



dx = [0, 0, 0, 1, -1] # 우 좌 하 상
dy = [0, 1, -1, 0, 0]
direction = [1, 2, 3, 4] # 동 서 남 북

X, Y = map(int, input().split())
arr = []
for i in range(Y):
    arr.append(list(map(int, input().split())))
# 1은 벽 0만 다닐수 있다.
sx, sy, sdir = map(int, input().split())
ex, ey, edir = map(int, input().split())

