import sys
sys.stdin = open('홀짝_input.txt')

tc = int(input())
for T in range(1, tc+1):
    num = int(input())
    if num % 2 == 1:
        print('#%s %s' % (T, 'Odd'))
    else:
        print('#%s %s' % (T, 'Even'))