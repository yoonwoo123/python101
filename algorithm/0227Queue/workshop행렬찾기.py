import sys
sys.stdin = open('workshop행렬찾기_input.txt')

tc = int(input())
for T in range(tc):
    table = []
    N = int(input())
    for i in range(N):
        table.append(list(map(int, list(input().split()))))

    ware = []
    col = 0
    row = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] != 0:
                box = []
                i2 = i
                j2 = j
                col = 0
                row = 0
                while True: # 행의 개수 찾기
                    if table[i2][j] != 0:
                        row += 1
                        i2 += 1
                    if table[i2][j] == 0:
                        box.append(row)
                        break

                while True: # 열의 개수 찾기
                    if table[i][j2] != 0:
                        col += 1
                        j2 += 1
                    if table[i][j2] == 0:
                        box.append(col)
                        break
                box.insert(0, row * col)
                ware.append(box)
                for c in range(i, i + row): # clear
                    for l in range(j, j + col):
                        table[c][l] = 0
            else:
                continue
    ware.sort()
    print(f'#{T + 1} {len(ware)}', end=" ")
    for i in range(len(ware)):
        print(ware[i][1], end=" ")
        print(ware[i][2], end=" ")
    print()