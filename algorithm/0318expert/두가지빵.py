import sys
sys.stdin = open('두가지빵_input.txt')

tc = int(input())
for T in range(1, tc+1):
    A, B, C = map(int, input().split())
    if C < A and C < B:
        print('#%s %d' % (T, 0))
    elif A >= B:
        print('#%s %d' % (T, int(C//B)))
    else:
        print('#%s %d' % (T, int(C//A)))