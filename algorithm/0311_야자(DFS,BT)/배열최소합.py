# 이렇게 하면 테스트케이스 10 개중 3개 밖에 맞지 않는다.
# BT 로 다시 짜자
import sys
sys.stdin = open("배열최소합_input.txt")
testcases = int(input())
for T in range(testcases):
    tmp = []
    table = []
    res = []
    N = int(input())
    visit = [0] * N
    for i in range(N):
        tmp =list(map(int, input().split()))
        table.append(tmp)
    # 세로 : x , 가로 : y
    h = 0
    idx = []
    for x in range(N):
        min = 11
        for y in range(N): # 최소값 찾기 방문안했을 때만 최소값 될수 있다.
            if table[x][y] <= min and visit[y] == 0:
                min = table[x][y]
        res.append(min)
        for i in range(N): # 방문처리
            if min == table[x][i]:
                visit[i] = 1
                break
        for i in range(N): # min이 2개이상일 경우 인덱스를 찾는다.
            if table[x].count(min) > 1:
                if min == table[x][i]:
                    idx.append(i) # idx = [2, 3]

        if len(idx) > 1: # 인덱스가 3개이상일경우 그 중 min을 찾아 더해주자
            h_min=11
            for o in range(len(idx)):
                if table[x][idx[o]] < h_min:
                    h_min = table[x][idx[o]]
            if min > h_min:
                res[-1] = h_min
    print("%s%d %d" % ('#', T+1, sum(res)))

    # 세로줄에서 최소값이 2개 이상이면 안되기 때문에
    # visited 표시를 하자 N의 길이만큼의 [0] * N 을 만들어준후
    # 최소값으로 뽑아낸 인덱스의 y 값을 방문표시 1 해주고
    # 다음 최소값을 뽑을 땐 visit == 0 인 곳에서만 뽑는다.

    # table의 min이 2개 이상일때 그 다음줄에서 min이 2개이상이였던 idx와 같은 세로줄의
    # idx에 최소값을 비교할 경우 그 최소값을 뽑아라.