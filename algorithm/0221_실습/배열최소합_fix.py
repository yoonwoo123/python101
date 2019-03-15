import sys
sys.stdin = open("배열최소합_input.txt")

def process_solution(a, k, sum): # 답을 출력하는 단계
    global min

    if sum > min: return
    # res = 0

    # for i in range(1, k+1): # i = [1,2,3]
    #     if a[i]:
    #         res += table[i-1][data[a[i]]-1] # 12, 9, 8
    #         total.append(res)
    # if total[-1] < res:
    #     return
    # else:
    #     total[-1] = res
    #     return total[-1]
    #         # if table[i-1][data[a[i]]-1] < my_min:
    #         #     my_min = table[i-1][data[a[i]]-1]


def make_candidates(a, k, input, c):
    in_perm = [False] * NMAX # in_perm 은 [0] * 100 개 빈리스트

    for i in range(1, k): # k = 1 안돈다/ k=2 i=1로 돈다./ k=3 i= 1, 2
        in_perm[a[i]] = True # in_perm[1] = 1이 된다.
                             # in_perm[2] = 1 , in_perm[3] = 1

    ncands = 0
    for i in range(1, input+1): # range=[1,2,3]
        if in_perm[i] == False: # in_perm[1] = 1 이므로 넘어감/ in_perm[1]은 들어감
            c[ncands] = i # c[0] = 1 , c[1] = 2, c[2] = 3/ c[0] = 2, c[1] = 3/ c[0] = 1
            ncands += 1 # ncands = 1 , 2 , 3 /
    return ncands # 3 / 2 / 1

def backtrack(a, k, input, sum): # a=선택집합, k=선택한 수, input = 모든선택수
    global min

    if sum > min: return

    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input: # k = 3 일 경우
        process_solution(a, k, sum) # k=3
        if sum < min:
            min = sum
            sum = 0
    else:
        k += 1  # k = 1 이 된다./ k = 2 / k = 3
        ncands = make_candidates(a, k, input, c) # ncands = 3 / 2 / 1
        for i in range(ncands): # ncands 가 3이므로 0,1,2 반복/ 0,1 / 0
            a[k] = c[i] # a집합의 k번째에 c[0] 를 넣어줌 a[1] = c[0] = 1/ a[2] = c[0] = 2
                        # a집합의 k번째에 c[1] 를 넣어줌 a[1] = c[1] = 2/ a[2] = c[1] = 3
                        # a[1] = c[2] = 3
                        # a[3] = c[0] = 1
            backtrack(a, k, input, sum + table[k-1][a[k]-1]) # 재귀



testcases = int(input())
for T in range(testcases):
    N = int(input())
    table = []
    total = []
    min = 99999
    MAXCANDIDATES = 100
    NMAX = 100
    data = range(N + 1)
    a = [0] * NMAX

    for i in range(N): # 세로 : x , 가로 : y  테이블 생성
        tmp =list(map(int, input().split()))
        table.append(tmp)
    backtrack(a, 0, N, 0)
    print("%s%d %d" % ('#', T+1, min))
