import sys
sys.stdin = open('색종이_input.txt')

N = int(input())
table = []
for i in range(N):
    cnt = 0
    w, h = map(int, input().split())
    for _ in range(100):
        table.append([0] * 100)
    for x in range(w, w+10):
        for y in range(h, h+10):
            table[x][y] = 1
    for x in range(100):
        for y in range(100):
            cnt += table[x][y]
print(cnt)