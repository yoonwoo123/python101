import sys, itertools
sys.stdin = open("치킨배달2_input.txt")

def comb(no, cnt): # 현재 가정집(행) 에서 모든 치킨집을 가는 경우를 조합으로 뽑자
    global my_min
    # if tot >= my_min:
    #     return
    if cnt == M: # 스택 (열) 의 개수
        tot = 0
        for i in range(HN):
            nmin = 9999999
            for j in range(CN):
                if not chk[j]: continue
                if nmin > dist[i][j]:
                    nmin = dist[i][j]
            tot += nmin

        if tot < my_min:
            my_min = tot
        return
    if no >= CN: return # 치킨집
    # for i in range(len(house)): # 치킨집 (열)
    #     if chk[i] == 1: continue
    chk[no] = 1
    comb(no + 1, cnt + 1)
    chk[no] = 0
    comb(no + 1, cnt)

N, M = map(int, input().split())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))
# print(arr)
# 로봇-스낵 문제처럼 치킨집-집 문제이다. 치킨집 좌표는 뽑아두고
# 치킨집을 어떻게 고를지 조합으로 뽑아낸다.

# 집좌표를 순열로 바꿔가면서 최소값을 찾는다.
# 치킨집 = 2, 집 = 1

# 2. 토마토 응용 x
# 어차피 모든집까지의 거리를 계산해야하므로 치킨집을 토마토로 생각
# 각 집까지의 거리를 BFS로 찍어서 각 집까지 걸리는 시간을 저장한후
# 각집에 저장된 시간값을 더해서 그중 최소를 찾는다.

house = []
chicken = []
for x in range(N):
    for y in range(N):
        if arr[x][y] == 1:
            house.append([x, y])
        if arr[x][y] == 2:
            chicken.append([x, y])
HN = len(house)
CN = len(chicken)
# print(house)
# print(chicken)
my_min = 999999999999999
dist = [[0 for _ in range(CN)] for _ in range(HN)] # 각 치킨집 [x] 에서 가정집 [y] 까지의 거리를 계산
chk = [0] * CN
# print(A)

for x in range(HN): # 가정집을 행으로
    for y in range(CN): # 치킨집을 열(스택)으로
        dist[x][y] = abs(house[x][0] - chicken[y][0]) + abs(house[x][1] - chicken[y][1])

comb(0, 0)
print(my_min)
# itercomb = itertools.combinations(chicken, M)
# for i in itercomb:
#     print(i)

