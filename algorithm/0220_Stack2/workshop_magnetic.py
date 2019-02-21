import sys
sys.stdin = open("workshop_magnetic_input.txt")
testcases = 10
for T in range(testcases):
    w = int(input())
    table = []
    for i in range(w):
        tmp = list(map(int, input().split()))
        table.append(tmp)
    # 1 : N극 , 2 : S극
    # table에있는 1들은 전부 아래로 내려가고 2는 전부 위로 올라간다.
    # 움직이는 경우는 아래 또는 위가 0일 때고 그 외에는 만나면 멈춘다
    # 범위를 넘어가는 경우 그 값은 0으로 바뀐다 (떨어진다)
    # 교착상태의 개수를 셀 때는 N 밑에 S 2개가 쌍으로 이루어진것만센다.

    # 교착이 이루어질수있는 상황은 1 밑에 2가 있는상황뿐이다
    # 즉 1을 발견한 후 2를 찾으면 cnt += 1
    # 그 후 다른 2들은 전부무시가능 그 다음 1을 찾고 그후2찾을시 cnt+=1

    # 교착상태의 개수를 출력하는것이 목표
    # 탐색은 세로로 하자. 세로는 x축 가로는 y축
    cnt = 0
    for y in range(w):
        couple = []
        for x in range(w):
            if table[x][y] == 1:
                couple.append(1)
            if table[x][y] == 2 and len(couple) > 0:
                cnt += 1
                couple= []
    print(f'#{T+1} {cnt}')