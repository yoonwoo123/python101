import sys
sys.stdin = open('빙고_input.txt')

# # 가로줄 합 구하기
#
# def row(table):
#     global table, bingo
#     for x in range(5):
#         line_sum = 0
#         for y in range(5):
#             line_sum += table[x][y]
#         if line_sum == 0:
#             bingo += 1

bingo = 0
table = []
bingo_num = []
for i in range(5): # 빙고판 생성
    tmp = list(map(int ,input().split()))
    table.append(tmp)

for i in range(5): # 빙고숫자배열 생성
    numbers = list(map(int ,input().split()))
    for num in numbers:
        bingo_num.append(num)
cnt = 0
bin_cnt = 0
# for x in range(5):
#     for y in range(5):
while bingo != 3:
    while cnt < 25:
        if table[cnt // 5][cnt % 5] == bingo_num[bin_cnt]:
            table[cnt // 5][cnt % 5] = 0 # 맞는 빙고를 0으로 지우기
            # 가로
            for x in range(5):
                line_sum = 0
                for y in range(5):
                    line_sum += table[x][y]
                if line_sum == 0:
                    bingo += 1
            if bingo > 2:
                break
            # 세로
            for x in range(5):
                line_sum = 0
                for y in range(5):
                    line_sum += table[y][x]
                if line_sum == 0:
                    bingo += 1
            if bingo > 2:
                break
            # 대각선-왼위
            line_sum = 0
            for y in range(5):
                line_sum += table[y][y]
            if line_sum == 0:
                bingo += 1
            if bingo > 2:
                break
            # 대각선-오위
            line_sum = 0
            for y in range(5):
                line_sum += table[y][4-y]
            if line_sum == 0:
                bingo += 1
            if bingo > 2:
                break
            bin_cnt += 1
            cnt = 0
            bingo = 0
        else:
            cnt += 1   # 횟수 1 증가
    if bingo > 2:
        break
# for i in range(len(bingo_num)):
#     if bingo_num[i]
print(bin_cnt + 1)

# 나중에 사회자가 부른 수 = bingo_num의 인덱스 + 1

# 맞는 빙고를 0으로 지울때마다 table의 가로줄 합, 세로줄 합, 대각선 합을 구하는 함수를 사용하여
# 줄 하나에 sum이 0이 나오면 bingo += 1 해준다. 그래서 bingo == 3 이 되는 순간
# 그 때의 cnt + 1 을 출력하자.