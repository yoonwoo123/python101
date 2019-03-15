import sys
sys.stdin = open("배열최소합_input.txt")

def perm(n, r, q): # sum을 넘겨줘야함.
    # 가지치기 조건 들어가야함
    if r== 0:
        while q != 0:
            q = q - 1
            p.append(t[q])
    else:
        for i in range(n-1, -1, -1):
            a[i], a[n-1] = a[n-1] , a[i]
            t[r-1] = a[n-1]
            perm(n-1, r-1, q)
            a[i], a[n-1] = a[n-1], a[i]

testcases = int(input())
for T in range(testcases):
    N = int(input())
    table = []
    total = []

    for i in range(N): # 세로 : x , 가로 : y  테이블 생성
        tmp =list(map(int, input().split()))
        table.append(tmp)

    a = [n for n in range(1, N+1)]
    # print(a)
    t = [0] * N
    p = []

    perm(N, N, N)

    total = []
    l = len(p)
    for _ in range(int(l//N)):
        my_sum = 0
        for i in range(N):
            my_sum += table[i][p.pop(0)-1]
        total.append(my_sum)
    print("%s%d %d" % ('#', T+1, min(total)))