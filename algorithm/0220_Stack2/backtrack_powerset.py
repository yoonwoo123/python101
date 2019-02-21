def process_solution(a, k):
    for i in range(1, k+1):
        if a[i] : print(data[i], end=" ")
    print()

def make_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input): # a=선택집합, k=선택한 수, input = 모든선택수
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k)
    else:
        k += 1
        ncands = make_candidates(a, k, input, c) # ncands = 2
        for i in range(ncands): # ncands 가 2이므로 0,1 반복 (True, False)
            a[k] = c[i] # a집합의 k번째에 True/False 를 넣어줌 a[1] = c[0]==True
            backtrack(a, k, input) # 재귀

MAXCANDIDATES = 100
NMAX = 100
data = [0, 1, 2, 3]
a = [0] * NMAX
backtrack(a, 0, 3)