import sys
sys.stdin = open("햄버거_input.txt")

def comb(no, start):
    if no > N:
        print(a)
        return
    else:
        for i in range(start, N):
            a[no] = i
            comb(no + 1, i + 1)

# def DFS4(n, start): # 조합
#     if n>N:
#         for i in range(N): print(arr[i], end=' ')
#         print()
#         return
#     for i in range(start, 5):
#         arr[n]=i
#         DFS4(n+1, i) # 조합은 i 가 아닌 i + 1 중요!

tc = int(input())
# L 이하의 칼로리면서 맛의 점수 score가 가장 높은 점수출력
for T in range(1, tc + 1):
    N, L = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    # print(arr)
    # 조합으로 모든 경우의 수를 계산해보고 가지를 쳐주자.
    a = [0] * (N+1)
    comb(5, 0)

    # arr = [0] * (N + 1)
    # chk = [0] * 7
    # DFS4(0, 0)

