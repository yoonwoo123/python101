import sys
sys.stdin = open('암호_input.txt')

# pwd = [[0,0,0,1,1,0,1], # 0
#        [0,0,1,1,0,0,1], # 1
#        [0,0,1,0,0,1,1],
#        [0,1,1,1,1,0,1],
#        [0,1,0,0,0,1,1],
#        [0,1,1,0,0,0,1],
#        [0,1,0,1,1,1,1],
#        [0,1,1,1,0,1,1],
#        [0,1,1,0,1,1,1],
#        [0,0,0,1,0,1,1]] # 9
pwd = [[2, 1, 1],
       [2, 2, 1],
       [1, 2, 2],
       [4, 1, 1],
       [1, 3, 2],
       [2, 3, 1],
       [1, 1, 4],
       [3, 1, 2],
       [2, 1, 3],
       [1, 1, 2]]

asc = [[0, 0, 0, 0], # 0
       [0, 0, 0, 1], # 1
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 1, 0, 0],
       [0, 1, 0, 1],
       [0, 1, 1, 0],
       [0, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 1],
       [1, 0, 1, 0],
       [1, 0, 1, 1],
       [1, 1, 0, 0],
       [1, 1, 0, 1],
       [1, 1, 1, 0],
       [1, 1, 1, 1]] # F

def aToh(c):
    if c <= '9':return ord(c) - ord('0')
    else: return ord(c) - ord('A') + 10

def makeT(x):
    for i in range(4):
        t.append(asc[x][i])

# 뒤에서부터 찾자 0이면 넘어가고 1일때부터 암호이다. insert(0)으로 앞으로쌓자

tc = int(input())
for T in range(1, 3):
    serial = []
    table = []
    flag = 0
    res = 0
    pwcnt = 0
    N, M = map(int, input().split())
    for _ in range(N):
        line = list(input())
    # 16진수 -> 2진수 변환
        t = []
        for i in range(M):  # 바꿔야함
            makeT(aToh(line[i]))  # sixteen도 바꿔야함
        table.append(t)
    # for g in table:
    #     print(g)
    serial_num = 0

    for z in range(1, N):
        # line[z] = line[z][::-1]
        table[z] = table[z][::-1]
        one = 0 # 다른암호만날때에도 0으로 초기화해줘야함
        zero = 0
        password = []

        for i in range(M*4):
            if pwcnt == 4: # password 3자리가 쌓이면 break
                password.pop(-1)
                my_min = min(password)
                for f in range(3):
                    password[f] = int(password[f] // my_min)
                for hg in range(10):
                    if password == pwd[hg]:
                        serial.insert(0, hg) # serial을 8자리 구한다.

                        if len(serial) == 8:
                            odd_sum = 0
                            even_sum = 0
                            for i in range(1, 9):
                                if i % 2 == 1:
                                    odd_sum += serial[i - 1]
                                else:
                                    even_sum += serial[i - 1]
                            if (odd_sum * 3 + even_sum) % 10 == 0:
                                res += sum(serial)
                                print(serial)
                                serial_num += 1
                            serial = []


                password = []
                pwcnt = 0
            if table[z][i] == 1 and table[z - 1][i] == 0:
                if zero != 0:
                    password.insert(0, zero)
                    zero = 0
                    pwcnt += 1
                one += 1
            elif table[z][i] == 0 and table[z - 1][i] == 0:
                if one != 0:
                    password.insert(0, one)
                    one = 0
                    pwcnt += 1
                zero += 1
    print('#%d %d' % (T, res))
    print(serial_num)
