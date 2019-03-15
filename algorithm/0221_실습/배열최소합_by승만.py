import sys
sys.stdin = open("배열최소합_input.txt")

def process_solution(a, k, sum):
    global min

    if sum > min : return

    # for i in range(1, k+1):
        # print(arr[i-1][data[a[i]]], end=" ")
    # print(min)
    # print()
    # return min


def make_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = True

    ncands = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncands] = i
            ncands += 1

    return ncands

def backtrack(a, k, input, sum):
    global min

    if sum > min: return

    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k, sum)
        if sum < min:
            min = sum
            sum=0
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, input, sum + arr[k-1][a[k]-1])


t = int(input())
for case in range(1, t+1):
    n = int(input())
    arr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))

    MAXCANDIDATES = 100
    NMAX = 100
    data = [0]
    min = 99999
    for i in range(n):
        data.append(i)
    a = [0] * NMAX
    backtrack(a, 0, n, 0)
    print("%s%d %d" % ('#', case, min))