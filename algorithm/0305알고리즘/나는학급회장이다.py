import sys
sys.stdin = open("나는학급회장이다_input.txt")

N = int(input())
one_cnt = [0] * 4
two_cnt = [0] * 4
thr_cnt = [0] * 4
one = 0
two = 0
thr = 0
for i in range(N):
    scores = list(map(int, input().split()))
    for x in range(3):
        if x == 0:
            one_cnt[scores[0]] += 1 # 점수
        elif x == 1:
            two_cnt[scores[1]] += 1
        elif x == 2:
            thr_cnt[scores[2]] += 1
    one += scores[0]
    two += scores[1]
    thr += scores[2]
for i in range(N):
    if one > two:
        if one > thr:

    elif one < two:
        if two > thr:
            


print(one, two, thr)
print(one_cnt, two_cnt, thr_cnt)