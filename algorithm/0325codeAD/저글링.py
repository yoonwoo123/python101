import sys
sys.stdin = open("저글링_input.txt")

def BFS():
    que = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 1. 시작점을 que에 저장 (방문표시)
    que.append([sx, sy, 3])
    arr[sx][sy] = 0 # 저글링주금 방문표시
    while que: # 큐가 빌때까지 반복
        # 2. que에서 데이터 읽기(현재 위치)
        x, y, time = que.pop(0)
        # 사방탐색하면서 연결점(길)을 찾아 큐에 저장
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 맵의 범위 체크
            if nx < 0 or nx >= X or ny < 0 or ny >= Y:
                continue
            if arr[nx][ny] != 1: # 저글링이 아니면 스킵
                continue
            # 3. 연결점 찾아 큐에저장(방문표시)
            que.append([nx, ny, time+1])
            arr[nx][ny] = 0
    # 4. 큐가 빈 상태
    return time

Y, X = map(int, input().split())
arr = []

for i in range(X):
    arr.append(list(map(int, list(input()))))
sy, sx = map(int, input().split())
sy -= 1 # 좌표값이 idx처럼 0이 아닌 1부터 시작하므로 1씩 빼줌
sx -= 1

print(BFS())
jug = 0
for x in range(X):
    for y in range(Y):
        if arr[x][y] == 1:
            jug += 1
print(jug)