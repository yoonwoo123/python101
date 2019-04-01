import sys
sys.stdin = open("건물세우기_input.txt")

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

# 여교수님 코드
# def DFS(no, sum): # no = depth로 들어가는 번호
#     global min
#     if no >= N:
#         if sum < sol:
#             sol = sum
#         return
#     else:
#         for i in range(N):
#             if chk[i]: continue
#             chk[i] = 1
#             DFS(no+1, sum + arr[no][i])
#             chk[i] = 0
#



my_min = 99999999999999
arr = []
N = int(input())
for i in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
a = [n for n in range(N)]
perm(N, 0, 0)

print(my_min)