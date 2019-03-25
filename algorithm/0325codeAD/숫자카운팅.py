import sys
sys.stdin = open('숫자카운팅_input.txt')

def lowerSearch(s, e, data):
    sol = -1
    while s<=e:
        m = (s+e)//2
        if data == numbers[m]:
            e = m-1 # 왼쪽 탐색
            sol = m # 찾은 위치가 왼쪽 경계치이므로 백업
        elif data > numbers[m]:
            s = m+1
        else:
            e = m-1
    return sol

def upperSearch(s, e, data):
    while s<=e:
        m = (s+e)//2
        if data == numbers[m]:
            s = m+1 # 오른쪽 탐색
            sol = m # 찾은 위치가 왼쪽 경계치이므로 백업
        elif data > numbers[m]:
            s = m+1
        else:
            e = m-1
    return sol

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
for i in range(M):
    lo = lowerSearch(0, N-1, targets[i])
    if lo >= 0: # 찾았을 경우만 오른쪽끝 탐색
        up = upperSearch(0, N-1, targets[i])
        print(up-lo+1, end=" ")
    else:
        print(0)


# def binary_sCount(target, data):
#     start = 0
#     end = len(data) - 1
#     flag = 0
#     res = 0
#     while start <= end:
#         mid = (start + end) // 2
#         if data[mid] == target:
#             res += 1
#             tmp = mid
#             while True:
#                 if tmp-1 >= 0:
#                     if data[tmp-1] == target:
#                         res += 1
#                         tmp -= 1
#                     else:
#                         break
#                 break
#             while True:
#                 if tmp + 1 < len(data):
#                     if data[tmp+1] == target:
#                         res += 1
#                         tmp += 1
#                     else:
#                         break
#                 break
#             if res != 0:
#                 return res
#             return 0
#         elif data[mid] < target:
#             start = mid + 1
#         else:
#             end = mid -1
