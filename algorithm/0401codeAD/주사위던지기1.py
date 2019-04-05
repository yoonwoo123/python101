import sys, itertools
sys.stdin = open("주사위던지기1_input.txt")
# M1 = 중복순열 구조 :
# M2 = 중복조합 구조 : 조합은 내 앞은 볼 필요 없으므로 start를 들고간다
                     # 그래서 start 부터 시작하면 됨
# M3 = 순열 구조
# M4 가 있다면 조합 구조 : start + 1 부터 시작하면됨

def ovperm(n):
    if n >= N:
        for g in range(N):
            print(a[g], end=" ")
        print()
        return
    for i in range(6):
        # p[k] = a[i]
        # a[i], a[k] = a[k], a[i]
        a[n] = i
        ovperm(n + 1)
        # ovperm(n, k+1)
        # a[i], a[k] = a[k], a[i]

def perm(n, k):
    if n == k:
        for g in a:
            print(g, end=" ")
        print()
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1)
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

N = 3
a = [0] * N
print(a)
print(a[1])
p = [0] * 6
ovperm(0)


# N, M = map(int, input().split())
# a = [n for n in range(1, 7)]
# b = [0] * N
# chk = [0] * N

# if M == 1:
#     DFS(0)

# elif M == 2:
#     combi = itertools.combinations_with_replacement(a, N)
#     for c in combi:
#         for i in c:
#             print(i, end=" ")
#         print()
#     # ovperm(N, 0)
#     # print(1)
#
#
# elif M == 3:
#     permu = itertools.permutations(a, N)
#     for c in permu:
#         for i in c:
#             print(i, end=" ")
#         print()

