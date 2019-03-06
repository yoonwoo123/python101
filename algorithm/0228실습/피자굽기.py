def solve():
    global N, M
    Q = []
    for i in range(1, N+1): # 화덕에 N개를 채움
        Q.append(i)
    idx = N + 1 # 아직 화덕에 넣지 않은 피자
    t = 0
    while len(Q) != 0:
        t = Q.pop(0)    # 치즈 확인
        if arr[t]//2 != 0: #치즈 남아있으면
            arr[t] //= 2
            Q.append(t) # 다시넣기
        elif idx <= M: # 치즈가 녹았으면 남은피자넣음
            Q.append(idx)
            idx += 1
        return t # 마지막으로 나온 피자 번호

import sys
sys.stdin = open('피자굽기_input.txt')
