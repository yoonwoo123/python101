import sys, collections
sys.stdin = open("자동차경주_input.txt")

def racing(start, tsum):
    global sol
    if tsum >= sol: return
    if start > N:
        if tsum < sol:
            sol = tsum
        return
    tot = 0 # 거리 누적
    # 출발점에서 제한된 거리 이내에서 모두 정비를 받아보는 경우의 수 시도
    for i in range(start, N+1):
        if tot + meter[i] > limit: break # 거리 벗어나면 탈출
        tot += meter[i]
        racing(i+1, tsum+time[i])
    # meter = metime[0][0]
    # time = metime[0][1]
    # if limit < meter:
    #     return




limit = int(input())
N = int(input())
meter = list(map(int, input().split()))
totmeter = sum(meter)
time = list(map(int, input().split()))
time.append(0) # 길이가 안맞으므로
# metime = []
sol = 0x7fffffff
# for i in range(N):
#     metime.append([meter[i], time[i]])
# print(metime)
racing(0, 0)
print(sol)
# if metime[i] <= limit:
    