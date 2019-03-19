import sys
sys.stdin = open("뿔의숲_input.txt")

tc = int(input())
for T in range(1, tc+1):
    uni = 0
    twin = 0
    N, M = map(int, input().split())
    for i in range(M):
        if N == M:
            uni = M
            break
        elif N < (M-i)*2:
            continue
        elif N == (M-i)*2:
            twin = M
        elif i == N - (M-i)*2:
            uni = i
            twin = M-i
            break
    print('#%s %d %d' % (T, uni, twin))