import sys
sys.stdin = open("예산_input.txt")

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

# def check(m):
#     # 현재 상한가보다 작으면 현 도시예산으로 더하고 아니면 상한가로 더함
#     tot = 0
#     for i in range(N):
#         if arr[i] <= m:
#             tot += arr[i]
#         else:
#             tot += m
#     if tot>M:
#         return 0
#     else:
#         return 1
#     # 총액을 초과하면 실패 0 아니면 성공 1
#
# e = max(arr)
# s, sol = 0, 0
# while s<= e:
#     m = (s+e)//2
#     if check(m):
#         sol = m
#         s = m+1
#     else:
#         e = m-1
# print(sol)

arr.sort()
acc = 0
tot = M
flag = 0
for i in range(N):
    if acc + arr[i] * (N-i) <= M:
        acc += arr[i]
    else:
        tot -= acc
        sang = tot // (N-i)
        flag = 1
        print(sang)
        break
if flag == 0:
    print(arr[-1])