import sys
sys.stdin = open("해밀턴_input.txt")
# 순열 N = 5 이면 0,1,2,3,4 중 1,2,3,4 만 순열로

def perm(no):
    global my_min
    if no >= N-1:
        # print(a)
        tot = arr[0][a[i]]
        for i in range(N-1):
            tot += arr[a[i]][a[i+1]]
        tot = arr[a[-2]][a[]]
        if my_min > tot:
            my_min = tot
    else:
        for i in range(1, N):
            if chk[i] == 1: continue
            chk[i] = 1
            a[no] = i
            perm(no + 1)
            chk[i] = 0

N = int(input())
arr = []
a = [0] * (N)
chk = [0] * (N)
my_min = 999999999
for i in range(N):
    arr.append(list(map(int, input().split())))

perm(0)