import sys
sys.stdin = open("도약_input.txt")

def lowerSearch(s, e, term):
    sol = -1
    while s<=e:
        m = (s+e)//2
        if term <= leafs[m]:
            e = m-1 # 왼쪽 탐색
            sol = m # 찾은 위치가 왼쪽 경계치이므로 백업
        else:
            s = m+1
    return sol

def upperSearch(s, e, term):
    sol = -1
    while s<=e:
        m = (s+e)//2
        if  term >= leafs[m]:
            s = m+1 # 오른쪽 탐색
            sol = m # 찾은 위치가 왼쪽 경계치이므로 백업
        else:
            e = m-1
    return sol

N = int(input())
leafs = []
for i in range(N):
    leafs.append(int(input()))
leafs = sorted(leafs)
cnt = 0
for pos in range(N-2): # 첫번째 잎 위치
    for jmp in range(pos+1, N-1): # 두번째 잎 위치
        term = leafs[jmp] - leafs[pos]
        start = leafs[jmp] + term
        end = leafs[jmp] + term*2
        # for last in range(pos+2, len(leafs)): # 세번째 잎 위치
        lo = lowerSearch(jmp+1 , N - 1, start)
        if lo == -1 or leafs[lo]>end:
            continue

        up = upperSearch(jmp+1, N - 1, end)
        # if up == -1:
        #     break
        cnt += up - lo + 1
print(cnt)