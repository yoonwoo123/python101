import sys
sys.stdin = open('sw02_압축_input.txt')

testcases = int(input())
tmp = []
for T in range(testcases):
    print(f'#{T+1}')
    N = int(input())
    for A in range(N):
        Char, Num = input().split()
        Num = int(Num)
        # 빈 배열에 넣고 그 배열의 10번째까지 출력하자.
        for i in range(Num):
            tmp.append(Char)
        if len(tmp) >= 10:
            for x in range(10):
                print(tmp.pop(0), end='')
            print()
        if A == N-1:
            while len(tmp) != 0:
                if len(tmp) <= 10:
                    for x in range(len(tmp)):
                        print(tmp.pop(0), end='')
                    print()
                if len(tmp) > 10:
                    for x in range(10):
                        print(tmp.pop(0), end='')
                    print()