import sys
sys.stdin = open("Forth_input.txt")
testcases = int(input())
for T in range(testcases):
    data = list(input().split())
    f_x = ['+', '-', '*', '/', '.']
    s = []
    for i in range(len(data)):
        if data[i] not in f_x:
            s.append(data[i])
        if data[i] == '+':
            if len(s) < 2:
                print(f'#{T + 1} error')
                break
            a = int(s.pop())
            b = int(s.pop())
            s.append(b + a)
        if data[i] == '-':
            if len(s) < 2:
                print(f'#{T + 1} error')
                break
            a = int(s.pop())
            b = int(s.pop())
            s.append(b - a)
        if data[i] == '*':
            if len(s) < 2:
                print(f'#{T + 1} error')
                break
            a = int(s.pop())
            b = int(s.pop())
            s.append(b * a)
        if data[i] == '/':
            if len(s) < 2:
                print(f'#{T + 1} error')
                break
            a = int(s.pop())
            b = int(s.pop())
            s.append(b // a)
        if data[i] == '.':
            if len(s) != 1:
                print(f'#{T + 1} error')
                break
            else:
                print(f'#{T+1} {s.pop()}')