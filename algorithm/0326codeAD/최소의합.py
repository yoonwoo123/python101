import sys
sys.stdin = open("최소의합_input.txt")

def perm(n, k, tot):
    global my_min
    if my_min <= tot:
        return
    if n == k:
        tot = 0
        for x in range(N):
            tot += arr[x][a[x]]
        if my_min > tot:
            # print(a)
            my_min = tot
            # print(my_min)
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1, tot + arr[k][a[k]])
            a[i], a[k] = a[k], a[i]


N = int(input())
arr = []
a = [n for n in range(N)]
my_min = 99999999999999
easymin = 0
for i in range(N):
    arr.append(list(map(int, input().split())))
for i in range(N):
    easymin += min(arr[i])
perm(N, 0, 0)
# 1] 첫번째 방법: 열의 중복허용한 순열
print(easymin)
print(my_min)






# #------------------- 한욱쌤 스타일---------------
# def perm(n, r, q): # sum을 넘겨줘야함.
#     # 가지치기 조건 들어가야함
#     if r== 0:
#         while q != 0:
#             q = q - 1
#             p.append(t[q])
#     else:
#         for i in range(n-1, -1, -1):
#             a[i], a[n-1] = a[n-1] , a[i]
#             t[r-1] = a[n-1]
#             perm(n-1, r-1, q)
#             a[i], a[n-1] = a[n-1], a[i]
#
# N = int(input())
# table = []
# total = []
#
# for i in range(N): # 세로 : x , 가로 : y  테이블 생성
#     tmp =list(map(int, input().split()))
#     table.append(tmp)
#
# a = [n for n in range(1, N+1)]
# # print(a)
# t = [0] * N
# p = []
# tot = 0
# for g in table:
#     tot += min(g)
#
# perm(N, N, N)
#
# total = []
# l = len(p)
# for _ in range(int(l//N)):
#     my_sum = 0
#     for i in range(N):
#         my_sum += table[i][p.pop(0)-1]
#     total.append(my_sum)
# print(tot)
# print(min(total))