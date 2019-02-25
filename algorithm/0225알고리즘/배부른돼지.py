import sys
sys.stdin = open('배부른돼지_input.txt')

testcases = int(input())
true = []
false = []
for i in range(testcases):
    num, tf = input().split()
    num = int(num)

# 최소 먹이횟수 (min num) 을 찾아야한다.
# 돼지가 2번보다 적게 10번보다 많게는 좋아하지 않는다.

    if tf == 'Y':
        true.append(num)
    if tf == 'N':
        false.append(num)
# if len(true) == 0:
#     print('F')
if testcases == 0:
    print('F')
elif max(false) > min(true):
    print('F')
else:
    print(min(true))