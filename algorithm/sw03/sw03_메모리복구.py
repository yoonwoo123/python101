import sys
sys.stdin = open("sw03_메모리복구_input.txt")
testcases = int(input())
for T in range(testcases):
    cnt = 0
    pre = 0
    memory = input()
    # print(memory)
    # memory[0] 메모리의 앞부분을 확인하며 0인 부분을 제낀다
    # 1이 나오면 cnt가 1증가한다. 그뒤로 0이 나올때까지 검사해서 0이나오면 cnt += 1
    # 0이 나온뒤로는 또 1이 나오면 증가한다. 즉 1 > 0 > 1 > 0 반복
    # 반복문은 memory의 길이만큼 돌린다.
    for i in range(len(memory)):
        if int(memory[i]) == pre:
            continue
        if int(memory[i]) != pre:
            cnt += 1
            pre = int(memory[i])
    print(f'#{T+1} {cnt}')