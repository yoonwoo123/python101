dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    global ans
    q = [(x,y)]
    while len(q):
        x,y = q.pop(0)

        if ans < mat[x][y] : ans = mat[x][y]
        mat[x][y] = 0

        for i in range(4):
            newX, newY = x + dx[i], y + dy[i]
            if 0 <= newX < n and 0 <= newY < n and mat[newX][newY]:
                    q.append((newX, newY))


def dfs(x, y):
    global ans
    if ans < mat[x][y] : ans = mat[x][y]
    mat[x][y] = 0
    for i in range(4):
        newX, newY = x + dx[i], y + dy[i]
        if 0 <= newX < n and 0 <= newY < n and mat[newX][newY]:
            dfs(newX, newY)

t = int(input())
for case in range(1, t+1):
    n = int(input())

    mat = [0 for i in range(n)]
    for i in range(n):
        mat[i] = list(map(int, input().split()))

    ans = 0
    cnt = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j]:
                #bfs(i,j)
                dfs(i,j)
                cnt += 1
    print("#%i %i" % (case, cnt))