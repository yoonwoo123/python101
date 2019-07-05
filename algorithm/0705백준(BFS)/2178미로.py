import collections

def BFS(x, y):
    q = collections.deque()
    q.append([x, y])
    arr[x][y] = 0 # 방문체크
    memo[x][y] = 1 # 거리기록 처음출발점은 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= H or ny >= W: continue
            if arr[nx][ny] == 1 and memo[nx][ny] > memo[x][y] + 1:
                memo[nx][ny] = memo[x][y] + 1 # 거리기록
                arr[nx][ny] = 0 # 방문체크
                q.append([nx, ny])


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

H, W = map(int, input().split())
memo = [[9999999999 for y in range(W)] for x in range(H)]
arr = []
for _ in range(H):
    arr.append(list(map(int, list(input()))))
# print(arr)
BFS(0, 0)

print(memo[H-1][W-1])