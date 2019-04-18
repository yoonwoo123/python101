import sys, copy
sys.stdin = open("색종이붙이기_input.txt")

def find(o):
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 1:
                # 여기서 함수로 만들자
                for i in range(5):
                    for j in range(5):

                if x >= N or y >= N: continue # 장외로 나가는지
                flag = 0

                for i in range(x, x + o + 1):
                    if flag == 1: break
                    for j in range(y, y + o + 1):
                        if arr[i][j] != 1:
                            flag = 1
                            break
                if flag == 0:
                    cnt[o] += 1
                    for k in range(x, x + o + 1):
                        for t in range(y, y + o + 1):
                            arr[k][t] = o + 2
# def refind(o):
#     for x in range(N-1, N-3-o, -1):
#         for y in range(N-1, N-3-o, -1):
#             flag = 0
#             for i in range(x, x - o - 1, -1):
#                 if flag == 1: break
#                 for j in range(y, y - o - 1, -1):
#                     if arr[i][j] == 0:
#                         flag = 1
#                         break
#             if flag == 0:
#                 cnt[o] += 1
#                 for k in range(x, x - o - 1, -1):
#                     for t in range(y, y - o - 1, -1):
#                         arr[k][t] = 0

arr = []
N = 10
for i in range(N):
    arr.append(list(map(int, input().split())))
ori = copy.deepcopy(arr)
# for g in arr:
#     print(g)
# print()


a = 0
my_min = 99999999999
for u in range(4, 0, -1):
    for l in range(N): # arr 초기화
        for p in range(N):
            arr[l][p] = ori[l][p]
    cnt = [0] * 5

    for o in range(u, -1, -1):
        find(o)

    print(cnt)
    if sum(cnt) < my_min:
        for i in range(5):
            if cnt[i] > 5:  # 조건을 불만족하면
                # print(-1)
                a = 1 # a = 1
                break
        if a == 0: # 조건을 전부 만족하는상황이면 my_min을 바꿔주자.
            my_min = sum(cnt)
    for g in arr:
        print(g)
    print()

if my_min == 99999999999:
    print(-1)
else:
    print(my_min)
