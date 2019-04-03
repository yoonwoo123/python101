def process_solution(a, k): # 답을 출력하는 단계
    global cnt
    for i in range(1, k+1): # i = [1,2,3]
        if a[i] : print(data[a[i]], end=" ")
    print()
    cnt += 1
def make_candidates(a, k, input, c):
    in_perm = [False] * NMAX # in_perm 은 [0] * 100 개 빈리스트 # visited의 뜻

    for i in range(1, k): # k = 1 안돈다/ k=2 i=1로 돈다./ k=3 i= 1, 2
        in_perm[a[i]] = True # in_perm[1] = 1이 된다.
                             # in_perm[2] = 1 , in_perm[3] = 1

    ncands = 0
    for i in range(1, input+1): # range=[1,2,3]
        if in_perm[i] == False: # in_perm[1] = 1 이므로 넘어감/ in_perm[1]은 들어감
            c[ncands] = i # c[0] = 1 , c[1] = 2, c[2] = 3/ c[0] = 2, c[1] = 3/ c[0] = 1
            ncands += 1 # ncands = 1 , 2 , 3 /
    return ncands # 3 / 2 / 1

def backtrack(a, k, input): # a=선택집합, k=선택한 수, input = 모든선택수
    global MAXCANDIDATES, total_cnt
    c = [0] * MAXCANDIDATES

    if k == input: # k = 3 일 경우
        process_solution(a, k) # k=3
    else:
        k += 1  # k = 1 이 된다./ k = 2 / k = 3
        ncands = make_candidates(a, k, input, c) # ncands = 3 / 2 / 1
        for i in range(ncands): # ncands 가 3이므로 0,1,2 반복/ 0,1 / 0
            a[k] = c[i] # a집합의 k번째에 c[0] 를 넣어줌 a[1] = c[0] = 1/ a[2] = c[0] = 2
                        # a집합의 k번째에 c[1] 를 넣어줌 a[1] = c[1] = 2/ a[2] = c[1] = 3
                        # a[1] = c[2] = 3
                        # a[3] = c[0] = 1
            backtrack(a, k, input) # 재귀
    total_cnt += 1

MAXCANDIDATES = 100
NMAX = 100
data = range(7)
a = [0] * NMAX
cnt = 0
total_cnt = 0
backtrack(a, 0, 6)
print("%s %d" % ('count:', cnt))
# print(f"total_count:{total_cnt}")
print("%s %d" % ('total_count:', total_cnt))