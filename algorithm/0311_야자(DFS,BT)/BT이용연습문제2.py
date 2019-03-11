def process_solution(a, k, sum): # sum 추가
    global cnt
    sum = 0
    for i in range(1, k+1):
        if a[i] : sum += data[i]

    if sum == 10:
        for i in range(1, k+1):
            if a[i] : print(data[i], end=" ")
        print()
        cnt += 1

def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input, sum): # sum 추가
    if sum > 10 : return # 가지치기

    global MAXCANDIDATES, total_cnt
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k, sum)
    else:
        k += 1
        ncands = construct_candidates(a, k, input, c) # ncands = 2
        for i in range(ncands): # ncands 가 2이므로 0,1 반복 (True, False)
            a[k] = c[i] # a집합의 k번째에 True/False 를 넣어줌 a[1] = c[0]==True
            if a[k]: # 가지치기로 인해 추가된 항목
                backtrack(a, k, input, sum + data[k])
            else:
                backtrack(a, k, input, sum) # 재귀
    total_cnt += 1

MAXCANDIDATES = 100
NMAX = 100
# data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data = range(11)
a = [0] * NMAX
cnt = 0
total_cnt = 0
backtrack(a, 0, 10, 0) # ,0 추가 (sum)
print("%s %d" % ('count:', cnt))
print("%s %d" % ('total_count', total_cnt))
# print(f"count:{cnt}")
# print(f"total_count:{total_cnt}")