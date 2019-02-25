import sys
sys.stdin = open('sw02_파스칼_input.txt')

T = int(input())

for tc in range(1, T + 1):
    num = int(input())
    res = ''
    tmp = ''
    for i in range(1, num + 1):
        tmp = [1] * i
        if i >= 3:
            for j in range(1, len(pre)):
                tmp[j] = int(pre[j - 1]) + int(pre[j])
        pre = tmp
        res += '\n' + ' '.join(map(str, tmp))

    print(f'#{tc} {res}')