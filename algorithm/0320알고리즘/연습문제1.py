import sys
sys.stdin = open('연습1_input.txt')
# 2진수 -> 10진수
arr = list(map(int, input()))

for i in range(10):
    n = 0
    for j in range(i*7, i*7+7, 1):
        n = n * 2 + arr[j]
    print(n, end=" ")
print()