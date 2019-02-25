import sys
sys.stdin = open('배열정리_input.txt')
Y, X = map(int, input().split())

table = []
for y in range(Y): # 행만큼 반복
    tmp = list(map(int, input().split()))
    table.append(tmp)
# print(table)
for y in range(Y): # 행
    res = []
    cnt = 1
    one = 1
    for x in range(X): # 열
        if one not in res and table[y][x] == 1: # 첫 1 넣어줄 때  table[행][열]
            res.append(1)
            continue
        if table[y][x] == 0: # 0을 만나면 초기화 해주고 넣어준다.
            res.append(0)
            cnt = 1
            continue
        if table[y][x] == 1 and res[-1] == 0:
            res.append(1)
            continue
        if one in res and res[-1] != 0:
            cnt += 1        # 1을 만나면 cnt +=1 해주고 넣어준다
            res.append(cnt)
            continue

    print(' '.join(map(str, res)))
# 0 또는 1만 존재하므로 끝이 0이 아니기만 하면서 1이 첨들어가지않으면 + 1 해서 넣어주면된다.
# 끝이 0
# 0 을 넣을때 cnt를 초기화 해주자