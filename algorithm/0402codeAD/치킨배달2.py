import sys, itertools
sys.stdin = open("치킨배달2_input.txt")

def BFS():
    que = []
    for i in range(len(chicken)): # 치킨집 좌표를 que에 전부 넣는다.
        que.append([chicken[i][0], chicken[i][1]], 0)
    while que:
        x, y, time = que.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue

            if arr[nx][ny] == 0:
                arr[nx][ny] = time + 1
                que.append([nx, ny, time + 1])
            elif arr[nx][ny] == 1:
                arr[nx][ny] = time + 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))
# print(arr)
# 로봇-스낵 문제처럼 치킨집-집 문제이다. 치킨집 좌표는 뽑아두고
# 치킨집을 어떻게 고를지 조합으로 뽑아낸다.

# 집좌표를 순열로 바꿔가면서 최소값을 찾는다.
# 치킨집 = 2, 집 = 1

# 2. 토마토 응용
# 어차피 모든집까지의 거리를 계산해야하므로 치킨집을 토마토로 생각
# 각 집까지의 거리를 BFS로 찍어서 각 집까지 걸리는 시간을 저장한후
# 각집에 저장된 시간값을 더해서 그중 최소를 찾는다.

house = []
chicken = []
for x in range(N):
    for y in range(N):
        if arr[x][y] == 1:
            house.append([x, y])
        if arr[x][y] == 2:
            chicken.append([x, y])


