import sys
sys.stdin = open('회전_input.txt')

def copy():
    for i in range(N):
        for j in range(N):
            table[i][j]= rotate[i][j]


# 회전함수
def rot(cnt):
    global N, rotate
    for z in range(cnt):
        for x in range(N):
            for y in range(N):
                rotate[y][N - 1 - x] = table[x][y]
        copy()

table = []
rotate = []
res = []

N = int(input())
for i in range(N): # 2차원의 table 생성
    tmp = []
    tmp = list(map(int, input().split()))
    table.append(tmp)

for i in range(N): # 2차원의 빈 배열 rotate 생성
    tmp = []
    tmp = [0] * N
    rotate.append(tmp)

# 회전할 각도를 입력받는다.
while True:
    cnt = 0
    num = int(input())
    if num == 0:
        break
    elif num % 90 != 0:
        continue
    else:
        cnt = num // 90
    if cnt > 0:
        rot(cnt)
    for i in range(N):
        for j in range(N):
            print(rotate[i][j], end=" ")
        print()