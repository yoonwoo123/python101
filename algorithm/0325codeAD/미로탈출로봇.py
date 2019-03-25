import sys
sys.stdin = open("미로탈출로봇_input.txt")

col, row = map(int, input().split())
sc, sr, ec, er = map(int, input().split())
table = []
dr = [-1, 1, 0, 0] # 상하좌우
dc = [0, 0, -1, 1]

for x in range(row):
    table.append(list(map(int, list(input()))))
# print(table)

def BFS():
    que = []
    # 1. 시작점을 큐에 저장(방문표시)
    que.append([sr, sc, 0])
    table[sr][sc] = 1 # 방문
    while len(que) != 0: # 큐가 빌때까지 반복
        r, c, time = que.pop(0)
        if r == er and c == ec:
            return time
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (nr < 1 or nc < 1 or nr > row or nc > col):
                continue
            if table[nr][nc] != 0:
                continue
            que.append([nr, nc, time + 1])
            table[nr][nc] = 1 # 방문
    return -1
        # 2. 큐에서 데이타 읽기 (현재 위치, 현재 시간)
        # 3. 사방탐색하면서 연결점(길)을 찾아 큐에 저장
            # 3-1. 맵 범위 이내 여부 체크
            # 3-2. 연결점을 찾아서 큐에 저장(방문표시)
    # 4. 큐가 비었을 경우 (엣지 케이스)
print(BFS())