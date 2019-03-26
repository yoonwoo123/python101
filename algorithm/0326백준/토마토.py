import sys, collections
sys.stdin = open("토마토_input.txt")

def BFS(x, y):
    que = collections.deque([])

    que.append([x, y, 1])
    while que:
        x, y, time = que.popleft()
        # print(time)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= X or ny < 0 or ny >= Y:
                continue
            if arr[nx][ny] < 0:
                continue

            if arr[nx][ny] == 0:
                arr[nx][ny] = time+1
                que.append([nx, ny, time + 1])
                continue

            elif arr[nx][ny] >= time+1:
                arr[nx][ny] = time+1 # 방문체크를 1이 아닌 걸리는 시간으로 함
                que.append([nx, ny, time + 1])
    days.append(time)
    # sum(days) == 0 이면 0 출력
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

Y, X = map(int, input().split())
arr = []
days = []

for i in range(X):
    arr.append(list(map(int, input().split())))
# 1 익음 0 익지않음 -1 없음
# 익은토마토 1이 바이러스처럼 출발지점
# 익은토마토는 상자에 여러개 있을 수있다.
# 익은토마토가 모든 안익은 0을 1로 만들때 걸리는 최소시간 = max(days)
# 먼저 익은토마토만 있는경우는 0을 출력하자. -> BFS돌려서 flag ==0일떄
# 다 못 익는 경우는 BFS돌리고 난후 0이 남았나 확인후 남았으면 -1 출력

for x in range(X):
    for y in range(Y):
        if arr[x][y] == 1:
            BFS(x, y)
# print(days)
flag = 0
for x in range(X):
    for y in range(Y):
        if arr[x][y] == 0:
            flag = -1
            break
    if flag == -1:
        break
if flag == -1:
    print(-1)
else:
    print(days[-1]-1)