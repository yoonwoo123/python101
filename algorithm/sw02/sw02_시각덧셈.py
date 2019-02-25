import sys
sys.stdin = open('sw02_시각덧셈_input.txt')

testcases = int(input())
for T in range(testcases):
    time = list(map(int,(input().split())))
    #시간덧셈
    hour = time[0] + time[2]
    if hour > 12:
        hour -= 12
    #분 덧셈
    min = time[1] + time[3]
    if min > 59:
        min -= 60
        hour += 1
    print(f'#{T+1} {hour} {min}')