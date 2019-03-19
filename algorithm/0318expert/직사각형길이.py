import sys
sys.stdin = open("직사각형길이_input.txt")

tc = int(input())
for T in range(1, tc+1):
    numbers = list(map(int, input().split()))
    for num in numbers:
        if numbers.count(num) == 1 or numbers.count(num) == 3:
            print('#%s %d' % (T, num))
            break