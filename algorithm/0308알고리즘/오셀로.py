import sys
sys.stdin = open("오셀로_input.txt")

tc = int(input())
dx = [0, 1, -1, 1, -1, 0, 1, -1]
dy = [1, 1, -1, 0, 0, -1, -1, 1]
for T in range(tc):
    N, M = map(int, input().split())
    table = [[0 for _ in range(N)] for _ in range(N)] # N 크기의 빈테이블 생성
    # 초기 놓여있는 돌  2x2 table에 채우기
    for x in range(int(N//2) - 1, int(N//2) +1):
        table[x][x] = 2
    for y in range(int(N//2) - 1, int(N//2) +1):
        table[y][N-y-1] = 1
    # for i in range(N):
    #     print(table[i])
    # print()
    # 놓은 돌이 1일 때 자신의 8방향에서 2가 있는지 찾는다.
    # 2를 찾으면 그쪽으로 가면서 끝에 2가 있는경우만! 그 사이를 2로 바꿔준다.
    # 즉 돌을 놓았을 때 8방향 전부 0이나 벽이 나올때까지 찍어봐서
    # 2가 있는경우에만 바꿔준다.
    # 멈추는 경우는 벽을 만나거나 1을 만나거나 0을 만날경우

    # 놓은 돌이 2일 때 자신의 8방향에서 1가 있는지 찾는다.
    # 1를 찾으면 그쪽으로 가면서 끝에 1가 있는경우만! 그 사이를 1로 바꿔준다.
    # 멈추는 경우는 벽을 만나거나 2를 만날경우
    for i in range(M):
        pos_y, pos_x, color = map(int, input().split()) # color = 1 흑 2 백
        xx = pos_x -1
        yy = pos_y -1
        fir_x = xx # 처음 들어온 돌의 위치
        fir_y = yy
        # print()
        # print(xx, yy, color)
        table[xx][yy] = color
        if color == 1:
            for d in range(8):
                flag = 0
                nx = fir_x + dx[d] # 놓인돌 기준 8방향 검사 1나올때까지
                ny = fir_y + dy[d]
                if nx >= N or nx < 0 or ny >= N or ny < 0: # range 오류방지
                    continue
                if table[nx][ny] != 0: # 0이 아닐 경우 들어감
                    while True:
                        xx = nx
                        yy = ny
                        nx = xx + dx[d]
                        ny = yy + dy[d]
                        if nx >= N or nx < 0 or ny >= N or ny < 0:  # range 오류방지
                            break
                        elif table[nx][ny] == 1:
                            flag = 1
                            break
                        elif table[nx][ny] == 0:
                            break
                nx = fir_x + dx[d]# nx를 재설정
                ny = fir_y + dy[d]# flag가 1인 방향만 돌려준다.
                if nx >= N or nx < 0 or ny >= N or ny < 0: # range 오류방지
                    continue
                if table[nx][ny] == 2 and flag == 1: # 가까운 2를 찾았을 때 들어감
                    while True:
                        if nx >= N or nx < 0 or ny >= N or ny < 0:  # range 오류방지
                            break
                        if table[nx][ny] == 2:
                            table[nx][ny] = 1

                            # for g in table:
                                # print(g)
                            # print()
                            xx = nx
                            yy = ny
                            nx = xx + dx[d]
                            ny = yy + dy[d]
                        else:
                            break

        elif color == 2:
            for d in range(8):
                flag = 0
                nx = fir_x + dx[d]  # 놓인돌 기준 8방향 검사 1나올때까지
                ny = fir_y + dy[d]

                if nx >= N or nx < 0 or ny >= N or ny < 0:  # range 오류방지
                    continue
                if table[nx][ny] != 0:  # 0이 아닐 경우 들어감
                    while True:
                        xx = nx
                        yy = ny
                        nx = xx + dx[d]
                        ny = yy + dy[d]
                        if nx >= N or nx < 0 or ny >= N or ny < 0:  # range 오류방지
                            break
                        elif table[nx][ny] == 2:
                            flag = 1
                            break
                        elif table[nx][ny] == 0:
                            break
                nx = fir_x + dx[d]  # nx를 재설정
                ny = fir_y + dy[d] # flag가 1인 방향만 돌려준다.
                if nx >= N or nx < 0 or ny >= N or ny < 0:  # range 오류방지
                    continue
                if table[nx][ny] == 1 and flag == 1:  # 가까운 1를 찾았을 때 들어감
                    while True:
                        if nx >= N or nx < 0 or ny >= N or ny < 0:  # range 오류방지
                            break
                        if table[nx][ny] == 1:
                            table[nx][ny] = 2
                            # for g in table:
                            #     print(g)
                            # print()
                            xx = nx
                            yy = ny
                            nx = xx + dx[d]
                            ny = yy + dy[d]
                        else:
                            break
    # for i in range(N):
    #     print(table[i])

    one = 0
    two = 0
    for x in range(N):
        for y in range(N):
            if table[x][y] == 1:
                one += 1
            elif table[x][y] == 2:
                two += 1
    print("%s%d %d %d" % ('#', T+1, one, two))


