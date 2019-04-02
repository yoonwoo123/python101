def ovperm(n, k):
    if n == k:
        for g in p:
            print(g, end=" ")
        print()
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            p[k] = a[i]
            perm(n, k+1)
            # perm(n-1, k+1)
            a[i], a[k] = a[k], a[i]

def DFS(no): # chk를 하면 순열 chk를 하지 않으면 중복순열
    if no >= N:
        for i in range(N):
            print(b[i], end=" ")
        print()
        return
    for i in range(6):
        # if chk[i]:continue # 1이면 continue, 0이면 진행
        # chk[i] = 1
        b[no] = a[i]
        DFS(no + 1)
        # chk[i] = 0

def comb(no):
    if no >= N:
        for i in range(N):
            print(b[i], end=" ")
        print()
        return
    b[no] = a[no]
    comb(no + 1)
    b[no] = 0
    comb(no + 1)

def combs(no, start): # a[no]번째 구슬을 상자에 담거나 담지 않는 모든 경우
    for i in range(N): print(b[i], end=" ")
    print()
    if no >= N or start >= N:
        return
    for i in range(start, N):
        b[no] = a[i]
        combs(no+1, i+1)
        b[no] = 0

N = int(input())
a = [n for n in range(1, 7)]
b = [0] * N
chk = [0] * N
# DFS(0)
comb(0)