import sys
sys.stdin = open("어디에단어_input.txt")

tc = int(input())
for T in range(tc):
    N, K = map(int, input().split())
    p_table = []
    table = [[0 for _ in range(N+2)] for _ in range(N+2)]
    for i in range(N):
        p_table.append(list(map(int, list(input().split()))))
    for x in range(1, N+1):
        for y in range(1, N+1):
            table[x][y] = p_table[x-1][y-1] # 벽 계산하기 귀찮으므로 주어진 N보다 2 큰 테이블을 만들어서 넣어준다.
    # for i in range(N+2):
    #     print(table[i])
    res = 0
    for x in range(N+2): # 가로 찾기
        cnt = 0
        for y in range(N+2):
            if table[x][y] == 1:
                cnt += 1
            elif table[x][y] == 0 and cnt == K:
                res += 1
                cnt = 0
            else:
                cnt = 0
    for x in range(N+2): # 세로 찾기
        cnt = 0
        for y in range(N+2):
            if table[y][x] == 1:
                cnt += 1
            elif table[y][x] == 0 and cnt == K:
                res += 1
                cnt = 0
            else:
                cnt = 0
    print("%s%d %d" % ('#', T+1, res))
