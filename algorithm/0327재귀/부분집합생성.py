# {1, 2, 3} 모든 부분집합 생성하기

def powerset(n, k): # n :원소의 갯수, k : 현재 depth
    global count
    if n == k:
        count += 1
        print("%d: " % (count), end="")
        for i in range(n): # 각 부분 배열의 원소 출력
            if A[i] == 1:
                print("%d " % data[i], end="")
        print()
    else:
        A[k] = 1 # k번 요소 o
        powerset(n, k + 1) # 다음 요소 포함 여부 결정
        A[k] = 0 # k번 요소 x
        powerset(n, k + 1) # 다음 요소 포함 여부 결정

count = 0
N = 3
A = [0 for _ in range(N)]
data = [1, 2, 3]
powerset(N, 0)