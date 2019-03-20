import sys
sys.stdin = open('건초더미_input.txt')

tc = int(input())
for T in range(1, tc+1):
    dummy = []
    res = 0
    N = int(input())
    for _ in range(N):
        dummy.append(int(input()))
    avg = int(sum(dummy)/N)
    for num in dummy:
        if num < avg:
            res += avg-num
    print('#%s %d' % (T, res))