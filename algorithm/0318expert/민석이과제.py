import sys
sys.stdin = open("민석이과제_input.txt")

tc = int(input())
for T in range(1, tc+1):
    N, K = map(int, input().split())
    numbers = set(map(int, input().split()))
    a = set(range(1, N+1))
    print('#%s' % (T), end=" ")
    for num in (a-numbers):
        print(num, end=" ")
    print()