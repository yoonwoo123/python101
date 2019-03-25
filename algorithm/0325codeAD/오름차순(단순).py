import sys
sys.stdin = open('오름차순(단순)_input.txt')

N = int(input())
numbers = list(map(int, input().split()))

# 속도는 sorted < 병합 <= 퀵 < 버블 순이다.

# O(N^2) 단순정렬
# def sort(s, e):
#     global N, arr
#     for i in range(e):
#         for j in range(i+1, N+1):
#             if arr[i]>arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]

# 함수쓰면
# for num in sorted(numbers):
#     print(num, end=" ")

# 버블 정렬
# for i in range(N-1): # 돌리고 싶은 만큼 돌릴 수 있다.
#     for j in range(i+1, N):
#         if numbers[i] > numbers[j]:
#             numbers[i], numbers[j] = numbers[j], numbers[i]
# for num in numbers:
#     print(num, end=" ")

# 퀵 정렬  0  N-1   O(N Log N)
# def Qsort(S, E):
#     if S >= E:
#         return
#     P = E
#     T = S
#     for L in range(S, E+1):
#         if numbers[L] < numbers[P]:
#             numbers[L], numbers[T] = numbers[T], numbers[L]
#             T += 1
#     numbers[T], numbers[P] = numbers[P], numbers[T] # 1회전 끝나고 target과 pivot을 한번교환
#     Qsort(S, T-1)
#     Qsort(T+1, E)
# Qsort(0, N-1)
# for num in numbers:
#     print(num, end=" ")

# 병합 정렬 O(N Log N)
#         0, N-1
def Msort(s, e):
    if s >= e:
        return
    m = (s+e)//2
    Msort(s, m)
    Msort(m+1, e)
    i = s
    j = m+1
    k = s
    while i <= m and j <= e: # 왼쪽영역, 오른쪽영역을 나누어서 임시버퍼에 비교한 후 저장
        if numbers[i] < numbers[j]:
            temp[k] = numbers[i]
            k += 1
            i += 1
        else:
            temp[k] = numbers[j]
            k += 1
            j += 1
    while i <= m: # 왼쪽영역이 남아있으면 임시버퍼에 저장
        temp[k] = numbers[i]
        k += 1
        i += 1
    while j <= e: # 오른쪽영역이 남아있으면 임시버퍼에 저장
        temp[k] = numbers[j]
        k += 1
        j += 1
    for i in range(s, e+1): # 임시버퍼를 원버퍼에 저장
        numbers[i] = temp[i]

temp = [0] * N
Msort(0, N-1)
for num in numbers:
    print(num, end=" ")