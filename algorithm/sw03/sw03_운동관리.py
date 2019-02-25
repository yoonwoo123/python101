import sys
sys.stdin = open("sw03_운동관리_input.txt")
testcases = int(input())
for T in range(testcases):
    L, U, X = list(map(int, input().split()))
    # L 분 이상 U분 이하 운동을 해야한다.
    # X 분 만큼 운동을 했을 시 모자라나 넘치나? 넘치면 -1 아니면 모자라는 분 출력
    print(f'#{T+1}', end= ' ')
    if L-X >= 0:
        print(L-X)
    if X-U > 0:
        print(-1)
    if L <= X <= U:
        print(0)


