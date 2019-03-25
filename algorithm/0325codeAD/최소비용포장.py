import sys
sys.stdin = open('최소비용포장_input.txt')

N = int(input())
numbers = list(map(int, input().split()))
total = 0

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

# 버블 정렬
def Bubblesort(N):
    for i in range(2): # 돌리고 싶은 만큼 돌릴 수 있다.
        for j in range(i+1, N):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

Bubblesort(N)
for i in range(N-1):
    s = numbers.pop(0) + numbers.pop(0)
    total += s
    numbers.insert(0, s)
    Bubblesort(N-(i+1))
print(total)

# 함수 이용
# candys.sort()
# for i in range(N-1):
#     s = candys.pop(0) + candys.pop(0)
#     total += s
#     candys.insert(0, s)
#     candys.sort()
# print(total)