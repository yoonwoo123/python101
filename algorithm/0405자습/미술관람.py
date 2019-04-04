import sys
sys.stdin = open("미술관람_input.txt")

def BFS(x, y, color):
    global sol
    que = []
    que.append([x, y, color])
    arr[x][y] == 'V'
    while que:
        color = que.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if arr[nx][ny] == color:
                arr[nx][ny] = 'V'
                que.append([nx, ny, color])
    sol += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
arr = []
sol = 0
for i in range(N):
    arr.append(list(input()))
# print(arr[1][1])

for x in range(N):
    for y in range(N):
        if arr[x][y] == 'V': continue
        BFS(x, y, arr[x][y])
print(sol)
for g in arr:
    print(g)
print()