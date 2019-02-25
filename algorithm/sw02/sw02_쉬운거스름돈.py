import sys
sys.stdin = open('sw02_쉬운거스름돈_input.txt')

testcases = int(input())
for T in range(testcases):
    cnt = []
    cash = list(map(int,(input().split())))
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for m in money:
        if cash[0] >= m:
            cnt.append(cash[0] // m)
            cash[0] = cash[0] % m
        else:
            cnt.append(0)
    print(f'#{T+1}')
    print(' '.join(list(map(str, cnt))))